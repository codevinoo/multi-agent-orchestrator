from orchestrator.agents.base import Agent


class WorkerAgent(Agent):
    def __init__(self, name: str, bus, tools: dict):
        super().__init__(name, bus)
        self.tools = tools

    async def handle(self, message: dict) -> None:
        task = message.get("task", "")
        result = await self._execute(task)
        await self.send("tasks.completed", {"task": task, "result": result})

    async def _execute(self, task: str) -> str:
        if "Research" in task and "search" in self.tools:
            return self.tools["search"](task)
        return f"completed: {task}"
