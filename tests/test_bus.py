import asyncio
from orchestrator.bus import MessageBus


async def test_publish_subscribe():
    bus = MessageBus()
    received = []

    async def handler(msg):
        received.append(msg)

    bus.subscribe("test", handler)
    await bus.publish("test", {"data": "hello"})
    assert len(received) == 1
    assert received[0]["data"] == "hello"


def test_message_bus():
    asyncio.run(test_publish_subscribe())
