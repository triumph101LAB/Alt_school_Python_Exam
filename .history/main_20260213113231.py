from fastapi import FastAPI
from routers.course import course_router
from routers.enrollment import enrollment_router
from routers.enrollment import use
app = FastAPI(
    title="Course Enrollmenet System",
    description="A RESTAPI for managing students, courses and enrollments",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message":"Hello world, this is my fist launch of my fast API project"}