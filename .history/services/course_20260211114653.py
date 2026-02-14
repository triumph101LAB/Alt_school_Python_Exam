from typing import Optional
from fastapi import HTTPException
from schemas.course import CourseBase,Course

class CourseService:
    @staticmethod
    def create_course(course_in:CourseBase):
        