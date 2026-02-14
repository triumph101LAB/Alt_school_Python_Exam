from pydantic import BaseModel
from schemas.user import User
from schemas.course import Course
class EnrollmentBase(BaseModel):
    id:int
    user_id:User
    course_id:Course
    
    clas