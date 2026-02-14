from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import enrollment
from core.db import users, courses
from fastapi import HTTPException, status
class EnrollmentService:
    
    @staticmethod
    def enroll_course(enroll_in:EnrollmentBase):
        user_id = enroll_in.user_id
        course_id = enroll_in.course_id
        
        if 
        