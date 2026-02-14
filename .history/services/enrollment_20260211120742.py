from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import enrollment

class EnrollmentService:
    
    @staticmethod
    def enroll_course(course)