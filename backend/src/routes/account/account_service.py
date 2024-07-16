from ..store.account_schemas import UserCreate
from .internal.account_writer import create_user, get_user_by_email

async def register_new_user(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        return None
    new_user = await create_user(user)
    return new_user
