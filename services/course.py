from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository.course import CourseRepository
from schemas.course import CourseResponse


class CourseService:
    def __init__(self, db: Session):
        self.repo = CourseRepository(db)

    def get_active_courses(self) -> list[CourseResponse]:
        courses = self.repo.get_all_active()
        return [CourseResponse.model_validate(c) for c in courses]

    def get_course(self, course_id: int) -> CourseResponse:
        course = self.repo.get_by_id(course_id)
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        return CourseResponse.model_validate(course)

    def create_course(self, title, code, capacity) -> CourseResponse:
        if self.repo.get_by_code(code):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Course with code '{code}' already exists"
            )
        course = self.repo.create(title, code, capacity)
        return CourseResponse.model_validate(course)

    def update_course(self, course_id: int, data: dict) -> CourseResponse:
        course = self.repo.get_by_id(course_id)
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        if "code" in data and data["code"] != course.code:
            if self.repo.get_by_code(data["code"]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Course with code '{data['code']}' already exists"
                )
        updated = self.repo.update(course, **data)
        return CourseResponse.model_validate(updated)

    def delete_course(self, course_id: int) -> dict:
        course = self.repo.get_by_id(course_id)
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        self.repo.delete(course)
        return {"detail": "Course deleted successfully"}