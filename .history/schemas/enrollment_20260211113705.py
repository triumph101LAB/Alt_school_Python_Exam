from pydantic import BaseModel
from schemas.user import User
from schemas.course import Course
class Enrollment(BaseModel):
    id:int
    user_id:
    course_id:int