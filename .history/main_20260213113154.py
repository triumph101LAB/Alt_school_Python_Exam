from fastapi import FastAPI
from routers.course import course_router
from routers.enrollment import enr
app = FastAPI(
    title="Course Enrollmenet System",
    description="A RESTAPI for managing students, courses and enrollments",
    
    
)

@app.get("/")
def root():
    return {"message":"Hello world, this is my fist launch of my fast API project"}