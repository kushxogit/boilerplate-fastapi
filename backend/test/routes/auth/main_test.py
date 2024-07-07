import pytest
from backend.src.routes.auth.store.auth_models import PasswordResetToken
from src.routes.users.models import User
import asyncio

@pytest.fixture
async def regular_user():
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        asyncio.set_event_loop(asyncio.new_event_loop())
    user = User(
        first_name="Kim",
        last_name="Wexler",
        email="kim.wexler@wexler-mcgill.law",
        password="hashed_password",
        super_admin=False,
        disabled=False
    )
    await user.insert()  # Use Beanie's insert method
    yield user
    await user.delete()  # Use Beanie's delete method

def test_post_reset_password(db, client, regular_user):
    url = "/auth/reset-password"

    # User does not exist
    response = client.post(url=url, json={'email': 'tuco@salamanca.biz'})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

    # User does exist, check if the mail has been sent
    response = client.post(url=url, json={'email': 'kim.wexler@wexler-mcgill.law'})
    assert regular_user.id == db.query(PasswordResetToken).filter(PasswordResetToken.user_id == regular_user.id).count()
    assert response.status_code == 200

# TODO: Your unittests for /auth here