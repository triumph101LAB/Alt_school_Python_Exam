from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.db import get_db
from services.user import UserService
from services.deps import get_current_user
from schemas.user import UserBase, UserResponse

user_router = APIRouter()


@user_router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(data: UserBase, db: Session = Depends(get_db)):
    return UserService(db).register(
        name=data.name,
        email=data.email,
        password=data.password,
        role=data.role
    )


@user_router.post("/login")
def login(data: UserBase, db: Session = Depends(get_db)):
    return UserService(db).login(
        email=data.email,
        password=data.password
    )


@user_router.get("/me", response_model=UserResponse)
def get_profile(current_user=Depends(get_current_user)):
    return UserService(None).get_profile(current_user)