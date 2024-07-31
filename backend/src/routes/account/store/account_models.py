from beanie import Document, Indexed
from pydantic import EmailStr

class Account(Document):
    email: EmailStr = Indexed(unique=True)
    password: str
    phoneNumber: str = Indexed(unique=True)