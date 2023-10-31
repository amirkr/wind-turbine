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