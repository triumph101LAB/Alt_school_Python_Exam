from schemas.user import UserBase, User,UserRole
from core.db import users

from fastapi import HTTPException, status
class UserService:
    from schemas.user import UserBase, User
from core.db import users # <--- Your "Database"

class UserService:
    
    @staticmethod
    def create_user(user_data: UserBase):
        # 1. Generate a new ID
        # (If db is empty, start at 1. Otherwise, take the max ID + 1)
        new_id = 1
        if users:
            new_id = max(users.keys()) + 1
            
        new_user = User(
            id=new_id,
            **user_data.model_dump() # Unpacks name, email, role, etc.
        )
        

        users[new_id] = new_user 
        

        return new_user
 
    @staticmethod
    def get_users():
        return users
    
    @staticmethod
    def get_user(user_id:int):
        return users.get(user_id)   