from typing import Optional
from fastapi import HTTPException
from schemas.course import CourseBase,Course
fr
class CourseService:
    @staticmethod
    def create_course(course_in:CourseBase):
        