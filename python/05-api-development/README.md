# Part 5 — API Development with Python

## Overview

**Goal:** Learn Python backend development by understanding HTTP, consuming REST APIs, building APIs with FastAPI, implementing authentication, testing endpoints, and automating checks using GitHub Actions.

This part focuses on practical development skills and a complete **Student Management REST API** project.

## Learning Objectives

By completing Part 5, you will be able to:

- Understand HTTP methods, status codes, headers, and request/response cycles.
- Understand REST API principles and resource-based endpoint design.
- Work with JSON and Python's built-in `json` module.
- Consume external APIs using the Python `requests` library.
- Build REST APIs using FastAPI and Pydantic.
- Implement CRUD operations and database integration.
- Understand password hashing, JWT, OAuth2, and role-based authorization.
- Write automated API tests using pytest and FastAPI TestClient.
- Apply code quality checks using Ruff.
- Configure GitHub Actions for continuous integration.
- Organize a Python backend project using maintainable architecture.

## Repository Structure

```text
part-05-api-development/
├── README.md
├── ROADMAP.md
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
│
├── lessons/
│   ├── lesson-01-http-rest-json/
│   ├── lesson-02-requests-client/
│   ├── lesson-03-fastapi/
│   ├── lesson-04-database-auth/
│   ├── lesson-05-testing/
│   └── lesson-06-github-cicd/
│
├── projects/
│   └── student-management-api/
│       ├── README.md
│       ├── requirements.txt
│       ├── .env.example
│       ├── alembic.ini
│       ├── app/
│       │   ├── main.py
│       │   ├── core/
│       │   │   ├── config.py
│       │   │   └── security.py
│       │   ├── api/
│       │   │   ├── deps.py
│       │   │   └── routes/
│       │   │       ├── auth.py
│       │   │       └── students.py
│       │   ├── models/
│       │   ├── schemas/
│       │   ├── services/
│       │   └── db/
│       ├── migrations/
│       └── tests/
│           ├── conftest.py
│           ├── test_students.py
│           ├── test_auth.py
│           └── test_health.py
│
└── .github/
    └── workflows/
        └── python-ci.yml
```

The structure will be created incrementally as the lessons progress. Avoid creating empty files before they are needed.

## Lessons

| Lesson | Topics | Outcome |
|---|---|---|
| 01 | HTTP, REST APIs, JSON | Understand API communication and design |
| 02 | Python Requests library | Consume external REST APIs |
| 03 | FastAPI fundamentals | Build endpoints and validate requests |
| 04 | Database and authentication | Implement CRUD, JWT, and access control |
| 05 | API testing and code quality | Automate API tests and linting |
| 06 | GitHub Actions and CI/CD | Automate project validation |

Refer to [ROADMAP.md](ROADMAP.md) for the detailed lesson plan, exercises, and completion checklist.

## Main Project — Student Management REST API

Build a backend service to manage student records.

### Core Features

- Create, retrieve, update, and delete student records.
- List students with pagination and filtering.
- Validate request data using Pydantic.
- Store student records in a SQL database.
- Register users and authenticate them.
- Issue and validate JWT access tokens.
- Protect endpoints using authentication and authorization.
- Return appropriate HTTP status codes and structured JSON responses.
- Test API endpoints and authentication behavior.
- Run automated quality checks through GitHub Actions.

### Example Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check service health |
| POST | `/auth/register` | Register a user |
| POST | `/auth/token` | Obtain an access token |
| GET | `/students` | List students |
| POST | `/students` | Create a student |
| GET | `/students/{student_id}` | Retrieve a student |
| PUT | `/students/{student_id}` | Replace student data |
| PATCH | `/students/{student_id}` | Update selected fields |
| DELETE | `/students/{student_id}` | Delete a student |

## Technology Stack

- **Language:** Python
- **API framework:** FastAPI
- **Validation:** Pydantic
- **HTTP client:** Requests
- **Database:** SQLite initially, with SQLAlchemy and Alembic
- **Authentication:** Password hashing, JWT, OAuth2
- **Testing:** pytest and FastAPI TestClient
- **Code quality:** Ruff
- **Version control:** Git and GitHub
- **CI/CD:** GitHub Actions

## Development Setup

Create and activate a virtual environment from the Part 5 directory.

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies after creating `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Run tests when the test suite is available:

```bash
python -m pytest
```

Run Ruff when configured:

```bash
ruff check .
```

## Git Workflow

Commit work in small, meaningful changes.

```bash
git status
git add .
git commit -m "feat(python): implement API feature"
git push
```

Use descriptive commit messages such as:

- `docs(python): add HTTP and REST notes`
- `feat(python): add FastAPI student endpoints`
- `test(python): add student API tests`
- `ci(python): configure GitHub Actions`

## Security Guidelines

- Never commit `.env` files, passwords, API keys, or real access tokens.
- Maintain `.env.example` with placeholder values only.
- Hash passwords; never store plaintext passwords.
- Validate authentication and authorization on protected endpoints.
- Use environment variables for configuration and secrets.
- Use HTTPS in production.
- Keep dependencies updated.

## Completion Criteria

Part 5 is complete when the Student Management API supports CRUD operations, database persistence, validated requests, authentication, automated tests, code quality checks, and a working GitHub Actions CI pipeline.

## Learning Approach

Complete each lesson in order. Read the notes, run the examples, solve the exercises, test your code, and commit the completed work to GitHub.

The focus is on building a working backend project rather than memorizing theory.
