from schemas.enrollment import Enrollment, EnrollmentBase

from core.db import users, courses,enrollments
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
        
        user = users[user_id]
        
        if user.role != UserRole.STUDENT:
            raise HTTPException(
                status_code= status.HTTP_403_FORBIDDEN,
                detail="Only students can enroll a course"
            )
            
        for enrollment in enrollments.values():
            if en   