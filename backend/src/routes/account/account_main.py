
from fastapi import APIRouter
from .rest_api.account_controller import signup


router = APIRouter(prefix="/accounts", tags=["Account"])

router.post("/",response_model=dict)(signup)


