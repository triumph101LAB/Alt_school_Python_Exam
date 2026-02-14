from fastapi import APIRouter status, HTTPException
from schemas.course import CourseBase
from services.course import CourseService

course_router = API()

@course_router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(course:CourseBase):
    return CourseService.create_course(course)



