# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file sets up the API router for authentication-related endpoints.

from fastapi import APIRouter  # Importing APIRouter from FastAPI to create route handlers.
from .rest_api.auth_controller import login_for_access_token, verify_token  # Importing the authentication controller functions.

router = APIRouter(prefix="/auth", tags=["Authentication"])  # Creating a router for authentication routes.

router.post("/token", response_model=dict)(login_for_access_token)  # Registering the login endpoint.
router.get("/verify-token", response_model=dict)(verify_token)  # Registering the token verification endpoint.