import motor.motor_asyncio

from app.config.config import MONGODB_URI, MONGODB_NAME


async def get_client(cluster_uri: str = MONGODB_URI):
    return motor.motor_asyncio.AsyncIOMotorClient(cluster_uri)


async def get_database(cluster_uri: str = MONGODB_URI, database_name: str = MONGODB_NAME):
    client = await get_client(cluster_uri)
    return client.get_database(database_name)