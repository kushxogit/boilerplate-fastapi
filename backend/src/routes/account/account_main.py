from fastapi import APIRouter
from .rest_api.account_controller import signup
from .rest_api.account_controller import login


router = APIRouter(prefix="/accounts", tags=["Account"])

router.post("/",response_model=dict)(signup)

router.post("/login",response_model=dict)(login)
