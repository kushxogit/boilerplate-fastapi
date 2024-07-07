from fastapi import APIRouter, Depends, HTTPException
from src.routes.auth.controller import get_current_active_user
from src.util.db_dependency import get_db
from .controller import *
from .schemas import *
from .models import User  # Ensure this is the Beanie model

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

# ---------------------------
# ----- Crud-Operations -----
# ---------------------------
@router.get("/")
async def get_all_users(user: User = Depends(get_current_active_user),
                        db = Depends(get_db)):  # Adjusted for Beanie
    """
    # Get a list of all users

    **Access:**
    - Admins get a list of all users.
    - Users with lower rights get a list with only the enabled users.
    """
    if user.super_admin:
        return await get_users_admin(db=db)  # Adjusted for async
    else:
        return await get_users(db=db)  # Adjusted for async

@router.get("/{user_id}")
async def get_user_by_id(user_id: str, db = Depends(get_db)):  # Adjusted for Beanie, using string IDs
    user = await User.find_one(User.id == user_id)  # Adjusted for Beanie query
    if not user:
        raise HTTPException(
            status_code=404,
            detail="There is no user with this id."
        )
    return user