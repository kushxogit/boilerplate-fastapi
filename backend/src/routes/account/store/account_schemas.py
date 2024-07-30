from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from bson import ObjectId

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    phoneNumber:str

class UserResponse(BaseModel):
    id: Optional[str]
    email: EmailStr
    phoneNumber: str

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }
