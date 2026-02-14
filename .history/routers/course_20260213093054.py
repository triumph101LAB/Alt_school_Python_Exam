from fastapi import APIRouter, status
from schemas.course import CourseBase
from services.course import CourseService

course_router = APIRouter()

@course_router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(course:CourseBase, admin):
    return CourseService.create_course(course)



