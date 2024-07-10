# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file defines the MongoDB document models for user credentials.

from beanie import Document

class Account(Document):
    account_id: int
    username: str
    password: str  # Note: In a real application, you should always encrypt passwords.