from ..store.account_models import Account
class AccountReader:
    @staticmethod
    async def get_user_by_username(username):
        return await Account.find_one(Account.username==username)
    
    #we can also find user by userid?