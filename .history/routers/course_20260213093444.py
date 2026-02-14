from fastapi import APIRouter, status,Depends
from schemas.course import CourseBase
from services.course import CourseService
from schemas.user import User
from services.deps import is_admint_user
course_router = APIRouter()

@course_router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(course:CourseBase, admin: User = Depends(is_admint_user)):
    return CourseService.create_course(course)

@course_router.get("")


