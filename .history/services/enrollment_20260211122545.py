from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import enrollment
from core.db import users, courses

class EnrollmentService:
    
    @staticmethod
    def enroll_course(enroll_in:EnrollmentBase):
        user