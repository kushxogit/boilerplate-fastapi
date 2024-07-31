# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file is the main entry point for the FastAPI application.
import sys
import os

# Import FastAPI for creating the web application
from fastapi import FastAPI
# Import CORSMiddleware for handling CORS
from fastapi.middleware.cors import CORSMiddleware
# Import RedirectResponse and JSONResponse for handling responses
from starlette.responses import RedirectResponse, JSONResponse

# Import init_beanie_db and database from database configuration
from src.config.database import init_beanie_db, database
# Import APP_NAME and VERSION from configuration
from src.config.config import APP_NAME, VERSION

# Import auth_router from auth_main
from src.routes.auth.auth_main import router as auth_router

from src.routes.account.account_main import router as account_router

# Create a FastAPI instance with title and version
app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

# Configure CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Include the authentication router with a prefix and tag
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

app.include_router(account_router,prefix="/accounts",tags=["Account"])

# Event handler for application startup
@app.on_event("startup")
async def startup_event():
    # Initialize the database connection on startup
    await init_beanie_db()

# Route to redirect / to Swagger-UI documentation
@app.get("/")
def main_function():
    """
    Redirect to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")

# Route to redirect /token to /auth/token for Swagger-UI authentication
@app.post("/token")
def forward_to_login():
    """
    Redirect to token-generation (`/token`). Used to make Auth in Swagger-UI work.
    """
    return RedirectResponse(url="/token")

# Route to test the database connection
@app.get("/test-db")
async def test_database_connection():
    try:
        # Test the database connection
        await database.command("ping")
        return JSONResponse(content={"status": "Database connection is successful"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"status": "Database connection failed", "error": str(e)}, status_code=500)


from src.routes.account.account_main import router as account_router


app.include_router(account_router, prefix="/account", tags=["Account"])