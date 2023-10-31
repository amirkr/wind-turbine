from fastapi import Depends

from app.api.sensor.repositories import SensorRepository
from app.api.sensor.models import SensorModel, ResponseCreateSensorModel

class SensorService:
    def __init__(self, sensor_repository: SensorRepository = Depends()) -> None:
        self.sensor_repository = sensor_repository

    async def create_sensor(self, sensor: SensorModel):
        inserted_sensor_id = await self.sensor_repository.insert_sensor(sensor)

        return inserted_sensor_id