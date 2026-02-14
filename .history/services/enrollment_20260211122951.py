from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import enrollment
from core.db import users, courses
from schemas.user import UserRole
from fastapi import HTTPException, status
class EnrollmentService:
    
    @staticmethod
    def enroll_course(enroll_in:EnrollmentBase):
        user_id = enroll_in.user_id
        course_id = enroll_in.course_id
        
        if user_id not in users:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        if course_id not in courses:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="Course is not found"
            )    
        