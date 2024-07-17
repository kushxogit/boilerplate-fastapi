from fastapi import FastAPI, HTTPException
from .rest_api.auth_controller import login_for_access_token, verify_token
from .internal.auth_writer import create_user, update_user, disable_user

app = FastAPI()

app.include_router(login_for_access_token)
app.include_router(verify_token)

@app.post("/register")
async def register_user(username: str, password: str, email: str, full_name: str):
    try:
        user = create_user(username, password, email, full_name)
        return {"msg": "User created successfully", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/update-user")
async def update_user_info(username: str, password: str = None, email: str = None, full_name: str = None):
    try:
        user = update_user(username, password, email, full_name)
        return {"msg": "User updated successfully", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/disable-user")
async def disable_user_account(username: str):
    try:
        user = disable_user(username)
        return {"msg": "User disabled successfully", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
