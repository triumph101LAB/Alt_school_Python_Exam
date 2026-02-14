from fastapi.testclient import TestClient
from main import app

client
# --- Test 1: Student Enrolls in a Course ---
def test_student_enroll_course(client, test_course_id):
    # The 'test_course_id' argument automatically ensures a course exists!
    
    payload = {
        "user_id": 2,       
        "course_id": test_course_id
    }
    
    response = client.post("/enrollments/?user_id=2", json=payload)
    
    assert response.status_code == 201
    data = response.json()
    assert data["course_id"] == test_course_id
    assert data["user_id"] == 2

def test_get_course_enrollments(client, test_course_id):
   
    client.post("/enrollments/?user_id=2", json={"user_id": 2, "course_id": test_course_id})

    response = client.get(f"/enrollments/course/{test_course_id}?user_id=1")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["course_id"] == test_course_id

# --- Test 3: Get Student's Own Enrollments ---
def test_get_student_enrollments(client, test_course_id):
    # 1. Setup
    client.post("/enrollments/?user_id=2", json={"user_id": 2, "course_id": test_course_id})
    
    # 2. Action: Student checks their own list
    response = client.get(f"/enrollments/student/2?user_id=2")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1

# --- Test 4: Student Deregisters (Self) ---
def test_student_deregister_self(client, test_course_id):
    # 1. Setup
    enroll_res = client.post("/enrollments/?user_id=2", json={"user_id": 2, "course_id": test_course_id})
    enrollment_id = enroll_res.json()["id"]
    
    # 2. Action
    response = client.delete(f"/enrollments/{enrollment_id}?user_id=2")
    assert response.status_code == 200
    
    # 3. Verify
    check = client.get(f"/enrollments/student/2?user_id=2")
    assert check.json() == []

# --- Test 5: Admin Force Deregister ---
def test_admin_force_deregister(client, test_course_id):
    # 1. Setup
    enroll_res = client.post("/enrollments/?user_id=2", json={"user_id": 2, "course_id": test_course_id})
    enrollment_id = enroll_res.json()["id"]
    
    # 2. Action
    response = client.delete(f"/enrollments/force/{enrollment_id}?user_id=1")
    assert response.status_code == 200