# Lesson 04 — Database & Authentication

## Goal

Upgrade the Student Management API using SQLite and SQLAlchemy, then secure API endpoints using authentication.

## 1. What You Will Learn

- SQLite database fundamentals
- SQLAlchemy ORM and database models
- Database sessions and CRUD operations
- Persistent data storage
- Password hashing
- JWT authentication
- Protected FastAPI endpoints

## 2. Project Structure

```text
04-database-auth/
├── README.md
├── main.py
├── database.py
├── models.py
├── schemas.py
└── auth.py
```

## 3. Install Dependencies

From the `05-api-development` directory, activate your existing virtual environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install sqlalchemy fastapi uvicorn pydantic email-validator "pwdlib[argon2]" pyjwt
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Keep `requirements.txt` in the `05-api-development` project root.

## 4. Configure the Database

Create `database.py`.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Practice:** Understand why the application needs a database engine, a session factory, and a database dependency.

## 5. Create the Student Database Model

Create `models.py`.

```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )
    age: Mapped[int] = mapped_column(Integer)
```

**Practice:** Understand how a Python class maps to a database table and how columns represent fields.

## 6. Create the API Schemas

Create `schemas.py`.

```python
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=1, le=120)


class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
```

Schemas validate incoming requests and define the data returned by the API. Database models and API schemas serve different purposes.

## 7. Build the Database-Backed API

Update `main.py`.

```python
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Student
from schemas import StudentCreate, StudentResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Student Management API",
    lifespan=lifespan,
)


@app.get("/")
def home():
    return {"message": "Student Management API is running"}


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db),
):
    student = Student(**student_data.model_dump())

    db.add(student)

    try:
        db.commit()
        db.refresh(student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this email already exists",
        )

    return student


@app.get("/students", response_model=list[StudentResponse])
def get_students(
    min_age: int | None = None,
    db: Session = Depends(get_db),
):
    query = select(Student)

    if min_age is not None:
        query = query.where(Student.age >= min_age)

    return db.scalars(query).all()


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    student = db.get(Student, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    student = db.get(Student, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}
```

This version implements create, list, retrieve, and delete operations. Add the update endpoint as an exercise.

## 8. Run and Test

From the `04-database-auth` directory:

```bash
../../.venv/bin/python -m uvicorn main:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Test the following endpoints:

| Method | Endpoint               | Expected result         |
| ------ | ---------------------- | ----------------------- |
| POST   | `/students`            | Creates a student       |
| GET    | `/students`            | Lists all students      |
| GET    | `/students?min_age=20` | Filters students by age |
| GET    | `/students/1`          | Returns student ID 1    |
| DELETE | `/students/1`          | Deletes student ID 1    |

Create a student using this JSON body:

```json
{
  "name": "Priya Patel",
  "email": "priya@example.com",
  "age": 24
}
```

Restart the server and retrieve the student again. The record should still exist because it is stored in SQLite.

## 9. Authentication — Next Part

After completing the database operations, implement authentication in `auth.py`.

Tasks:

1. Hash passwords using Argon2.
2. Never store plain-text passwords.
3. Create a login endpoint.
4. Issue and validate JWT access tokens.
5. Protect student creation, updating, and deletion endpoints.
6. Return HTTP 401 for missing or invalid credentials.
7. Store the JWT signing secret in an environment variable, not in source code.

Use a separate user model and password field rather than adding passwords to the student model.

Set `SECRET_KEY` in your Part 5 API project's `.env` file, not directly in `auth.py`. This key is used to sign and verify JWT tokens.

Your project should keep the secret outside GitHub so it is not exposed when you push your code.

## 1. Generate a secure secret key

From your Python virtual environment, run:

```
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

This generates a cryptographically secure random secret. Copy the output for your local configuration.

## 2. Set `SECRET_KEY` for your current project

Your existing `auth.py` reads the key using `os.getenv("SECRET_KEY")`, so the simplest approach is to set it in the terminal before starting FastAPI.

From your Lesson 04 directory, run:

```
cd /var/www/html/AI-Learning/python/05-api-development/lessons/04-database-auth

print from python

python -c "import secrets; print(secrets.token_hex(32))"

export SECRET_KEY="$(openssl rand -hex 32)"
```

Verify that it is set without displaying the secret:

```
python -c "import os; print('SECRET_KEY configured:', bool(os.getenv('SECRET_KEY')))"
```

Expected output:

```
SECRET_KEY configured: True
```

Start FastAPI in the same terminal session:

```
../../.venv/bin/python -m uvicorn main:app --reload
```

This environment variable remains available in that terminal session. If you open a new terminal, set it again.

## 3. Alternative: Store it in `.env`

If you prefer persistent local configuration, create this file:

`python/05-api-development/lessons/04-database-auth/.env`

```
SECRET_KEY=your-generated-secret-key
```

Generate the value using Step 1 above and replace the placeholder.

Install `python-dotenv` if needed:

```
../../.venv/bin/pip install python-dotenv
```

Then load the file near the top of `auth.py`, before calling `os.getenv()`:

```
import osfrom dotenv import load_dotenvload_dotenv()SECRET_KEY = os.getenv("SECRET_KEY")if not SECRET_KEY:    raise RuntimeError("SECRET_KEY is not configured")
```


## 10. Completion Checklist

- [x] Install SQLAlchemy and authentication dependencies.
- [x] Create the SQLite database configuration.
- [x] Create the Student ORM model.
- [x] Create Pydantic request and response schemas.
- [x] Implement database-backed student endpoints.
- [x] Verify records persist after restarting the server.
- [x] Handle duplicate email addresses.
- [x] Implement password hashing.
- [x] Implement JWT login and token validation.
- [x] Protect write endpoints.
- [x] Update this README with commands and test results.

## Expected Outcome

You will have a database-backed Student Management API with validated requests, persistent records, and authenticated endpoints.
