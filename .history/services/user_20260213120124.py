from schemas.user import UserBase, User,UserRole
from core.db import users

from fastapi import HTTPException, status
class UserService:
    
 
    @staticmethod
    def get_users():
        return users
    
    @staticmethod
    def get_user(user_id:int):
        return users.get(user_id)   