from pydantic import BaseModel
from schemas import user
class Enrollment(BaseModel):
    id:int
    user_id:int
    course_id:int