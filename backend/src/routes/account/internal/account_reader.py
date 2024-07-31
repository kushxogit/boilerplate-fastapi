from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from ..store.account_models import Account

MONGODB_URL = "mongodb://localhost:27017/"
client = AsyncIOMotorClient(MONGODB_URL)
database = client["example_db"]
user_collection = database.get_collection("users")

async def get_database():
    return database

class AccountReader:
    @staticmethod
    async def get_user_by_email(email):
        return await Account.find_one(Account.email == email)