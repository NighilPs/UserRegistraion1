

from pymongo import MongoClient
from storage.configuration import MongoDBDatabase

MongoDBDatabase = MongoDBDatabase()

MONGO_USERNAME = MongoDBDatabase.mongo_user_name
MONGO_PASSWORD = MongoDBDatabase.mongo_password
MONGO_HOST = MongoDBDatabase.mongo_host
MONGO_PORT = MongoDBDatabase.mongo_port
MONGO_DB = MongoDBDatabase.mongo_db
 
# Create a MongoDB client
client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}")
mongodb = client[MONGO_DB]