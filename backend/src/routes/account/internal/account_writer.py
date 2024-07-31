from src.routes.account.store.account_schemas import UserCreate
from src.routes.account.internal.account_reader import user_collection

async def create_user(user: UserCreate):
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    new_user = await user_collection.find_one({"_id": result.inserted_id})
    return new_user

async def get_user_by_email(email: str):
    user = await user_collection.find_one({"email": email})
    return user
