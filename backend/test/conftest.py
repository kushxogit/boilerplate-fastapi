from fastapi.testclient import TestClient
from main import app
import pytest
from src.util.db_dependency import get_db
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import asyncio

from src.routes.users.models import User

# MongoDB test settings
MONGO_TEST_DETAILS = "mongodb://localhost:27018"  # Use a different port for testing
DATABASE_TEST_NAME = "example_test_db"

client = AsyncIOMotorClient(MONGO_TEST_DETAILS)
database = client[DATABASE_TEST_NAME]

async def init_beanie_test_db():
    await init_beanie(database=database, document_models=[User])

@pytest.fixture(scope="module")
async def test_db(setup_event_loop):
    loop = setup_event_loop
    client = AsyncIOMotorClient("mongodb://localhost:27017/test_database", io_loop=loop)
    await init_beanie(database=client.test_database, document_models=[User])
    yield
    client.close()

@pytest.fixture
def db():
    # Adjust to use Beanie for MongoDB
    app.dependency_overrides[get_db] = lambda: database
    yield database
    # Cleanup logic here, if necessary

@pytest.fixture
def client():
    return TestClient(app)

# Adjust user fixture to work with MongoDB
@pytest.fixture
async def user_1(db):
    u = User(
        first_name="Saul",
        last_name="Goodman",
        email="saul.goodman@wexler-mcgill.law",
        password="hashed_password",  # Assume password is already hashed for simplicity
        super_admin=True,
        disabled=False
    )
    await u.insert()  # Use Beanie's insert method
    yield u
    await u.delete()  # Use Beanie's delete method

@pytest.fixture
async def regular_user(db):
    user = User(
        first_name="Kim",
        last_name="Wexler",
        email="kim.wexler@wexler-mcgill.law",
        password="hashed_password",
        super_admin=False,
        disabled=False
    )
    await user.insert()  # Use Beanie's insert method
    yield user
    await user.delete()  # Use Beanie's delete method

@pytest.fixture(scope="session", autouse=True)
def setup_event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()