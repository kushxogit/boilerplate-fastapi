# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file defines Pydantic models for various authentication-related schemas.

from pydantic import BaseModel

# This model represents the token response
class Token(BaseModel):
    access_token: str
    token_type: str

# This model represents the token data
class TokenData(BaseModel):
    username: str | None = None

# This model represents the email schema
class EmailSchema(BaseModel):
    email: str

# This model represents the set new password schema
class SetNewPassword(BaseModel):
    user_id: int
    reset_token: str
    new_password: str

# This model represents the password schema
class Password(BaseModel):
    new_password: str