from fastapi import HTTPException,status,APIRouter
from ..account_service import AccountService
from pydantic import BaseModel
class AccountDetails(BaseModel):
    email: str
    password: str

router=APIRouter()

@router.post("/login")
async def login(account_details:AccountDetails):
    account = await AccountService.login_user(account_details.email, account_details.password)
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    response_body={
        "message":"login successful","status_code": status.HTTP_200_OK,"account":account
    }
    return response_body



  