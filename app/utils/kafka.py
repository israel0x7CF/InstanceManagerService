import asyncio
import contextlib
import os

from app.KafkaManager.producer import create_response
from app.schema.instance import CreateInstanceMsg



from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC           = "events"
GROUP_ID        = "fastapi-group"



producer: AIOKafkaProducer | None = None
consumer: AIOKafkaConsumer | None = None
_consumer_task: asyncio.Task | None = None



async def start_kafka() -> None:
    """Start both producer and consumer (and spin up the consume loop)."""
    print("starting kafka...............")
    global producer, consumer, _consumer_task

    # **create** inside coroutine, so asyncio.get_running_loop() works
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP,
    )
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        group_id=GROUP_ID,
        auto_offset_reset="earliest",
    )
    await producer.start()
    await consumer.start()

    async def _consume_loop() -> None:
        async for msg in consumer:
            print(f"[kafka] {msg.topic}:{msg.partition}@{msg.offset} → {msg.value!r}")
            instance_config_json = msg.value.decode('utf-8')
            management_service = CreateInstanceMsg(instanceName=instance_config_json["instanceName"],moduleName=instance_config_json["moduleName"],modulePath=instance_config_json["modulePath"])
            instance_data = management_service.create_container()
            await create_response(instance_data)

    global _consumer_task
    _consumer_task = asyncio.create_task(_consume_loop())

async def stop_kafka()-> None:
    if _consumer_task:
        _consumer_task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await  _consumer_task
        await producer.stop()
        await consumer.stop()

