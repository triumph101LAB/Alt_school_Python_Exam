from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    ADMIN:"adminstrator"