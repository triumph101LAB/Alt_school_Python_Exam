from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "adminstrator"
    STUDENT = "student"
    
class UserBase(BaseModel):
    username: str
    email: str
    role: UserRole 

class User(UserBase):
    id:int       