def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    assert response.status_code == 201


def test_duplicate_registration(client):
    payload = {
        "email": "dev@example.com",
        "password": "StrongPass123!",
    }

    first_response = client.post(
        "/auth/register",
        json=payload,
    )

    second_response = client.post(
        "/auth/register",
        json=payload,
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 409


def test_login_with_valid_credentials(client):
    client.post(
        "/auth/register",
        json={
            "email": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_with_wrong_password(client):
    client.post(
        "/auth/register",
        json={
            "email": "dev@example.com",
            "password": "StrongPass123!",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "dev@example.com",
            "password": "WrongPass123!",
        },
    )

    assert response.status_code == 401


def test_current_user_requires_token(client):
    response = client.get("/auth/me")

    assert response.status_code == 401


def test_current_user_with_valid_token(client):
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

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200
    assert response.json()["email"] == "dev@example.com"
