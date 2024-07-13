from fastapi import HTTPException,status,APIRouter
from ..account_service import AccountService
from pydantic import BaseModel
class AccountDetails(BaseModel):
    username: str
    password: str

router=APIRouter()

@router.post("/login")
async def login(account_details:AccountDetails):
    account = await AccountService.login_user(account_details.username, account_details.password)
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return {"message":"login successful"}



    # return {"access_token": token, "token_type": "bearer"}

# @router.get("./verify_token/{token}")
# async def verify(token:str):
#     payload=await AccountService.verify_user_token(token)
#     if not payload:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")
#     return{"message":"Valid Token","data":payload}