# WRITING COMMENTS INITIALLY FOR BETTER ONBOARDING AND EASIER UNDERSTANDING P.S. WE WILL REMOVE THESE AFTER WE ALL KNOW HOW ITS WORKING
# This file is the main entry point for the FastAPI application.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, JSONResponse

from src.config.database import init_beanie_db, database  # Import the database object
from src.config.config import APP_NAME, VERSION

from src.routes.auth.auth_main import router as auth_router

app = FastAPI(
    title=APP_NAME,  # Set the title of the application
    version=VERSION  # Set the version of the application
)

# Configure CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
    allow_credentials=True
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.on_event("startup")
async def startup_event():
    await init_beanie_db()  # Initialize the database connection on startup

# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    Redirect to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")

# Swagger expects the auth-URL to be /token, but in our case it is /auth/token
# So, we redirect /token -> /auth/token
@app.post("/token")
def forward_to_login():
    """
    Redirect to token-generation (`/auth/token`). Used to make Auth in Swagger-UI work.
    """
    return RedirectResponse(url="/auth/token")

@app.get("/test-db")
async def test_database_connection():
    try:
        await database.command("ping")  # Test the database connection
        return JSONResponse(content={"status": "Database connection is successful"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"status": "Database connection failed", "error": str(e)}, status_code=500)