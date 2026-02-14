
from fastapi.testclient import TestClient
from main import app

def test_admin_can_create_course(client):

    response = client.post("/courses/?user_id=1", json={
        "title": "FastAPI 101",
        "code": "CS101",
      
    })
    assert response.status_code == 201
    assert response.json()["code"] == "CS101"

def test_student_cannot_create_course(client):
    # Student (ID 2) tries to create a course
    response = client.post("/courses/?user_id=2", json={
        "title": "Hacking",
        "code": "HACK101",
 
    })
    # Should fail with 403 Forbidden
    assert response.status_code == 403 

def test_public_can_get_courses(client):
    # 1. Admin creates a course first
    client.post("/courses/?user_id=1", json={
        "title": "Math", "code": "MATH"
    
    # 2. Anyone (no user_id needed) can fetch the list
    response = client.get("/courses/")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_delete_course(client):
    # 1. Create
    create_res = client.post("/courses/?user_id=1", json={
        "title": "To Delete", "code": "DEL", "description": "...", "instructor": "..."
    })
    course_id = create_res.json()["id"]
    
    # 2. Delete (As Admin)
    response = client.delete(f"/courses/{course_id}?user_id=1")
    assert response.status_code == 200 # or 204 depending on your service return