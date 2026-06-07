from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.db import Base

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    student = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class EnrollmentRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, enrollment_id: int):
        return self.db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()

    def get_all(self):
        return self.db.query(Enrollment).all()

    def get_by_course(self, course_id: int):
        return self.db.query(Enrollment).filter(Enrollment.course_id == course_id).all()

    def get_by_user(self, user_id: int):
        return self.db.query(Enrollment).filter(Enrollment.user_id == user_id).all()

    def get_by_user_and_course(self, user_id: int, course_id: int):
        return self.db.query(Enrollment).filter(
            Enrollment.user_id == user_id,
            Enrollment.course_id == course_id
        ).first()

    def count_by_course(self, course_id: int):
        return self.db.query(Enrollment).filter(Enrollment.course_id == course_id).count()

    def create(self, user_id: int, course_id: int):
        enrollment = Enrollment(user_id=user_id, course_id=course_id)
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)
        return enrollment

    def delete(self, enrollment):
        self.db.delete(enrollment)
        self.db.commit()