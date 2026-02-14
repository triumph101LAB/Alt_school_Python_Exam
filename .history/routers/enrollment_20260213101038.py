from fastapi import APIRouter, status,Depends
from services.deps import is_student_user, is_admin_user
from schemas.enrollment import EnrollmentBase
from schemas.user import User
from core.db import enrollments
from services.enrollment import EnrollmentService

enrollment_router = APIRouter()


@enrollment_router.create("/", status_code = status.HTTP_201_CREATED)
def enroll_course(enrollIn:EnrollmentBase, student : User = Depends(is_student_user)):
    return EnrollmentService.enroll_course(enrollIn)

@enrollment_router.get("/enrollments")
def get_enrollment():
    return EnrollmentService.get_all_enrollment(enrollments)

@enrollment_router.delete("/{userId}")
def deregitser_course(enrollmentId:Id):