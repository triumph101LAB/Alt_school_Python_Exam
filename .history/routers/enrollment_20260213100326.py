from fastapi import APIRouter, status,Depends
from services.deps import is_student_user, is_admin_user
from schemas.enrollment import EnrollmentBase
from schemas.user import User
from services.enrollment import EnrollmentService

enrollment_router = APIRouter()


@enrollment_router.create("/", status_code = status.HTTP_201_CREATED)
def enroll_course(enrollIn:EnrollmentBase, student : User = Depends(is_student_user)):
    return EnrollmentService.
