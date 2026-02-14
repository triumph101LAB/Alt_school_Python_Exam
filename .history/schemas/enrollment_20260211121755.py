from pydantic import BaseModel
from schemas.user import User
from schemas.course import Course

class EnrollmentBase(BaseModel):
    user_id:User.id
    course_id:Course
    
class Enrollment(EnrollmentBase):
    id:int