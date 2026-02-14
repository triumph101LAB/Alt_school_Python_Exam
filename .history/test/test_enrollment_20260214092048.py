# tests/test_enrollments.py

def create_course_helper(client):
    """Helper to create a course and return its ID"""
    res = client.post("/courses/?user_id=1", json={
        "title": "Physics", "code": "PHY101", "description": "Forces", "instructor": "Newton"
    })
    return res.json()["id"]

def test_student_enroll_success(client):
    course_id = create_course_helper(client)
    
    # Student (ID 2) enrolls
    response = client.post(f"/enrollments/?user_id=2", json={
        "user_id": 2,a
        "course_id": course_id
    })
    assert response.status_code == 201
    assert response.json()["course_id"] == course_id

def test_student_deregister_own_course(client):
    # 1. Setup
    course_id = create_course_helper(client)
    enroll_res = client.post(f"/enrollments/?user_id=2", json={"user_id": 2, "course_id": course_id})
    enrollment_id = enroll_res.json()["id"]
    
    # 2. Deregister (As Student ID 2)
    response = client.delete(f"/enrollments/{enrollment_id}?user_id=2")
    assert response.status_code == 200

def test_student_cannot_deregister_others(client):
    # 1. Setup
    course_id = create_course_helper(client)
    # Student A (ID 2) enrolls. Enrollment ID will be 1.
    client.post(f"/enrollments/?user_id=2", json={"user_id": 2, "course_id": course_id})
    
    # 2. Create Student B (ID 3)
    client.post("/users/", json={"username": "student_b", "email": "b@b.com", "role": "student"})
    
    # 3. Student B tries to delete Student A's enrollment
    response = client.delete(f"/enrollments/1?user_id=3")
    assert response.status_code == 403 # Forbidden!

def test_admin_force_deregister(client):
    # 1. Setup
    course_id = create_course_helper(client)
    client.post(f"/enrollments/?user_id=2", json={"user_id": 2, "course_id": course_id})
    
    # 2. Admin (ID 1) force deletes Enrollment 1
    # Note: Use the /force/ path we created!
    response = client.delete(f"/enrollments/force/1?user_id=1")
    assert response.status_code == 200