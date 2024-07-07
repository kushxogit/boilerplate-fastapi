# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file contains the AuthReader class which is responsible for reading user data from the database.

from ..store.auth_models import UserCredentials  # Importing the UserCredentials model from the auth_models file.

class AuthReader:
    @staticmethod
    async def get_user_by_username(username):
        # Fetches a user by username from the database.
        return await UserCredentials.find_one(UserCredentials.username == username)