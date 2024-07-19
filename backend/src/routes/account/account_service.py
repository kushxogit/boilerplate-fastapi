from .internal.account_reader import AccountReader
# from .internal.account_writer import AccountWriter

class AccountService:
    @staticmethod
    async def login_user(email:str,password:str):
        user=await AccountReader.get_user_by_email(email)
        if user and user.password==password:
            return user
        return None
    
    
    
    
    #         return AccountWriter.create_access_token({"sub":username})
    #     return None
    # @staticmethod
    # async def verify_user_token(token:str):
    #     return AccountWriter.decode_jwt(token)    