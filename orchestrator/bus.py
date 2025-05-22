import asyncio
from collections import defaultdict
from typing import Any, Callable, Awaitable

MessageHandler = Callable[[dict[str, Any]], Awaitable[None]]


class MessageBus:
    def __init__(self):
        self._subscribers: dict[str, list[MessageHandler]] = defaultdict(list)
        self._history: list[dict[str, Any]] = []

    def subscribe(self, topic: str, handler: MessageHandler) -> None:
        self._subscribers[topic].append(handler)

    async def publish(self, topic: str, message: dict[str, Any]) -> None:
        msg = {"topic": topic, **message}
        self._history.append(msg)
        for handler in self._subscribers[topic]:
            await handler(msg)

    def history(self) -> list[dict[str, Any]]:
        return list(self._history)
