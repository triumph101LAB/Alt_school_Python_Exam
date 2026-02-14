from pydantic import BaseModel


class EnrollmentBase(BaseModel):
    user_id:int
    course_id:int
    
class Enrollment(EnrollmentBase):
    id:int