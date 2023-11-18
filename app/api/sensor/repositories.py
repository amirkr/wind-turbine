from typing import Optional

from app.database.mongo import get_database
from app.api.sensor.models import SensorModel, ResponseCreateSensorModel
from app.utils.helpers import mongo_exception_handler

class SensorRepository:
    async def get_sensor_collection(self):
        database = await get_database()
        return database.get_collection("sensor")

    @mongo_exception_handler
    async def insert_sensor(self, sensor: SensorModel) -> Optional[str]:
        sensor_collection = await self.get_sensor_collection()

        new_sensor = await sensor_collection.insert_one(
            {"name": sensor.name, "unit": sensor.unit},
        )

        sensor = ResponseCreateSensorModel(id=str(new_sensor.inserted_id))
        return sensor.model_dump()

    @mongo_exception_handler
    async def does_sensor_exist(self, sensor: SensorModel) -> bool:
        does_sensor_exist = False
        sensor_collection = await self.get_sensor_collection()
        sensor_match_count = await sensor_collection.count_documents(
            {"name": sensor.name},
        )
        if sensor_match_count > 0:
            does_sensor_exist = True

        return does_sensor_exist