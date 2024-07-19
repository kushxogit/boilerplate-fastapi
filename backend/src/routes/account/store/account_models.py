from beanie import Document,Indexed

class Account(Document):
    email: str=Indexed(unique=True)
    password: str
