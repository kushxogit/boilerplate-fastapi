from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from bson import ObjectId

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    full_name: str

class UserResponse(BaseModel):
    id: Optional[str]
    email: EmailStr
    full_name: str

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }
