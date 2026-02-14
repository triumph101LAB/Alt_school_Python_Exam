from fastapi import APIRouter, status
from services.deps import is_student_user, is_admin_user
from schemas.enrollment import EnrollmentBase
from services.enrollment import EnrollmentService

enrollment_router = APIRouter()


@enrollment_router.create("/", status_code = status.HTTP_201_CREATED)
