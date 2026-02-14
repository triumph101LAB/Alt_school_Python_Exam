from typing import Optional
from fastapi import HTTPException
from schemas.course import CourseBase,Course
from core.db import courses as courses_db
class CourseService:
    @staticmethod
    def create_course(course_in:CourseBase):
        course_dict: dict = course_in.model_dump()
        course_id = len(courses_db) +1
        new_course : Course = Course(
            id=course_id,
            **course_dict 
        )
        
        courses_db[course_id] =new_course
        return new_course
    
    @staticmethod
    def get_course(courses_db):
        return courses_db
    @staticmethod
    def get_courseid()
            
        