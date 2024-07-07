from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import asyncio

from ..routes.users.models import User

# MongoDB settings
MONGO_DETAILS = "mongodb://localhost:27017"
DATABASE_NAME = "example_db"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client[DATABASE_NAME]

async def init_beanie_db():
    await init_beanie(database=database, document_models=[User])