from ..store.account_models import Account
class AccountReader:
    @staticmethod
    async def get_user_by_email(email):
        return await Account.find_one(Account.email==email)
    
    #we can also find user by userid?