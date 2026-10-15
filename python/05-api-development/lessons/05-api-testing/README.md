# Lesson 05 — API Testing and Code Quality

## Goal

Learn how to test the Student Management API automatically, verify authentication, catch regressions, and maintain clean Python code.

## 1. What You Will Learn

- `pytest` fundamentals
- FastAPI `TestClient`
- Testing GET, POST, and DELETE endpoints
- Testing registration, login, and JWT authentication
- Database isolation during tests
- Test fixtures and dependency overrides
- Code quality using Ruff
- Test coverage

## 2. Project Structure

Create this folder:

```text
python/05-api-development/
└── lessons/
    ├── 04-database-auth/
    │   ├── main.py
    │   ├── database.py
    │   ├── models.py
    │   ├── schemas.py
    │   └── auth.py
    └── 05-api-testing/
        ├── README.md
        ├── conftest.py
        ├── test_students.py
        └── test_auth.py
```

The tests will validate the API you built in Lesson 04 without moving or duplicating its application code.

## 3. Install Testing Tools

From the `05-api-development` directory:

```bash
source .venv/bin/activate

pip install pytest httpx pytest-cov ruff
```

Update your existing dependency file:

```bash
pip freeze > requirements.txt
```

## 4. Configure the Test Environment

Create `conftest.py` inside `05-api-testing`.

```python
import os
import sys
from pathlib import Path

os.environ.setdefault(
    "SECRET_KEY",
    "test-only-secret-key-do-not-use-in-production",
)

API_DIR = Path(__file__).resolve().parents[1] / "04-database-auth"

sys.path.insert(0, str(API_DIR))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base, get_db
from main import app
import models  # Ensures all database models are registered.


@pytest.fixture
def client():
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(
        bind=test_engine,
        autoflush=False,
        autocommit=False,
    )

    Base.metadata.create_all(bind=test_engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)
    test_engine.dispose()
```

### Understand the important concepts

- `pytest.fixture`: Prepares resources that tests need.
- `TestClient`: Sends HTTP requests to FastAPI without starting a real server.
- `StaticPool`: Keeps the same in-memory SQLite database available across test connections.
- `dependency_overrides`: Replaces the application's normal database dependency with a test database.
- `create_all()` and `drop_all()`: Create and remove the test tables.

**Important:** This setup uses a separate in-memory database so test records don't get mixed with your development records. The test-only secret is not a production secret.

## 5. Test Student Endpoints

Create `test_students.py`.

```python
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
    response = client.post(
        "/students",
        json={
            "name": "P",
            "email": "invalid-email",
            "age": 24,
        },
    )

    assert response.status_code == 422
```

These tests check normal responses, authentication requirements, and request validation.

## 6. Test Authentication

Create `test_auth.py`.

```python
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
```

## 7. Run the Tests

From the `05-api-development` directory, execute:

```bash
python -m pytest lessons/05-api-testing -v
```

To run the tests with coverage:

```bash
python -m pytest lessons/05-api-testing \
    --cov=lessons/04-database-auth \
    --cov-report=term-missing
```

The coverage command may need adjustment if your project uses a different Python package layout. The first command should be your initial test.

Expected result: the tests pass and pytest reports the number of successful tests.

If a test fails, read the assertion and traceback. Fix the application or test setup rather than changing a correct expected result merely to make the test pass.

## 8. Run Ruff

Check code quality in the lesson files:

```bash
ruff check lessons/05-api-testing
```

Check formatting:

```bash
ruff format --check lessons/05-api-testing
```

To automatically fix supported formatting and lint issues:

```bash
ruff check --fix lessons/05-api-testing
ruff format lessons/05-api-testing
```

Review changes before committing them. Ruff can identify many style issues, unused imports, and common mistakes, but it doesn't replace tests or security review.

## 9. Exercises

### Exercise 1 — Test Student Retrieval

- Create an authenticated student.
- Retrieve the student by ID.
- Verify the returned name and email.
- Test an unknown student ID.

### Exercise 2 — Test Deletion

- Create a student.
- Delete it using an authenticated request.
- Confirm the expected success response.
- Retrieve the deleted ID and check for `404 Not Found`.

### Exercise 3 — Test JWT Validation

- Call `/auth/me` without a token.
- Call it with a malformed token.
- Call it with an expired token.
- Confirm that invalid credentials are rejected.

### Exercise 4 — Improve Coverage

- Test duplicate student email addresses.
- Test invalid registration data.
- Add a test for the minimum and maximum allowed student ages.
- Review which branches remain uncovered.

### Exercise 5 — Code Quality

- Run Ruff against your lesson.
- Fix unused imports and formatting issues.
- Run the full test suite again.
- Record the test results in this README.

## 10. Completion Checklist

- [ ] Installed pytest, httpx, pytest-cov, and Ruff.
- [ ] Created an isolated test database.
- [ ] Tested student endpoints.
- [ ] Tested registration and duplicate registration.
- [ ] Tested successful and unsuccessful login.
- [ ] Tested protected endpoints.
- [ ] Tested invalid request data.
- [ ] Ran pytest with coverage.
- [ ] Fixed Ruff issues.
- [ ] Committed the working tests to Git.

## 11. Expected Outcome

You will have a repeatable test suite for your FastAPI application. You will be able to detect regressions before committing code and verify that authentication and API validation continue to work.

## 12. Next Lesson

**Lesson 06 — GitHub Actions CI/CD and Deployment Readiness**

Next, automate your test suite using GitHub Actions so every push or pull request can run tests and code-quality checks. We'll prepare the application for deployment after the automated workflow works reliably.