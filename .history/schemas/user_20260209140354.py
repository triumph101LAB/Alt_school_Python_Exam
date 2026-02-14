from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "adminstrator"
    USER = "student"
    
class UserBase(BaseModel):
    username: str
    email: str
    role: UserRole 

class User       