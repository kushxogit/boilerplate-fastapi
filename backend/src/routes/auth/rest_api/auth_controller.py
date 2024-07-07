# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file contains the API endpoints for handling authentication requests.

from fastapi import HTTPException, status  # Importing FastAPI's HTTPException for error handling.
from ..auth_service import AuthService  # Importing the AuthService class for authentication logic.
from pydantic import BaseModel  # Importing BaseModel from Pydantic for request data validation.

class AuthDetails(BaseModel):
    # Pydantic model for authentication details.
    username: str
    password: str

async def login_for_access_token(auth_details: AuthDetails):
    # Endpoint for logging in and getting an access token.
    token = await AuthService.authenticate_user(auth_details.username, auth_details.password)  # Authenticating the user.
    if not token:
        # If authentication fails, raise an HTTP 401 error.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return {"access_token": token, "token_type": "bearer"}  # Returning the access token.

async def verify_token(token: str):
    # Endpoint for verifying the validity of an access token.
    payload = await AuthService.verify_user_token(token)  # Verifying the token.
    if not payload:
        # If token verification fails, raise an HTTP 401 error.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"message": "Token is valid", "data": payload}  # Returning the verification result.