from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends

MONGODB_URL = "mongodb://localhost:27017/"
client = AsyncIOMotorClient(MONGODB_URL)
database = client["example_db"]
user_collection = database.get_collection("users")

async def get_database():
    return database
