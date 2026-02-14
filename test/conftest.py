
import pytest
from fastapi.testclient import TestClient
from main import app
from core.db import users, courses, enrollments
from schemas.user import User, UserRole, UserBase

@pytest.fixture
def client():

    users.clear()
    courses.clear()
    enrollments.clear()
    
    # 2. Seed Admin (ID 1)
    users[1] = User(id=1, username="admin", email="admin@test.com", role=UserRole.ADMIN)
    
    # 3. Seed Student (ID 2)
    users[2] = User(id=2, username="student", email="student@test.com", role=UserRole.STUDENT)
    
    with TestClient(app) as c:
        yield c

@pytest.fixture
def test_course_id(client):
    # Create the course as Admin (ID 1)
    response = client.post("/courses/?user_id=1", json={
        "title": "Test Course", 
        "code": "TST101"
    })
    return response.json()["id"]