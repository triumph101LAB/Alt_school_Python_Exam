from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository.enrollment import EnrollmentRepository
from repository.course import CourseRepository
from schemas.enrollment import EnrollmentResponse


class EnrollmentService:
    def __init__(self, db: Session):
        self.repo = EnrollmentRepository(db)
        self.course_repo = CourseRepository(db)

    def enroll(self, user_id: int, course_id: int) -> EnrollmentResponse:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        if not course.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot enroll in an inactive course"
            )
        if self.repo.get_by_user_and_course(user_id, course_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Already enrolled in this course"
            )
        if self.repo.count_by_course(course_id) >= course.capacity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Course is at full capacity"
            )
        enrollment = self.repo.create(user_id, course_id)
        return EnrollmentResponse.model_validate(enrollment)

    def deregister(self, enrollment_id: int, user_id: int) -> dict:
        enrollment = self.repo.get_by_id(enrollment_id)
        if not enrollment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Enrollment not found"
            )
        if enrollment.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only deregister from your own enrollments"
            )
        self.repo.delete(enrollment)
        return {"detail": "Successfully deregistered"}

    def get_all(self) -> list[EnrollmentResponse]:
        return [EnrollmentResponse.model_validate(e) for e in self.repo.get_all()]

    def get_by_course(self, course_id: int) -> list[EnrollmentResponse]:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        return [EnrollmentResponse.model_validate(e) for e in self.repo.get_by_course(course_id)]

    def get_by_student(self, user_id: int) -> list[EnrollmentResponse]:
        return [EnrollmentResponse.model_validate(e) for e in self.repo.get_by_user(user_id)]

    def admin_remove(self, enrollment_id: int) -> dict:
        enrollment = self.repo.get_by_id(enrollment_id)
        if not enrollment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Enrollment not found"
            )
        self.repo.delete(enrollment)
        return {"detail": "Student removed from course"}