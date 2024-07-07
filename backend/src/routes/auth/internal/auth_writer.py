# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file contains the AuthWriter class which is responsible for writing (creating and decoding) JWT tokens.

import jwt  # Importing the jwt library for encoding and decoding JWTs.
from datetime import datetime, timedelta  # Importing datetime utilities for setting token expiration.
from fastapi import HTTPException, status  # Importing FastAPI's HTTPException for error handling.

SECRET_KEY = "your_secret_key_here"  # Secret key for JWT encoding and decoding.
ALGORITHM = "HS256"  # Algorithm used for JWT encoding.
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes.

class AuthWriter:
    @staticmethod
    def create_access_token(data: dict):
        # Creates a JWT access token with an expiration time.
        to_encode = data.copy()  # Copying data to avoid modifying the original dict.
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Setting the expiration time.
        to_encode.update({"exp": expire})  # Adding the expiration time to the token data.
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encoding the JWT.
        return encoded_jwt

    @staticmethod
    def decode_jwt(token: str):
        # Decodes a JWT token and checks its validity.
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Attempting to decode the token.
            return decoded if decoded['exp'] >= datetime.utcnow().timestamp() else None  # Checking if the token is expired.
        except jwt.PyJWTError:
            # Handling the error if token decoding fails.
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")