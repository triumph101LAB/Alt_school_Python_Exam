# tests/test_users.py

def test_create_user(client):
    response = client.post("/users/", json={
        "username": "new_student",
        "email": "new@test.com",
        "role": "student"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "new_student"
    assert data["id"] == 3 # Should be 3 (since 1 & 2 are seeded)

def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 2 # Admin + Student

def test_get_user_by_id(client):
    # Get the seeded Admin (ID 1)
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "admin_user"

def test_get_non_existent_user(client):
    response = client.get("/users/999")
    assert response.status_code == 404