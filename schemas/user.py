from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "administrator"
    STUDENT = "student"
    
class UserBase(BaseModel):
    name: str
    password:str
    email: EmailStr
    role: UserRole = UserRole.STUDENT 

class UserResponse(BaseModel):
    id:int
    name:str
    role:UserRole
    is_active:bool
    
    model_config = {"from_attributes":True}
              