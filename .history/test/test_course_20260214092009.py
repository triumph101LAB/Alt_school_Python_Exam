# tests/test_courses.py

def test_admin_can_create_course(client):
    # User 1 is Admin
    response = client.post("/courses/?user_id=1", json={
        "title": "FastAPI 101",
        "code": "CS101",
        "description": "Intro to APIs",
        "instructor": "Prof. Smith"
    })
    assert response.status_code == 201
    assert response.json()["code"] == "CS101"

def test_student_cannot_create_course(client):
    # User 2 is Student
    response = client.post("/courses/?user_id=2", json={
        "title": "Hacking",
        "code": "HACK101",
  
    })
    assert response.status_code == 403 # Forbidden

def test_public_can_get_courses(client):
    # Create a course first (as admin)
    client.post("/courses/?user_id=1", json={
        "title": "Math", "code": "MATH", "description": "1+1", "instructor": "A"
    })
    
    # Get list (No user_id needed)
    response = client.get("/courses/")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_delete_course_admin(client):
    # 1. Create
    create_res = client.post("/courses/?user_id=1", json={
        "title": "To Delete", "code": "DEL", "description": "...", "instructor": "..."
    })
    course_id = create_res.json()["id"]
    
    # 2. Delete (As Admin)
    response = client.delete(f"/courses/{course_id}?user_id=1")
    assert response.status_code == 200