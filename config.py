import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "test"
KAFKA_CONSUMER_GROUP = "group-1"
loop = asyncio.get_event_loop()
