from fastapi import FastAPI
from .rest_api.account_controller import router as account_router

app = FastAPI()

app.include_router(account_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
