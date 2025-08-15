from orchestrator.agents.base import Agent


class PlannerAgent(Agent):
    async def decompose(self, goal: str) -> list[str]:
        steps = [
            f"Research: {goal}",
            f"Analyze findings for: {goal}",
            f"Write summary of: {goal}",
        ]
        await self.send("tasks.created", {"steps": steps, "goal": goal})
        return steps
