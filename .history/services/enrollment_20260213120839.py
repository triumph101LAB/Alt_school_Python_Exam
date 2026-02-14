from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import users, courses,enrollments
from schemas.user import User

from fastapi import HTTPException, status
class EnrollmentService:
    
    @staticmethod 
    def deregister(enrollment_id:int):
        # enrollment_to_delete = enrollments[enrollment_id]
        if enrollment_id not in enrollments:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="Enrollment not found"   
            )                
        del enrollments[enrollment_id]
        return{"details":"Successfully deregistered"}   
    @staticmethod
    def get_all_enrollment(enrollments,):
        return enrollments
    @staticmethod
    def get_course_enrollment(course_id:int):
        if course_id not in courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "Course not found"
            ) 
        matching_enrollment = []
        for enrollment in enrollments.values():
           if (enrollment.course_id == course_id):
               matching_enrollment.append(enrollment)
        return matching_enrollment       
               
    @staticmethod
    def student_enrollment(user_id:int):
        if user_id not in users:
            raise HTTPException(
              status_code= status.HTTP_404_NOT_FOUND,
              detail = "User not found"  
            )
        courses_enrolled = []
        for enrollment in enrollments.values():
            if(enrollment.user_id == user_id):
                courses_enrolled.append(enrollment)
        return courses_enrolled    
                    