from pydantic import BaseModel, Field

class SensorModel(BaseModel):
    name: str = Field(..., description="Sensor name", examples=["Main Bearer Sensor"])
    unit: str = Field(..., description="Sensor unit", examples=["Celsius"])

class ResponseCreateSensorModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs["id"]

    id: str = Field(..., examples=["65401d8f393232b0520a354d"])