from .auth_reader import fake_users_db, hash_password
from auth_types import UserInDB

def create_user(username: str, password: str, email: str, full_name: str) -> UserInDB:
    if username in fake_users_db:
        raise ValueError("User already exists")
    
    hashed_password = hash_password(password)
    new_user = UserInDB(
        username=username,
        email=email,
        full_name=full_name,
        hashed_password=hashed_password,
        disabled=False
    )
    
    fake_users_db[username] = new_user.dict()
    return new_user

def update_user(username: str, password: str = None, email: str = None, full_name: str = None) -> UserInDB:
    user = fake_users_db.get(username)
    if not user:
        raise ValueError("User not found")
    
    if password:
        user['hashed_password'] = hash_password(password)
    if email:
        user['email'] = email
    if full_name:
        user['full_name'] = full_name
    
    fake_users_db[username] = user
    return UserInDB(**user)

def disable_user(username: str) -> UserInDB:
    user = fake_users_db.get(username)
    if not user:
        raise ValueError("User not found")
    
    user['disabled'] = True
    fake_users_db[username] = user
    return UserInDB(**user)
