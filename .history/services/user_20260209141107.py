from schemas.user import UserBase, User

class UserService:
    
    @staticmethod
    def create_user(user_create:UserBase):
        