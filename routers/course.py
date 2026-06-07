from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.db import get_db
from services.course import CourseService
from services.deps import require_admin
from schemas.course import CourseCreate, CourseUpdate, CourseResponse

course_router = APIRouter()


@course_router.get("/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return CourseService(db).get_active_courses()


@course_router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return CourseService(db).get_course(course_id)


@course_router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(data: CourseCreate, db: Session = Depends(get_db), _=Depends(require_admin)):
    return CourseService(db).create_course(
        title=data.title,
        code=data.code,
        capacity=data.capacity
    )


@course_router.patch("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, data: CourseUpdate, db: Session = Depends(get_db), _=Depends(require_admin)):
    return CourseService(db).update_course(
        course_id=course_id,
        data=data.model_dump(exclude_unset=True)
    )


@course_router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    return CourseService(db).delete_course(course_id)