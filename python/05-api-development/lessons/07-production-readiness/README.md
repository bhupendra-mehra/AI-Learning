
# Lesson 07 — FastAPI Production Readiness

## Objective

Prepare the Student Management API for deployment by configuring environment variables, running the application without development reload, checking database persistence, and understanding production requirements.

## 1. Inspect the Project

From the project directory:

```bash
cd projects/student-management-api

cat README.md
cat requirements.txt
cat .env.example
```

Inspect these files:

- `app/main.py` — API routes and application startup
- `app/auth.py` — JWT authentication and secret configuration
- `app/database.py` — database connection and session management
- `tests/conftest.py` — isolated test database

Do not modify the existing API behavior unnecessarily.

## 2. Environment Variables

The application reads `SECRET_KEY` and `DATABASE_URL` from environment variables.

Create the local environment file if it does not exist:

```bash
cp .env.example .env
```

Generate a secure random key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Put the generated value in `.env`:

```dotenv
SECRET_KEY=replace-with-your-generated-secret
DATABASE_URL=sqlite:///./student_management.db
```

Never commit `.env` or a production secret to Git.

The application does not automatically load `.env` merely because the file exists. Export the variables before starting the application:

```bash
set -a
source .env
set +a
```

Verify that the key is configured without printing its value:

```bash
python -c "import os; print('SECRET_KEY configured:', bool(os.getenv('SECRET_KEY')))"
```

## 3. Run the API Locally

Activate the project's virtual environment:

```bash
source .venv/bin/activate
```

Start the API without development auto-reload:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open:

- Swagger UI: http://127.0.0.1:8000/docs
- Root endpoint: http://127.0.0.1:8000/
- Health endpoint: http://127.0.0.1:8000/health

Stop the application with `Ctrl+C`.

The absence of `--reload` avoids development file-watching behavior. This alone does not make the application fully production-ready.

## 4. Test the Running Application

Start the API in one terminal.

In a second terminal, run:

```bash
curl -i http://127.0.0.1:8000/
curl -i http://127.0.0.1:8000/health
```

Expected health response:

```json
{
  "status": "healthy"
}
```

Confirm that Swagger UI loads and the existing registration, login, student CRUD, PUT, and PATCH endpoints remain available.

## 5. Database Persistence

The project currently uses SQLite by default.

The database URL:

```text
sqlite:///./student_management.db
```

creates or opens a database file relative to the application's working directory.

Important considerations:

- Keep the database file out of Git.
- Confirm the database directory is writable.
- Avoid deleting the database file while the application is running.
- Test whether records remain after restarting the application.
- Use persistent storage when deploying to a host where local files may be temporary.

For production applications with multiple instances or more demanding workloads, evaluate PostgreSQL.

## 6. Database Schema Management

The current application creates tables using SQLAlchemy's `Base.metadata.create_all()` during startup.

This is convenient for learning, but it is not a complete database migration strategy.

Before production deployment, learn Alembic migrations so schema changes can be applied deliberately and safely.

Do not assume that changing a SQLAlchemy model automatically migrates an existing database.

## 7. Health Checks and Logging

The existing `/health` endpoint returns an application status.

A simple health endpoint is useful, but returning `healthy` does not prove that the database is reachable.

Production monitoring should distinguish:

- Liveness: whether the application process is running.
- Readiness: whether the application can serve requests, including required dependencies.

Also learn structured logging, error reporting, and monitoring without logging passwords, tokens, or other secrets.

## 8. Security Checklist

- [ ] Generate a strong secret key.
- [ ] Keep `.env` out of Git.
- [ ] Use separate secrets for testing, development, and production.
- [ ] Never expose debug details or secret values in API responses.
- [ ] Restrict database access and protect database backups.
- [ ] Configure CORS only for trusted frontend origins when needed.
- [ ] Consider rate limiting for authentication endpoints.
- [ ] Use HTTPS in deployed environments.
- [ ] Review dependency updates and security advisories.

## 9. Automated Quality Checks

Run from the Part 5 root:

```bash
cd /var/www/html/AI-Learning/python/05-api-development

ruff format --check \
  projects/student-management-api/app \
  projects/student-management-api/tests

ruff check \
  projects/student-management-api/app \
  projects/student-management-api/tests

pytest -v
```

All checks should pass before deployment.

## 10. Practical Exercises

- [ ] Start the application without `--reload`.
- [ ] Call the root and health endpoints using curl.
- [ ] Verify Swagger UI is accessible.
- [ ] Restart the application and check database persistence.
- [ ] Confirm `.env` and the SQLite database are ignored by Git.
- [ ] Explain why `create_all()` is not a migration system.
- [ ] Explain the difference between liveness and readiness.
- [ ] Run Ruff and pytest successfully.

## Completion Criteria

The lesson is complete when the API starts with the expected configuration, its endpoints remain functional, database behavior is understood, and automated checks pass.

Yes. We'll cover Lesson 07 — FastAPI Production Readiness in one go, just like your previous lessons: one complete `README.md`, all practical commands, configuration, exercises, and a completion checklist. No separate sub-lessons.

## 1. Final folder structure

Keep your existing lessons unchanged and add only:

```
python/05-api-development/
├── lessons/
│   ├── 01-http-rest-json/
│   ├── 02-requests-api-consumption/
│   ├── 03-fastapi/
│   ├── 04-database-auth/
│   ├── 05-api-testing/
│   ├── 06-github-cicd/
│   └── 07-production-readiness/
│       └── README.md
└── projects/
    └── student-management-api/
        ├── app/
        ├── tests/
        ├── requirements.txt
        ├── .env.example
        └── README.md
```

## 2. What the single lesson will cover

Environment configuration

Configure `SECRET_KEY` and `DATABASE_URL`, keep secrets out of Git, and load `.env` correctly.

Run the API

Start Uvicorn without development auto-reload and verify endpoints with `curl` and Swagger.

Database readiness

Understand SQLite persistence, PostgreSQL options, and why production schema changes need migrations.

Security and operations

Review secret management, HTTPS, logging, health checks, and production error handling.

Final verification

Run Ruff and pytest against only the standalone Student Management API project.

## 3. Create the lesson file

Run:

```
cd /var/www/html/AI-Learning/python/05-api-development

mkdir -p lessons/07-production-readiness
touch lessons/07-production-readiness/README.md
```

Use the complete lesson content from my previous response as the single README. It already includes the implementation steps, commands, security checklist, exercises, and completion criteria.

Important: Don't change the working API code just to complete this lesson. First verify its current configuration and behavior; make code changes only when a real gap is identified.

## 4. Final verification

From `python/05-api-development/`:

```
ruff format --check \
  projects/student-management-api/app \
  projects/student-management-api/tests

ruff check \
  projects/student-management-api/app \
  projects/student-management-api/tests

pytest -v
```

All checks should pass before you consider the lesson complete.

After that, we'll move directly to Lesson 08 — Dockerizing the Student Management API, also as one complete lesson with a single README, a Dockerfile, Docker Compose configuration, and practical testing.