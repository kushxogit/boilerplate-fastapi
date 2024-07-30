from fastapi import APIRouter, Depends, HTTPException
from ..store.account_schemas import UserCreate, UserResponse
from ..account_service import register_new_user
from ..internal.account_reader import get_database

router = APIRouter()

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
