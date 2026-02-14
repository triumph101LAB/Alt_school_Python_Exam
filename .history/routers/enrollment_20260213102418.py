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
def get_enrollment(admin : User =  Depends(is_admin_user)):
    return EnrollmentService.get_all_enrollment(enrollments)

@enrollment_router.delete("/{EnrollId}")
def deregitser_course(enrollmentId:int, student: User = Depends(is_student_user)):
    return EnrollmentService.deregister(enrollmentId)

@enrollment_router.get("/{Userid}")
def get_enrolled_courses(student_id:int, student:User = Depends(is_student_user)):
    return EnrollmentService.student_enrollment(student_id)

@enrollment_router.get("/{courseId}")
def get