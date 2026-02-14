from schemas.enrollment import Enrollment, EnrollmentBase
from core.db import users, courses,enrollments
from schemas.user import User,UserRole

from fastapi import HTTPException, status
class EnrollmentService:
    @staticmethod
    def enroll_course(enroll_in: EnrollmentBase, student: User): # Added student param if you need it

        if enroll_in.user_id not in users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        if enroll_in.course_id not in courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )    
        for enrollment in enrollments.values():
            if enrollment.user_id == enroll_in.user_id and enrollment.course_id == enroll_in.course_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Student is already registered"
                )
        enrollment_id = 1
        if enrollments:
            enrollment_id = max(enrollments.keys()) + 1
        new_enrollment = Enrollment(
            id=enrollment_id,
            user_id=enroll_in.user_id,
            course_id=enroll_in.course_id
        )
        enrollments[enrollment_id] = new_enrollment  
        return new_enrollment
 
    @staticmethod

    def deregister(enrollment_id: int, user: User): 
        if enrollment_id not in enrollments:
             raise HTTPException(status_code=404, detail="Enrollment not found")
        
        enrollment = enrollments[enrollment_id]
        if user.role == UserRole.STUDENT and enrollment.user_id != user.id:
            raise HTTPException(
                status_code=403, 
                detail="You can only deregister from your own courses."
            )

        del enrollments[enrollment_id]
        return {"message": "Deregistered successfully"}  
    @staticmethod
    def get_all_enrollment():
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
                    