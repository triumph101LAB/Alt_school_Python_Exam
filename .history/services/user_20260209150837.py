from schemas.user import UserBase, User,UserRole
from core.db import users

from fastapi import HTTPException, status
class UserService:
    
    @staticmethod
    def create_user(user_create:UserBase):
        user_id = len(users) + 1
        
        user = User(
            id = user_id,
            username = user_create.username,
            email=user_create.email,
            role=user_create.role
        )
        
        users[user_id]  = user
        
        if (len(user.username) == 0):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="user name must not be be empty"
            )
        if ("@gmail.com" not in user.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="email most contain @gmail.com"
            )
        if (user.role != UserRole.ADMIN or user.role UserRole.STUDENT )):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Users role most Either be student or admin"
            )    
            
        return user
    
    @staticmethod
    def get_users(users):
        return users
    
    @staticmethod
    def get_user(user_id:int):
        return users.get(user_id)   