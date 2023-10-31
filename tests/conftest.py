import motor.motor_asyncio
from unittest import mock

import pytest
from httpx import AsyncClient
from mongomock_motor import AsyncMongoMockClient
from pymongo import ASCENDING

from app.config import config
from app.main import app


TEST_MONGODB_NAME = "db_test"


@pytest.fixture
async def mongo_mock():
    yield AsyncMongoMockClient()


@pytest.fixture
async def fastapi_app():
    async with AsyncClient(app=app, base_url="http://test") as fastapi_app:
        yield fastapi_app


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def mongo_fastapi_app_mock(fastapi_app, mongo_mock):
    async def get_mongodb_mock():
        mongodb = mongo_mock.get_database(config.MONGODB_NAME)
        await mongodb.sensor.create_index( [("name", ASCENDING)], unique=True )
        return mongodb

    with mock.patch("app.api.sensor.repositories.get_database", get_mongodb_mock):
        yield fastapi_app, mongo_mock


@pytest.fixture
async def test_mongo_client():
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017")
    yield mongo_client


@pytest.fixture
async def test_mongo_fastapi_app_mock(fastapi_app, test_mongo_client):
    async def get_sensor_mongodb_mock():
        mongo_db = test_mongo_client.get_database(TEST_MONGODB_NAME)
        sensor_collection = mongo_db.get_collection("sensor")
        sensor_collection.create_index( [("name", ASCENDING)], unique=True )
        return test_mongo_client.get_database(TEST_MONGODB_NAME)

    with mock.patch("app.api.sensor.repositories.get_database", get_sensor_mongodb_mock):
        yield fastapi_app, test_mongo_client
