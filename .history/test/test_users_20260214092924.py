from fastapi.testclient import TestClient
from main import app

def test_create_user(client):
    response = client.post("/users/", json={
        "username": "new_student",
        "email": "new@test.com",
        "role": "student"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "new_student"

    assert data["id"] == 3 

def test_get_all_users(client):
    response = client.get("/users/")
    assert response.status_code == 200

    assert len(response.json()) >= 2 

def test_get_user_by_id(client):

    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "admin_user"