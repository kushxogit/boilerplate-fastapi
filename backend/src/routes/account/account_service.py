from src.routes.account.store.account_schemas import UserCreate
from src.routes.account.internal.account_writer import create_user, get_user_by_email
from .internal.account_reader import AccountReader

class AccountService:
    @staticmethod
    async def login_user(email:str,password:str):
        user=await AccountReader.get_user_by_email(email)
        if user and user.password==password:
            return user
        return None
      
    
async def register_new_user(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        return None
    new_user = await create_user(user)
    return new_user