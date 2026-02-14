from pydantic import BaseModel

class CourseBase(BaseModel): 
    title:str
    code:str.sp
    
class Course(CourseBase):
    id:int
        