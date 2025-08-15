from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    def __init__(self, name: str, bus):
        self.name = name
        self.bus = bus

    @abstractmethod
    async def handle(self, message: dict[str, Any]) -> None:
        ...

    async def send(self, topic: str, payload: dict[str, Any]) -> None:
        await self.bus.publish(topic, {"from": self.name, **payload})
