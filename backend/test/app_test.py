import httpx
import pytest
from main import app
from src.util.db_dependency import get_db
from src.config.database import database  # Import the database object
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.routes.users.models import User  # Import your Beanie document models

"""
    Explanation of what is happening here can be found in the FastAPI Docs:
    https://fastapi.tiangolo.com/advanced/testing-database/
    https://fastapi.tiangolo.com/tutorial/testing/
"""

# Setup test database and initialize Beanie
@pytest.fixture(scope="module")
async def test_db():
    # Connect to the test MongoDB database
    client = AsyncIOMotorClient("mongodb://localhost:27017/test_database")
    # Initialize Beanie with the test database and document models
    await init_beanie(database=client.test_database, document_models=[User])
    yield
    # Optional: Drop the test database after tests are done
    client.drop_database("test_database")

# Test to check database connection
@pytest.mark.asyncio
async def test_database_connection(test_db):
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/test-db")
        assert response.status_code == 200, f"Database connection failed: {response.text}"