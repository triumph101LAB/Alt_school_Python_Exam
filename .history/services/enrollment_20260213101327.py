from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import users, courses,enrollments
from schemas.user import User

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
        # user = users[user_id]
        for enrollment in enrollments.values():
            if enrollment.user_id == user_id and enrollment.course_id == course_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail = "Student is already registered"
                )
        enrollment_id = len(enrollments) +1
        
        new_enrollment = Enrollment(
            id = enrollment_id,
            user_id = user_id,
            course_id = course_id
        )
        enrollments[enrollment_id] = new_enrollment  
        return new_enrollment
    
    @staticmethod 
    def deregister(enrollment_id:int):
        # enrollment_to_delete = enrollments[enrollment_id]
        if enrollment_id not in enrollments:
            raise HTTPException(
             status_code= status.HTTP_404_NOT_FOUND   
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
                    