from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.db import get_db
from services.enrollment import EnrollmentService
from services.deps import require_admin, require_student
from schemas.enrollment import EnrollmentCreate, EnrollmentResponse

enrollment_router = APIRouter()


@enrollment_router.get("/me", response_model=list[EnrollmentResponse])
def my_enrollments(db: Session = Depends(get_db), current_user=Depends(require_student)):
    return EnrollmentService(db).get_by_student(current_user.id)


@enrollment_router.get("/", response_model=list[EnrollmentResponse])
def get_all_enrollments(db: Session = Depends(get_db), _=Depends(require_admin)):
    return EnrollmentService(db).get_all()


@enrollment_router.get("/course/{course_id}", response_model=list[EnrollmentResponse])
def get_course_enrollments(course_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    return EnrollmentService(db).get_by_course(course_id)


@enrollment_router.post("/", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll(data: EnrollmentCreate, db: Session = Depends(get_db), current_user=Depends(require_student)):
    return EnrollmentService(db).enroll(current_user.id, data.course_id)


@enrollment_router.delete("/admin/{enrollment_id}")
def admin_remove(enrollment_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    return EnrollmentService(db).admin_remove(enrollment_id)


@enrollment_router.delete("/{enrollment_id}")
def deregister(enrollment_id: int, db: Session = Depends(get_db), current_user=Depends(require_student)):
    return EnrollmentService(db).deregister(enrollment_id, current_user.id)