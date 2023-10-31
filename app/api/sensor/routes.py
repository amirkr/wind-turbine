from typing import List

from fastapi import APIRouter, Body, Depends
from app.api.sensor.models import SensorModel, ResponseCreateSensorModel
from app.api.sensor.services import SensorService

sensor = APIRouter(prefix="/api/sensor")

@sensor.get("/")
async def get_sensor_list() -> List[SensorModel]:
    pass

@sensor.get("/{sensor_id}")
async def get_sensor(sensor_id: int) -> SensorModel:
    pass

@sensor.post("/")
async def create_sensor(sensor: SensorModel = Body(...), sensor_service: SensorService = Depends()) -> ResponseCreateSensorModel:
    return await sensor_service.create_sensor(sensor)