from datetime import datetime, timedelta
from beanie import Document
from pydantic import BaseModel

from src.routes.users.models import User

class PasswordResetToken(Document):
    user_id: int
    reset_token: str
    expires: datetime = datetime.now() + timedelta(hours=1)