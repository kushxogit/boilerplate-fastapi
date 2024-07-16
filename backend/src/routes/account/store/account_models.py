from beanie import Document,Indexed

class Account(Document):
    account_id: int
    username: str=Indexed(unique=True)
    password: str