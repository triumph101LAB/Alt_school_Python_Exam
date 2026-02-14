from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "adminstrator"
    STUDENT = "student"
    
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole 

class User(UserBase):
    id:int       