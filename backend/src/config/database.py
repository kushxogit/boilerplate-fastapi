# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file configures the database connection and initializes Beanie for MongoDB.

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


# MongoDB settings
MONGO_DETAILS = "mongodb://localhost:27017"  # MongoDB connection string
DATABASE_NAME = "example_db"  # Database name

client = AsyncIOMotorClient(MONGO_DETAILS)  # Create a MongoDB client
database = client[DATABASE_NAME]  # Select the database

async def init_beanie_db():
    await init_beanie(database=database, document_models=[])  # Initialize Beanie with the database and models