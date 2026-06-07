from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from core.db import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")

class CourseRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, course_id: int):
        return self.db.query(Course).filter(Course.id == course_id).first()

    def get_by_code(self, code: str):
        return self.db.query(Course).filter(Course.code == code).first()

    def get_all_active(self):
        return self.db.query(Course).filter(Course.is_active == True).all()

    def create(self, title, code, capacity):
        course = Course(title=title, code=code, capacity=capacity)
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def update(self, course, **kwargs):
        for key, value in kwargs.items():
            setattr(course, key, value)
        self.db.commit()
        self.db.refresh(course)
        return course

    def delete(self, course):
        self.db.delete(course)
        self.db.commit()