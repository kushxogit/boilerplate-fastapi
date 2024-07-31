from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from ..store.account_schemas import UserCreate, UserResponse
from ..account_service import register_new_user, AccountService
from ..internal.account_reader import get_database

router = APIRouter()

class AccountDetails(BaseModel):
    email: str
    password: str

@router.post("/accounts", response_model=UserResponse)
async def signup(user: UserCreate, db=Depends(get_database)):
    new_user = await register_new_user(user)
    if new_user is None:
        raise HTTPException(status_code=400, detail="User already signed up. Please log in.")
    return {
        "status_code": status.HTTP_201_CREATED,
        "message": "User successfully created",
        "user": new_user
    }

@router.post("/login")
async def login(account_details: AccountDetails):
    account = await AccountService.login_user(account_details.email, account_details.password)
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    response_body = {
        "message": "login successful",
        "status_code": status.HTTP_200_OK,
        "account": account
    }
    return response_body