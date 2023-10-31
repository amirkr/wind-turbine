from pymongo import MongoClient, ASCENDING

# TODO Try pymongo-migration
mongo_client = MongoClient("mongodb://mongo:27017")
mongo_db = mongo_client.get_database("wind_turbine")
sensor_collection = mongo_db.get_collection("sensor")
sensor_collection.create_index( [("name", ASCENDING)], unique=True )