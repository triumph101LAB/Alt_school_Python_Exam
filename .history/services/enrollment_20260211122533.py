from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import enrollment
from core.db import users, 

class EnrollmentService:
    
    @staticmethod
    def enroll_course(enroll_in:EnrollmentBase):
        