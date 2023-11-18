from fastapi import Depends

from app.api.sensor.repositories import SensorRepository
from app.api.sensor.models import SensorModel
from app.utils.exceptions import BadRequestException


class SensorService:
    def __init__(self, sensor_repository: SensorRepository = Depends()) -> None:
        self.sensor_repository = sensor_repository

    async def create_sensor(self, sensor: SensorModel):
        does_sensor_exist = await self.sensor_repository.does_sensor_exist(sensor)
        # Checking if a sensor with the same already exists in the db
        if does_sensor_exist is True:
            raise BadRequestException(message="this sensor already exists", action="api.sensor.services", status_code=400)
        inserted_sensor_id = await self.sensor_repository.insert_sensor(sensor)

        return inserted_sensor_id