from fastapi import HTTPException, status
from schemas.user import UserRole, User
from services.user import UserService

def is_admint_user(user_id:int):
    user: User = User