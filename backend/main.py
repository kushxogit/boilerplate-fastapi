from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, JSONResponse

from src.config.database import init_beanie_db, database  # Import the database object
from src.config.config import APP_NAME, VERSION


from src.routes.users.main import router as users_router
from src.routes.auth.main import router as auth_router

app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Include routers
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.on_event("startup")
async def startup_event():
    await init_beanie_db()

# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")


# Swagger expects the auth-URL to be /token, but in our case it is /auth/token
# So, we redirect /token -> /auth/token
@app.post("/token")
def forward_to_login():
    """
    # Redirect
    to token-generation (`/auth/token`). Used to make Auth in Swagger-UI work.
    """
    return RedirectResponse(url="/auth/token")

@app.get("/test-db")
async def test_database_connection():
    try:
        # Perform a simple operation to test the database connection
        await database.command("ping")  # MongoDB ping command
        return JSONResponse(content={"status": "Database connection is successful"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"status": "Database connection failed", "error": str(e)}, status_code=500)