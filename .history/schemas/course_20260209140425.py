from pydantic import BaseModel

class CourseBase(BaseModel):
    
    title:str
    code:str