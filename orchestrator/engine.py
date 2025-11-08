import asyncio
from orchestrator.bus import MessageBus
from orchestrator.agents.planner import PlannerAgent
from orchestrator.agents.worker import WorkerAgent
from orchestrator.tools.search import web_search


class Orchestrator:
    def __init__(self):
        self.bus = MessageBus()
        self.planner = PlannerAgent("planner", self.bus)
        self.worker = WorkerAgent("worker-1", self.bus, {"search": web_search})
        self.results: list[dict] = []
        self.bus.subscribe("tasks.completed", self._on_complete)

    async def _on_complete(self, msg: dict) -> None:
        self.results.append(msg)

    async def run(self, goal: str) -> list[dict]:
        steps = await self.planner.decompose(goal)
        for step in steps:
            await self.bus.publish("tasks.assigned", {"task": step, "from": "planner"})
            await self.worker.handle({"task": step})
        return self.results
