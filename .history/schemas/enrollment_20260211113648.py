from pydantic import BaseModel
from schemas.user import User
from schemas.
class Enrollment(BaseModel):
    id:int
    user_id:int
    course_id:int