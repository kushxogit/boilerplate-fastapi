# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file contains the AuthService class which provides methods for user authentication and token verification.

from .internal.auth_reader import AuthReader  # Importing AuthReader for fetching user data.
from .internal.auth_writer import AuthWriter  # Importing AuthWriter for handling JWT tokens.

class AuthService:
    @staticmethod
    async def authenticate_user(username, password):
        # Authenticates a user by their username and password.
        user = await AuthReader.get_user_by_username(username)  # Fetching the user from the database.
        if user and user.password == password:
            # If the user exists and the password matches, create an access token.
            return AuthWriter.create_access_token({"sub": username})
        return None  # Return None if authentication fails.

    @staticmethod
    async def verify_user_token(token):
        # Verifies a JWT token.
        return AuthWriter.decode_jwt(token)  # Decoding the JWT token.