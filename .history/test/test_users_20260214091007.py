from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Note: Our conftest.py already seeds Admin(1) and Student(2)

def test_create_new_user():
    response = client.post("/users/", json={
        "username": "test_student",
        "email": "test@student.com",
        "role": "student"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "test_student"
    assert "id" in data

def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) >= 2 # Should have at least the seeded users

def test_get_user_by_id_success():
    # ID 1 is the Admin created in conftest
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["role"] == "admin"

def test_get_user_not_found():
    response = client.get("/users/9999")
    assert response.status_code == 404