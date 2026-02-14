from fastapi import FastAPI
from routers.course import course_router
from routers.enrollment import enrollment_router
from routers.user import user_router
app = FastAPI(
    title="Course Enrollmenet System",
    description="A RESTAPI for managing students, courses and enrollments",
    version="1.0.0"
)
app.in

@app.get("/")
def root():
    return {"message":"Hello there, Welcom to the Course Enrollment API"}