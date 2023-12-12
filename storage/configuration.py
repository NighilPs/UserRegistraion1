from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class PostgresDatabase(BaseSettings):
    host = os.getenv('pg_database_host')
    port = os.getenv('pg_database_port')
    user_name = os.getenv('pg_database_username')
    password = os.getenv('pg_database_password')
    db = os.getenv('pg_database')

class MongoDBDatabase(BaseSettings):
    mongo_host = os.getenv('mongo_host')
    mongo_port = os.getenv('mongo_port')
    mongo_user_name = os.getenv('mongo_username')
    mongo_password = os.getenv('mongo_password')
    mongo_db = os.getenv('mongo_db')
    



