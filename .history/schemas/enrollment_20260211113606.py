from pydantic import BaseModel
from schemas import u
class Enrollment(BaseModel):
    id:int
    user_id:int
    course_id:int