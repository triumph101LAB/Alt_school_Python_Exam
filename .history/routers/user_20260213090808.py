from typing import Optional
from fastapi import APIRouter, status, HTTPException, Depends
from schemas.user import UserBase
from services.user import UserService
from core.db import users


user_router = APIRouter()

#create user

@user_router.post("/")
def create_user(user_data:UserBase):
    return UserService.create_user(user_data)

@user_router.get("/allusers")
def get_users():
    return UserService.get_users()

@user_router.get("/user_id")
def get_user_byid(userid:int):
    return UserService.get_user(userid)

