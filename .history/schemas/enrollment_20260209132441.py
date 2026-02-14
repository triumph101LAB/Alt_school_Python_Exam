from pydantic import BaseModel

class Enrollment(BaseModel):
    id:int
    user_id:int
    course_id:int