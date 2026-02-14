from fastapi import APIRouter, status
from schemas.course import CourseBase
from services.course import CourseService
from schemas.user import
course_router = APIRouter()

@course_router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(course:CourseBase, admin: User):
    return CourseService.create_course(course)



