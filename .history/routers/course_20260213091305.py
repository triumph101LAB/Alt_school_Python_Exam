from fastapi import FastAPI, status, HTTPException
from schemas.course import CourseBase
from services.course import CourseService

course_router = FastAPI()

@course_router.post("/", status_code=status.HTTP_201_CREATED)
def create_course



