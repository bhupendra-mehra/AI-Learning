# Lesson 01 — HTTP, REST APIs and JSON

## 1. Objective

Understand how clients and servers communicate over HTTP, how REST APIs are designed, and how Python handles JSON data.

By the end of this lesson, you should be able to:
- Understand HTTP requests and responses.
- Use HTTP methods and identify status codes.
- Understand request and response headers.
- Design REST API endpoints.
- Convert Python objects to JSON and back.
- Prepare for consuming APIs using the Python `requests` library.

---

## 2. HTTP Fundamentals

HTTP (Hypertext Transfer Protocol) is used for communication between clients and servers.

### HTTP Request Lifecycle

1. The client sends an HTTP request to a server.
2. The server processes the request.
3. The server performs the required operation.
4. The server returns an HTTP response.
5. The client processes the response.

Example:

```http
GET /students/1 HTTP/1.1
Host: example.com
Accept: application/json
```

Example response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Rahul Sharma"
}
```

An HTTP request may contain:
- Method
- URL or path
- Headers
- Optional request body

An HTTP response may contain:
- Status code
- Headers
- Optional response body

---

## 3. HTTP Methods

HTTP methods describe the operation a client wants to perform.

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve data | `GET /students` |
| POST | Create a resource | `POST /students` |
| PUT | Replace a resource | `PUT /students/1` |
| PATCH | Partially update a resource | `PATCH /students/1` |
| DELETE | Delete a resource | `DELETE /students/1` |

### Example

To retrieve a student:

```http
GET /students/1
```

To create a student:

```http
POST /students
Content-Type: application/json

{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "age": 22
}
```

**Important:** GET is intended for retrieving data. POST commonly creates resources. PUT replaces a resource, while PATCH updates selected fields.

---

## 4. HTTP Status Codes

Status codes indicate the result of an HTTP request.

| Code | Meaning | Example |
|---|---|---|
| 200 | OK | Student retrieved successfully |
| 201 | Created | Student created successfully |
| 204 | No Content | Student deleted successfully |
| 400 | Bad Request | Request cannot be processed |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | User lacks permission |
| 404 | Not Found | Student does not exist |
| 422 | Unprocessable Content | Request validation failed |
| 500 | Internal Server Error | Unexpected server failure |

### Status Code Categories

- `2xx`: Successful requests.
- `3xx`: Redirection.
- `4xx`: Client-side errors.
- `5xx`: Server-side errors.

### 401 vs. 403

- **401:** The request lacks valid authentication credentials.
- **403:** The server understands the request but refuses access because the client lacks permission.

---

## 5. HTTP Headers

Headers provide metadata about requests and responses.

### Common Headers

| Header | Purpose |
|---|---|
| `Content-Type` | Describes the body format |
| `Accept` | Specifies acceptable response formats |
| `Authorization` | Carries authentication credentials |
| `User-Agent` | Identifies the client software |
| `Cache-Control` | Provides caching instructions |

Example:

```http
Content-Type: application/json
Accept: application/json
Authorization: Bearer <access_token>
```

`Content-Type` describes the format of the body being sent. `Accept` indicates the formats the client can receive.

The `Authorization` header is used when an endpoint requires authentication.

---

## 6. REST API Fundamentals

REST stands for Representational State Transfer. It is an architectural style commonly used to design web APIs.

REST APIs expose resources through predictable URLs and use HTTP methods to operate on those resources.

### REST Design Principles

- Use nouns to represent resources.
- Use HTTP methods to describe operations.
- Return meaningful status codes.
- Keep request and response formats consistent.
- Use stateless requests: each request contains the information needed to process it, including authentication credentials when required.
- Validate incoming data.
- Provide predictable error responses.

### Student Management API Examples

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/students` | List students |
| GET | `/students/1` | Retrieve student 1 |
| POST | `/students` | Create a student |
| PUT | `/students/1` | Replace student 1 |
| PATCH | `/students/1` | Partially update student 1 |
| DELETE | `/students/1` | Delete student 1 |

Prefer resource-oriented paths such as `/students` over action-oriented paths such as `/getStudents`.

---

| Feature | PUT | PATCH |
| :--- | :--- | :--- |
| **Primary Purpose** | Full resource replacement (or creation) | Partial resource updates |
| **Request Payload** | Must contain the **complete resource** | Contains **only the fields** being changed |
| **Idempotency** | **Always idempotent** (repeating the request yields the same result) | **Not always idempotent** (depends on how it is implemented) |
| **Omitted Fields** | Cleared, set to `null`, or reverted to defaults | Left completely unchanged |
| **Bandwidth Usage** | Higher (transmits all data) | Lower (transmits only the changes) |

| Feature | Request Headers | Request Body |
| :--- | :--- | :--- |
| **Primary Purpose** | Provide metadata and context about the request | Carry the actual data payload |
| **Content Type** | Key-value pairs (plain text) | Flexible formats (JSON, XML, Form Data, Binary) |
| **HTTP Methods** | Required for **all** HTTP methods (`GET`, `POST`, etc.) | Typically used in `POST`, `PUT`, and `PATCH` |
| **Visibility** | Sent as part of the initial HTTP message line | Sent after the headers, separated by a blank line |
| **Examples** | `Content-Type`, `Authorization`, `User-Agent` | `{"username": "alex", "password": "secure123"}` |


## 7. JSON Fundamentals

JSON (JavaScript Object Notation) is a lightweight text format used to exchange structured data between applications.

### Example JSON Object

```json
{
  "id": 1,
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "age": 22,
  "active": true,
  "skills": ["Python", "SQL"],
  "address": null
}
```

### JSON Data Types

| JSON type | Example | Python equivalent |
|---|---|---|
| String | `"Rahul"` | `str` |
| Number | `22` | `int` or `float` |
| Boolean | `true` | `True` |
| Array | `[1, 2, 3]` | `list` |
| Object | `{"id": 1}` | `dict` |
| Null | `null` | `None` |

JSON uses lowercase `true`, `false`, and `null`. Python uses `True`, `False`, and `None`.

---

## 8. Python JSON Module

Python provides the built-in `json` module to convert between Python objects and JSON.

### Important Functions

| Function | Purpose |
|---|---|
| `json.dumps()` | Python object to JSON string |
| `json.loads()` | JSON string to Python object |
| `json.dump()` | Write JSON data to a file |
| `json.load()` | Read JSON data from a file |

### Practical Example

Create `examples.py` in this lesson directory.

```python
import json

student = {
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "age": 22,
    "skills": ["Python", "SQL"],
}

# Convert a Python dictionary to a JSON string.
json_string = json.dumps(student, indent=2)

print("JSON Data:")
print(json_string)

# Convert the JSON string back to a Python dictionary.
parsed_student = json.loads(json_string)

print("\nStudent Name:", parsed_student["name"])
print("Student Age:", parsed_student["age"])
print("Student Skills:", parsed_student["skills"])
```

Run the example:

```bash
python examples.py
```

Expected output:

```text
Student Name: Rahul Sharma
Student Age: 22
Student Skills: ['Python', 'SQL']
```

### Writing JSON to a File

```python
import json

student = {
    "id": 1,
    "name": "Rahul Sharma",
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=2)
```

### Reading JSON from a File

```python
import json

with open("student.json", encoding="utf-8") as file:
    student = json.load(file)

print(student["name"])
```

**Important:** JSON serialization and deserialization are fundamental when building APIs because API clients and servers frequently exchange JSON request and response bodies.

---

## 9. Exercises

Complete these exercises in `exercises.py`.

### Exercise 1 — HTTP Methods

Write down the correct HTTP method for each operation:

1. Retrieve all students.
2. Create a student.
3. Replace a student's complete record.
4. Update only a student's email.
5. Delete a student.

### Exercise 2 — Status Codes

Choose the appropriate status code for each scenario:

1. A student is retrieved successfully.
2. A student is created successfully.
3. The requested student does not exist.
4. Authentication credentials are missing.
5. The authenticated user does not have the required permission.
6. A request fails data validation.

### Exercise 3 — REST Endpoint Design

Design endpoints for these operations:

1. List all students.
2. Retrieve student ID 10.
3. Create a new student.
4. Update student ID 10's email.
5. Delete student ID 10.

Write both the HTTP method and endpoint.

### Exercise 4 — JSON Conversion

Create a dictionary representing a student with:

- `id`
- `name`
- `email`
- `age`
- `skills`

Convert it to a JSON string using `json.dumps()`. Convert the string back using `json.loads()` and print the student's name and skills.

### Exercise 5 — JSON File Handling

Write a Python program that:

1. Creates a student dictionary.
2. Saves it to `student.json`.
3. Reads the file back.
4. Prints the student's details.

### Exercise 6 — Conceptual Questions

Answer the following:

1. What is HTTP?
2. What is a REST API?
3. What is the difference between PUT and PATCH?
4. What is the difference between `json.dumps()` and `json.loads()`?
5. What is the difference between request headers and a request body?
6. Why do APIs use status codes?

---

## 10. GitHub Workflow

From your repository root, check the changed files:

```bash
git status
```

Stage the lesson files:

```bash
git add python/05-api-development/lessons/01-http-rest-json/
```

Commit the lesson:

```bash
git commit -m "feat(python): add HTTP REST and JSON lesson"
```

Push to GitHub:

```bash
git push
```

---

## 11. Completion Checklist

- [ ] Understand the HTTP request and response lifecycle.
- [ ] Understand GET, POST, PUT, PATCH, and DELETE.
- [ ] Identify common HTTP status codes.
- [ ] Understand HTTP headers.
- [ ] Design resource-based REST endpoints.
- [ ] Understand JSON data types.
- [ ] Use `json.dumps()` and `json.loads()`.
- [ ] Read and write JSON files.
- [ ] Complete the exercises.
- [ ] Commit and push the lesson to GitHub.

## 12. Key Takeaways

HTTP defines communication between clients and servers. REST provides a consistent approach to designing APIs around resources. JSON provides a standard format for exchanging structured data.

These concepts are the foundation for the next lesson, where you will use Python's `requests` library to consume real REST APIs.