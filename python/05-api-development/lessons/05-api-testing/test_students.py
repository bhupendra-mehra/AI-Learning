def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == ("Student Management API is running")


def test_list_students(client):
    response = client.get("/students")

    assert response.status_code == 200
    assert response.json() == []


def test_create_student_requires_authentication(client):
    response = client.post(
        "/students",
        json={
            "name": "Priya Patel",
            "email": "priya@example.com",
            "age": 24,
        },
    )

    assert response.status_code == 401


def test_create_student_with_authentication(client):
    client.post(
        "/auth/register",
        json={
            "email": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.post(
        "/students",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "name": "Priya Patel",
            "email": "priya@example.com",
            "age": 24,
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Priya Patel"


def test_invalid_student_data(client):
    # Register a user.
    client.post(
        "/auth/register",
        json={
            "email": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    # Log in to get an access token.
    login_response = client.post(
        "/auth/login",
        data={
            "username": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    token = login_response.json()["access_token"]

    # Submit invalid student data with valid authentication.
    response = client.post(
        "/students",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "name": "P",
            "email": "invalid-email",
            "age": 24,
        },
    )

    assert response.status_code == 422
