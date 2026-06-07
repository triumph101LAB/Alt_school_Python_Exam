from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository.user import UserRepository
from schemas.user import UserResponse
from jose import jwt
from datetime import datetime, timedelta, timezone
import bcrypt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(user_id: int, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "role": role, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(self, name, email, password, role) -> UserResponse:
        if self.repo.get_by_email(email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        user = self.repo.create(name, email, password, role)
        return UserResponse.model_validate(user)

    def login(self, email, password) -> dict:
        user = self.repo.get_by_email(email)
        if not user or not bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive"
            )
        token = create_access_token(user.id, user.role.value)
        return {"access_token": token, "token_type": "bearer"}

    def get_profile(self, user) -> UserResponse:
        return UserResponse.model_validate(user)