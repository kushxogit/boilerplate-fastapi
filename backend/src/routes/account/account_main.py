from fastapi import APIRouter
from routes.account.rest_api.account_controller import login


router = APIRouter(prefix="/accounts", tags=["Account"])  

router.post("/login",response_model=dict)(login)


# need to import this is main.py