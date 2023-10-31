import pytest
from bson import ObjectId


pytestmark = pytest.mark.anyio

"""
    create sensor `POST /api/sensor/` endpoint E2E test
"""
async def test_create_sensor(mongo_fastapi_app_mock):
    fastapi_app, mongo_mock = mongo_fastapi_app_mock

    sensor_dict = {
        "name": f"Spare Main Bearing Sensor",
        "unit": "Celsius",
    }
    response = await fastapi_app.post(url="/api/sensor/", json=sensor_dict)
    created_sensor = response.json()
    created_sensor_id = created_sensor.get("id")
    sensor_collection = mongo_mock.get_database("wind_turbine").sensor
    inserted_sensor = await sensor_collection.find_one({"_id": ObjectId(created_sensor_id)})
    sensor_dict["_id"] = ObjectId(created_sensor_id)
    
    assert response.status_code == 200
    assert inserted_sensor == sensor_dict


"""
    We check that we can't create two sensors with the same name
"""
async def test_create_duplicate_sensor(test_mongo_fastapi_app_mock):
    fastapi_app, test_mongodb = test_mongo_fastapi_app_mock
    sensor_collection = test_mongodb.get_database("db_test").sensor
    await sensor_collection.drop()

    sensor_dict = {
        "name": f"Test Temperature Sensor",
        "unit": "Celsius",
    }



    response_1 = await fastapi_app.post(url="/api/sensor/", json=sensor_dict)
    assert response_1.status_code == 200

    inserted_sensor = await sensor_collection.find_one({"name": sensor_dict["name"]})
    inserted_sensor.pop("_id")
    assert inserted_sensor == sensor_dict

    response_2 = await fastapi_app.post(url="/api/sensor/", json=sensor_dict)

    assert response_2.status_code == 400


