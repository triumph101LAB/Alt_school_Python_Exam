from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# --- PUBLIC ACCESS ---
def test_get_courses_public():
    response = client.get("/courses/")
    assert response.status_code == 200

# --- ADMIN ACTIONS (Should Succeed) ---
def test_create_course_as_admin():
    # User 1 is Admin
    response = client.post("/courses/?user_id=1", json={
        "title": "Advanced Python",
        "code": "PY300",
        "description": "Deep dive",
        "instructor": "Guido"
    })
    assert response.status_code == 201
    assert response.json()["code"] == "PY300"

def test_delete_course_as_admin():
    # First, create a course to delete
    create_res = client.post("/courses/?user_id=1", json={
        "title": "Temp Course", "code": "TMP101", "description": "Delete me", "instructor": "None"
    })
    course_id = create_res.json()["id"]

    # Now delete it
    response = client.delete(f"/courses/{course_id}?user_id=1")
    assert response.status_code == 200

# --- STUDENT ACTIONS (Should Fail - 403 Forbidden) ---
def test_create_course_as_student_fails():
    # User 2 is Student
    response = client.post("/courses/?user_id=2", json={
        "title": "Hacker Course",
        "code": "HACK101",
        "description": "I should not be able to make this",
        "instructor": "Me"
    })
    assert response.status_code == 403 # Forbidden