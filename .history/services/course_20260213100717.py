from fastapi import HTTPException, status
from schemas.course import CourseBase, Course
from core.db import courses as courses_db
from schemas.user import UserRole,User

class CourseService:
    
    @staticmethod
    def create_course(course_in: CourseBase):
        for existing_course in courses_db.values():
            if existing_course.code == course_in.code:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Course code must be unique"
                )

        course_id = 1
        if courses_db:
            course_id = max(courses_db.keys()) + 1

        new_course = Course(
            id=course_id,
            **course_in.model_dump()
        )
        courses_db[course_id] = new_course
        return new_course
    
    @staticmethod
    def get_courses():

        return list(courses_db.values())
    
    @staticmethod
    def get_course(course_id: int):
        course = courses_db.get(course_id)
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        return course
    @staticmethod
    def update_course(course_id: int, course_update: CourseBase):
        # 1. Existence Check
        if course_id not in courses_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        current_course = courses_db[course_id]
        if course_update.code != current_course.code:
            for id, course in courses_db.items():
                if course.code == course_update.code and id != course_id:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Course code must be unique"
                    )
        current_course.title = course_update.title
        current_course.code = course_update.code
        return current_course
        
    @staticmethod
    def delete_course(course_id: int):
       
        del courses_db[course_id]
            return {"detail": "Course deleted successfully"}