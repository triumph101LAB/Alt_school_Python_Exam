from schemas.user import UserBase, User
from cor
class UserService:
    
    @staticmethod
    def create_user(user_create:UserBase):
        user_id = len(users) + 1