# from fastapi import FastAPI
# from routers.course import course_router
# from routers.enrollment import enrollment_router
# from routers.user import user_router
# app = FastAPI(
#     title="Course Enrollmenet System",
#     description="A RESTAPI for managing students, courses and enrollments",
#     version="1.0.0"
# )
# app.include_router(user_router, prefix="/users", tags=["Users"])
# app.include_router(course_router,prefix="/courses", tags=["Courses"])
# app.include_router(enrollment_router, prefix="/enrollments", tags=["Enrollments"])

# @app.get("/")
# def root():
#     return {"message":"Hello there, Welcome to the Course Enrollment API"}


from fastapi import FastAPI
from core.db import init_db
from routers.user import user_router
from routers.course import course_router
from routers.enrollment import enrollment_router

app = FastAPI(
    title="Course Enrollment System",
    description="A secure role-based API for managing courses and enrollments",
    version="2.0.0"
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(course_router, prefix="/courses", tags=["Courses"])
app.include_router(enrollment_router, prefix="/enrollments", tags=["Enrollments"])

@app.get("/", tags=["Health"])
def root():
    return {"message": "Course Enrollment API is running"}