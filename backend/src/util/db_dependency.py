from ..config.database import database

async def get_db():
    yield database