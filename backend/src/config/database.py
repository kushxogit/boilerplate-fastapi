# Import logging module to log messages
import logging

# Import AsyncIOMotorClient for asynchronous MongoDB operations
from motor.motor_asyncio import AsyncIOMotorClient
# Import init_beanie to initialize Beanie with MongoDB
from beanie import init_beanie
from backend.src.routes.account.store.auth_models import Account

# Import UserCredentials model from auth_models
from src.routes.auth.store.auth_models import UserCredentials

# MongoDB connection string
MONGO_DETAILS = "mongodb://localhost:27017/"
# Database name
DATABASE_NAME = "example_db"

# Create a MongoDB client
client = AsyncIOMotorClient(MONGO_DETAILS)
# Select the database
database = client[DATABASE_NAME]

# Configure basic logging
logging.basicConfig(level=logging.INFO)
# Create a logger for this module
logger = logging.getLogger(__name__)

# Function to initialize Beanie with the database and models
async def init_beanie_db():
    try:
        # Initialize Beanie with the database and UserCredentials model
        await init_beanie(database=database, document_models=[UserCredentials, Account])
        logger.info("Beanie initialized with database and models.")
        # Check if dummy data already exists
        existing_user = await UserCredentials.find_one(UserCredentials.username == "testuser")
        if not existing_user:
            # Insert dummy data if it doesn't exist
            await insert_dummy_data()
    except Exception as e:
        logger.error(f"Failed to initialize Beanie: {e}")

# Function to insert dummy data into the database
async def insert_dummy_data():
    try:
        # Create a dummy user
        dummy_user = UserCredentials(account_id=1, username="testuser", password="testpassword")
        # Insert the dummy user into the database
        await dummy_user.insert()
        logger.info("Dummy data inserted successfully.")
    except Exception as e:
        logger.error(f"Failed to insert dummy data: {e}")