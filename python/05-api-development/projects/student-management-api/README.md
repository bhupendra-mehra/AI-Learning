# Student Management API

A standalone FastAPI project with SQLAlchemy, SQLite, password hashing, JWT authentication, and automated tests.

## Features

- Health endpoint
- User registration and login
- JWT authentication for creating and deleting students
- Student list, detail, age filtering, creation, and deletion
- Duplicate-email handling and request validation
- pytest tests using an isolated in-memory SQLite database

## Setup

Run these commands from this project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set `SECRET_KEY` to a strong random value. Generate one with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

The application reads environment variables directly. If you want `.env` to be loaded automatically, start the app with the environment exported, or install/use a dotenv loader in your shell. For example:

```bash
set -a
source .env
set +a
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for Swagger UI.

## Test and lint

Run from this directory:

```bash
pytest -v
ruff check app tests
ruff format --check app tests
```

Tests use an in-memory database and do not use your local development database.

## Main endpoints

| Method | Endpoint | Access |
|---|---|---|
| GET | `/` | Public |
| GET | `/health` | Public |
| POST | `/auth/register` | Public |
| POST | `/auth/login` | Public; form fields `username` and `password` |
| GET | `/auth/me` | Authenticated |
| POST | `/students` | Authenticated |
| GET | `/students` | Public |
| GET | `/students/{student_id}` | Public |
| DELETE | `/students/{student_id}` | Authenticated |

For OAuth2 login, use the Authorize flow in Swagger. For direct JWT entry, paste the token using the JWT bearer authorization option and call a protected endpoint.

## Security notes

- Never commit `.env` or a real production secret.
- Use a separate database and secret for tests and development.
- This project is a learning baseline, not a production deployment blueprint. Review rate limiting, email validation, migrations, CORS, logging, and deployment security before production use.
