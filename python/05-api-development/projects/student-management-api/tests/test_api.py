def register_and_login(client, email="developer@example.com", password="StrongPass123"):
    response = client.post(
        "/auth/register", json={"email": email, "password": password}
    )
    assert response.status_code == 201
    login_response = client.post(
        "/auth/login", data={"username": email, "password": password}
    )
    assert login_response.status_code == 200
    return login_response.json()["access_token"]


def test_home_and_health(client):
    assert client.get("/").status_code == 200
    assert client.get("/health").json() == {"status": "healthy"}


def test_register_login_and_current_user(client):
    token = register_and_login(client)
    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "developer@example.com"


def test_duplicate_registration_returns_conflict(client):
    payload = {"email": "developer@example.com", "password": "StrongPass123"}
    assert client.post("/auth/register", json=payload).status_code == 201
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 409


def test_login_rejects_wrong_password(client):
    client.post(
        "/auth/register",
        json={"email": "developer@example.com", "password": "StrongPass123"},
    )
    response = client.post(
        "/auth/login",
        data={"username": "developer@example.com", "password": "wrong-password"},
    )
    assert response.status_code == 401


def test_create_student_requires_authentication(client):
    response = client.post(
        "/students", json={"name": "Asha Mehra", "email": "asha@example.com", "age": 21}
    )
    assert response.status_code == 401


def test_student_crud_and_filtering(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": "Asha Mehra", "email": "asha@example.com", "age": 21}

    created = client.post("/students", json=payload, headers=headers)
    assert created.status_code == 201
    student = created.json()
    assert student["name"] == payload["name"]

    assert len(client.get("/students").json()) == 1
    assert len(client.get("/students", params={"min_age": 25}).json()) == 0
    assert client.get(f"/students/{student['id']}").status_code == 200

    deleted = client.delete(f"/students/{student['id']}", headers=headers)
    assert deleted.status_code == 200
    assert client.get(f"/students/{student['id']}").status_code == 404


def test_duplicate_student_email_returns_conflict(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": "Asha Mehra", "email": "asha@example.com", "age": 21}
    assert client.post("/students", json=payload, headers=headers).status_code == 201
    duplicate = {**payload, "name": "Asha M."}
    assert client.post("/students", json=duplicate, headers=headers).status_code == 409


def test_invalid_student_payload_returns_validation_error(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/students",
        headers=headers,
        json={
            "name": "A",
            "email": "asha@example.com",
            "age": 0,
        },
    )

    assert response.status_code == 422


def test_put_replaces_student_fields(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    created = client.post(
        "/students",
        json={"name": "Asha Mehra", "email": "asha@example.com", "age": 21},
        headers=headers,
    )
    student_id = created.json()["id"]

    response = client.put(
        f"/students/{student_id}",
        json={"name": "Asha Sharma", "email": "asha.sharma@example.com", "age": 22},
        headers=headers,
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": student_id,
        "name": "Asha Sharma",
        "email": "asha.sharma@example.com",
        "age": 22,
    }


def test_put_requires_all_student_fields(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    created = client.post(
        "/students",
        json={"name": "Asha Mehra", "email": "asha@example.com", "age": 21},
        headers=headers,
    )
    student_id = created.json()["id"]

    response = client.put(
        f"/students/{student_id}",
        json={"name": "Asha Sharma"},
        headers=headers,
    )
    assert response.status_code == 422


def test_patch_updates_only_provided_fields(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    created = client.post(
        "/students",
        json={"name": "Asha Mehra", "email": "asha@example.com", "age": 21},
        headers=headers,
    )
    student_id = created.json()["id"]

    response = client.patch(
        f"/students/{student_id}",
        json={"age": 22},
        headers=headers,
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": student_id,
        "name": "Asha Mehra",
        "email": "asha@example.com",
        "age": 22,
    }


def test_patch_rejects_empty_payload(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    created = client.post(
        "/students",
        json={"name": "Asha Mehra", "email": "asha@example.com", "age": 21},
        headers=headers,
    )

    response = client.patch(
        f"/students/{created.json()['id']}", json={}, headers=headers
    )
    assert response.status_code == 422


def test_update_endpoints_require_authentication(client):
    payload = {"name": "Asha Mehra", "email": "asha@example.com", "age": 21}
    assert client.put("/students/1", json=payload).status_code == 401
    assert client.patch("/students/1", json={"age": 22}).status_code == 401


def test_put_and_patch_return_not_found_for_missing_student(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": "Asha Mehra", "email": "asha@example.com", "age": 21}

    assert client.put("/students/999", json=payload, headers=headers).status_code == 404
    assert (
        client.patch("/students/999", json={"age": 22}, headers=headers).status_code
        == 404
    )


def test_patch_rejects_null_values(client):
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    created = client.post(
        "/students",
        json={"name": "Asha Mehra", "email": "asha@example.com", "age": 21},
        headers=headers,
    )

    response = client.patch(
        f"/students/{created.json()['id']}", json={"age": None}, headers=headers
    )
    assert response.status_code == 422
