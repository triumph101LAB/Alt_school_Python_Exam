from pydantic import BaseModel
from schemas.user import User
from schemas.course import Course

class EnrollmentBase(BaseModel):
    user_id:int
    course_id:Course
    
class Enrollment(EnrollmentBase):
    id:int