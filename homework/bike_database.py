from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://admin:<password>@cluster0-nmvb5.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

bike_data = client.db_bike
Bikes = bike_data["Bikes"]