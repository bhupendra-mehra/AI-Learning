# Lesson 03 — Building REST APIs with FastAPI

## 1. Learning Objectives

By the end of this lesson, I will be able to:

- Build REST APIs using FastAPI.
- Create GET, POST, PUT, and DELETE endpoints.
- Handle path and query parameters.
- Accept and validate JSON request bodies.
- Use Pydantic models for data validation.
- Handle HTTP errors.
- Test APIs through Swagger UI.
- Run an API locally using Uvicorn.

## 2. Prerequisites

- Python basics and functions.
- Lesson 01 — HTTP, REST, and JSON.
- Lesson 02 — Consuming REST APIs with Requests.
- Python virtual environment.
- Basic Git commands.

## 3. What Is FastAPI?

FastAPI is a Python framework for building APIs.

It provides:

- HTTP endpoint routing.
- Request and response validation.
- Automatic API documentation.
- JSON serialization.
- Integration with Python type hints.
- Support for asynchronous endpoints.

FastAPI uses Pydantic to validate structured request data.

## 4. Install Dependencies

```bash
python -m pip install fastapi "uvicorn[standard]"
```

Check the installed packages:

```bash
python -m pip show fastapi
python -m pip show uvicorn
```

## 5. Create Your First API

Create `main.py` inside this lesson folder.

```python
from fastapi import FastAPI

app = FastAPI(title="Student Management API")


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

### Run the API

```bash
python -m uvicorn main:app --reload
```

Open these URLs in your browser:

- API home: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Interactive API documentation: http://127.0.0.1:8000/docs

The `main:app` argument means the `app` object inside `main.py`.

The `--reload` option automatically restarts the server when you modify the code. Use it for local development.

## 6. Understand HTTP Methods

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve data | Get all students |
| POST | Create data | Add a student |
| PUT | Update a resource | Update a student's details |
| DELETE | Delete data | Remove a student |

These methods describe common API operations. The server determines the actual behavior.

## 7. Create a Student API

Replace the contents of `main.py` with the following complete example.

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Student Management API")


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str
    age: int = Field(ge=1, le=120)


class Student(StudentCreate):
    id: int


students: dict[int, Student] = {}
next_student_id = 1


@app.get("/")
def home():
    return {"message": "Student Management API is running"}


@app.get("/students", response_model=list[Student])
def get_students():
    return list(students.values())


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student


@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED,
)
def create_student(student_data: StudentCreate):
    global next_student_id

    student = Student(
        id=next_student_id,
        **student_data.model_dump(),
    )

    students[next_student_id] = student
    next_student_id += 1

    return student


@app.put("/students/{student_id}", response_model=Student)
def update_student(
    student_id: int,
    student_data: StudentCreate,
):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    updated_student = Student(
        id=student_id,
        **student_data.model_dump(),
    )

    students[student_id] = updated_student

    return updated_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    del students[student_id]

    return {"message": "Student deleted successfully"}
```

### Important concepts

**`@app.get()` and `@app.post()`**

These decorators connect URLs and HTTP methods to Python functions.

**`BaseModel`**

Pydantic models define the expected request structure and validate incoming data.

**`Field()`**

Adds validation rules. For example, the student's age must be between 1 and 120.

**`HTTPException`**

Returns an appropriate HTTP error response when a student doesn't exist.

**`response_model`**

Documents and validates the structure of successful responses.

**`status_code`**

Allows the API to return `201 Created` when a student is created.

**Important limitation:** This example stores students in memory. Data disappears when the server restarts, and it is not suitable for concurrent production use. Database persistence will be introduced in a later lesson.

## 8. Test the API with Swagger UI

Start the server:

```bash
python -m uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000/docs

Use the interactive interface to test each endpoint.

### Create a student

Select `POST /students` and submit:

```json
{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "age": 25
}
```

Expected result: HTTP `201 Created`, with a generated student ID.

### Retrieve all students

Select `GET /students`.

Expected result: a JSON array containing the students you created.

### Retrieve one student

Select `GET /students/{student_id}` and enter `1`.

Expected result: the details of student 1.

### Update a student

Select `PUT /students/{student_id}` and submit:

```json
{
  "name": "Rahul Sharma",
  "email": "rahul.updated@example.com",
  "age": 26
}
```

Expected result: updated student information.

### Delete a student

Select `DELETE /students/{student_id}` and enter `1`.

Expected result: a successful deletion message.

### Test validation

Try creating a student with an age of `-5` or a name containing only one character.

Expected result: HTTP `422 Unprocessable Entity` because the input fails validation.

## 9. Test with Python Requests

Create a file called `test_api.py`.

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

payload = {
    "name": "Priya Patel",
    "email": "priya@example.com",
    "age": 24,
}

response = requests.post(
    f"{BASE_URL}/students",
    json=payload,
    timeout=10,
)

response.raise_for_status()

student = response.json()

print("Created student:", student)

student_id = student["id"]

response = requests.get(
    f"{BASE_URL}/students/{student_id}",
    timeout=10,
)

response.raise_for_status()

print("Retrieved student:", response.json())
```

Keep the API server running in one terminal. Run the test script from another terminal with the appropriate virtual environment activated.

```bash
python test_api.py
```

This connects the concepts from Lesson 02 with the API you built in this lesson.

## 10. Error Handling and HTTP Status Codes

| Status code | Meaning | Example |
|---|---|---|
| 200 | OK | Retrieve a student |
| 201 | Created | Create a student |
| 404 | Not Found | Student ID doesn't exist |
| 422 | Validation Error | Invalid request data |
| 500 | Internal Server Error | Unexpected server failure |

FastAPI automatically handles many request validation errors. Use `HTTPException` for expected application errors, and avoid exposing sensitive internal error details to API clients.

## 11. Exercises

### Exercise 1 — Health Check

- Create a `/health` endpoint.
- Return `{"status": "healthy"}`.
- Verify the endpoint in Swagger UI.

### Exercise 2 — Student Creation

- Create at least three students.
- Verify that each receives a unique ID.
- Retrieve all students.

### Exercise 3 — Validation

- Reject names shorter than two characters.
- Reject ages below 1 or above 120.
- Observe the response for invalid input.

### Exercise 4 — Error Handling

- Retrieve a nonexistent student.
- Update a nonexistent student.
- Delete a nonexistent student.
- Verify that each returns HTTP 404.

### Exercise 5 — API Integration

- Use `requests` to create a student.
- Retrieve the created student.
- Print the student's name and email.

### Exercise 6 — Extend the API

Add a GET endpoint that filters students by age using a query parameter.

For example:

`GET /students?min_age=20`

Return only students whose age is at least the supplied value.

## 12. Magento / PHP Comparison

| FastAPI / Python | Magento 2 / PHP |
|---|---|
| Route decorators | Web API route configuration |
| Pydantic models | Data interfaces and validation |
| `HTTPException` | HTTP exception handling |
| Python endpoint functions | Service classes and controllers |
| Automatic OpenAPI documentation | REST API documentation and schema |

FastAPI is useful for building independent services that can integrate with Magento through REST APIs.

## 13. Completion Checklist

- [X] Installed FastAPI and Uvicorn.
- [X] Created `main.py`.
- [X] Started the development server.
- [X] Opened Swagger UI.
- [X] Implemented GET, POST, PUT, and DELETE.
- [X] Validated request data with Pydantic.
- [X] Handled missing student records.
- [X] Tested the API using Python Requests.
- [X] Completed the exercises.
- [X] Committed the lesson to Git.

## 14. Key Takeaways

- FastAPI helps build REST APIs with Python.
- Decorators map HTTP methods and paths to endpoint functions.
- Pydantic validates incoming request data.
- Swagger UI makes interactive API testing straightforward.
- HTTP status codes communicate the result of a request.
- In-memory storage is for learning; production APIs need persistent storage.