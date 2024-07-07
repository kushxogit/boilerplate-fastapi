from beanie import Document
from pydantic import EmailStr

class User(Document):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    super_admin: bool
    disabled: bool