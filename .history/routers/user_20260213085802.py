from typing import Optional
from fastapi import APIRouter, status, HTTPException, Depends
from schemas.user import UserBase
from services.user import UserService


user_router = APIRouter()

#create user

@user_router.post("/")
def create_user()