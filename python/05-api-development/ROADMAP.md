# Part 5 — API Development Roadmap

## Goal

Learn Python backend development and build a production-oriented Student Management REST API using FastAPI, SQL database integration, authentication, automated testing, and GitHub Actions.

## Prerequisites

- Python fundamentals completed.
- Functions, data structures, modules, and exception handling.
- Basic Git and GitHub operations.
- Python virtual environments and package installation.

---

## Lesson 01 — HTTP, REST APIs, and JSON

### Topics

- HTTP request and response lifecycle.
- HTTP methods: GET, POST, PUT, PATCH, DELETE.
- HTTP status codes: 2xx, 4xx, and 5xx.
- HTTP headers and request bodies.
- REST principles and resource-based URLs.
- JSON objects, arrays, and data types.
- Python JSON serialization and deserialization.
- API endpoint design and naming conventions.

### Practical Exercises

- Identify the correct HTTP method for common operations.
- Choose suitable status codes for success and failure cases.
- Convert Python dictionaries to JSON and back.
- Design endpoints for student CRUD operations.
- Explain the difference between 401 and 403.

### Deliverables

- `theory.md`
- `examples.py`
- `exercises.py`
- `README.md`

### Completion Criteria

Understand the HTTP request/response lifecycle and design REST endpoints using appropriate methods and status codes.

---

## Lesson 02 — Consuming APIs with Requests

### Topics

- Installing and importing `requests`.
- Sending GET and POST requests.
- PUT, PATCH, and DELETE requests.
- Query parameters and request headers.
- JSON request bodies and responses.
- HTTP status validation.
- Timeouts and exception handling.
- Working with API pagination.
- Environment variables for API configuration.
- Handling API errors safely.

### Practical Exercises

- Call a public REST API.
- Retrieve and filter JSON data.
- Submit a JSON request.
- Handle timeout and connection errors.
- Build a reusable API client function.

### Deliverables

- API client examples.
- A reusable request utility.
- Error-handling exercises.

### Completion Criteria

Consume an external API, process its JSON response, and handle common network failures reliably.

---

## Lesson 03 — FastAPI Fundamentals

### Topics

- Installing and running FastAPI.
- Application entry point and routing.
- Path parameters and query parameters.
- GET, POST, PUT, PATCH, and DELETE endpoints.
- Pydantic request and response models.
- Data validation and serialization.
- HTTPException and error responses.
- Response status codes.
- Dependency injection fundamentals.
- Automatic OpenAPI documentation.
- Swagger UI and ReDoc.

### Practical Exercises

- Create a FastAPI application.
- Implement a health-check endpoint.
- Build in-memory student CRUD endpoints.
- Validate incoming student data.
- Add response models and error handling.
- Test endpoints using Swagger UI.

### Deliverables

- Working FastAPI application.
- Student CRUD endpoints using temporary in-memory storage.
- API documentation accessible through `/docs`.

### Completion Criteria

Build and run a validated REST API and test its endpoints interactively.

---

## Lesson 04 — Database Integration and Authentication

### A. Database Integration

- SQL database fundamentals.
- SQLite for local development.
- SQLAlchemy ORM.
- Database models and relationships.
- Database sessions and dependency injection.
- CRUD operations using persistent storage.
- Alembic database migrations.
- Pagination, filtering, and data validation.

### B. Authentication and Authorization

- Authentication versus authorization.
- Password hashing and verification.
- User registration and login.
- JWT structure, claims, signing, and expiration.
- OAuth2 bearer-token authentication.
- Protected endpoints and current-user dependencies.
- Role-based access control.
- Handling expired or invalid tokens.
- Safe handling of secrets and configuration.
- When to use OAuth authorization-code flows for external identity providers.

### Practical Exercises

- Replace in-memory storage with a SQL database.
- Register a user and hash the password.
- Authenticate a user and issue an access token.
- Require authentication to access protected endpoints.
- Restrict selected operations by role.
- Test invalid credentials and expired tokens.

### Deliverables

- Database-backed student API.
- User and student database models.
- Authentication endpoints.
- Protected student routes.
- Database migration setup.

### Completion Criteria

Persist student data, authenticate users, and enforce access permissions correctly.

---

## Lesson 05 — API Testing and Code Quality

### Topics

- pytest fundamentals.
- FastAPI TestClient.
- Unit tests and API integration tests.
- Testing successful responses and validation errors.
- Testing CRUD operations.
- Authentication and authorization tests.
- Test fixtures and dependency overrides.
- Isolating test data from development data.
- Ruff linting and formatting.
- Environment-specific configuration.
- Basic test coverage.

### Practical Exercises

- Test the health-check endpoint.
- Test student creation, retrieval, update, and deletion.
- Test invalid request payloads.
- Test missing, invalid, and valid authentication tokens.
- Test unauthorized role access.
- Run Ruff and resolve reported issues.

### Deliverables

- `tests/conftest.py`
- `tests/test_health.py`
- `tests/test_students.py`
- `tests/test_auth.py`
- Ruff configuration.

### Completion Criteria

Run a repeatable automated test suite and verify API functionality, validation, and security behavior.

---

## Lesson 06 — GitHub Actions and CI/CD

### Topics

- GitHub Actions workflow syntax.
- Workflow triggers for pushes and pull requests.
- Python version setup.
- Dependency installation.
- Running pytest automatically.
- Running Ruff checks.
- Managing GitHub Actions secrets.
- Environment variables and configuration.
- Reading logs and debugging failed workflows.
- Continuous integration versus continuous deployment.
- Production-readiness checklist.

### Practical Exercises

- Create `.github/workflows/python-ci.yml`.
- Run tests on every push.
- Run tests and linting on pull requests.
- Fix a deliberately failing test.
- Verify that the workflow passes before merging changes.

### Deliverables

- Working GitHub Actions workflow.
- Automated test and lint checks.
- Updated project documentation.

### Completion Criteria

The repository automatically validates code changes and reports failed checks through GitHub Actions.

---

## Mini Project — Student Management REST API

### Objective

Combine all six lessons into a single backend application.

### Functional Requirements

#### Student Management

- Create a student.
- Retrieve a student by ID.
- List students with pagination.
- Filter students using supported fields.
- Update all student fields.
- Partially update selected fields.
- Delete a student.
- Validate email and required fields.
- Return appropriate HTTP status codes.

#### User Management and Security

- Register a user.
- Hash and verify passwords.
- Authenticate users.
- Issue and validate JWT access tokens.
- Protect student endpoints.
- Enforce role-based permissions.
- Prevent unauthorized access to protected operations.

#### Data and Reliability

- Persist data in a SQL database.
- Use SQLAlchemy for database access.
- Manage schema changes with Alembic.
- Handle invalid input and unexpected failures.
- Keep secrets outside the repository.

#### Testing and Automation

- Test CRUD operations.
- Test input validation.
- Test authentication and authorization.
- Run tests with pytest.
- Run Ruff checks.
- Automate both checks using GitHub Actions.

### Final Project Structure

```text
student-management-api/
├── README.md
├── requirements.txt
├── .env.example
├── alembic.ini
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── api/
│   │   ├── deps.py
│   │   └── routes/
│   │       ├── auth.py
│   │       └── students.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── db/
├── migrations/
└── tests/
    ├── conftest.py
    ├── test_health.py
    ├── test_students.py
    └── test_auth.py
```

### Final Verification Checklist

- [ ] All CRUD endpoints work.
- [ ] Student records persist in the database.
- [ ] Request validation works.
- [ ] Correct HTTP status codes are returned.
- [ ] Passwords are hashed.
- [ ] JWT authentication works.
- [ ] Protected endpoints enforce authorization.
- [ ] Automated tests pass.
- [ ] Ruff checks pass.
- [ ] GitHub Actions completes successfully.
- [ ] `.env` and secrets are excluded from Git.
- [ ] README includes setup, execution, testing, and API usage instructions.

---

## Part 5 — Completion Summary

After completing this roadmap, you should be able to:

- Build and consume REST APIs with Python.
- Develop backend services using FastAPI.
- Work with JSON, HTTP, and external APIs.
- Integrate a relational database.
- Implement authentication and authorization.
- Test backend applications automatically.
- Maintain code quality and automate checks using GitHub Actions.
- Structure a maintainable Python backend project.

**Next roadmap stage:** Apply these Python skills to data processing, AI API integration, and AI-powered applications.
