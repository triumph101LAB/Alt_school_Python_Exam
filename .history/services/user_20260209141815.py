from schemas.user import UserBase, User
from core.db import users
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
        
        if
        return user
    
    @staticmethod
    def get_users(users):
        return users
    
    @staticmethod
    def get_user(user_id:int):
        return users.get(user_id)   