from fastapi import APIRouter, status,Depends
from schemas.course import CourseBase
# from core.db import courses
from services.course import CourseService
from schemas.user import User
from services.deps import is_admin_user
course_router = APIRouter()

@course_router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(course:CourseBase, admin: User = Depends(is_admin_user)):
    return CourseService.create_course(course)

@course_router.patch("/{course_id}")
def update_course(course_id:int, course:CourseBase,admin: User = Depends(is_admin_user)):
    return CourseService.update_course(course_id,course)

@course_router.delete("/{course_id}")
def delete_course(course_id:int, admin: User = Depends(is_admin_user)):
    return CourseService.delete_course(course_id)
        
@course_router.get("/")
def get_courses():
    return CourseService.get_courses()

@course_router.get("/{course_id}")
def get_course(course_id:int):
    return CourseService.get_course(course_id)



