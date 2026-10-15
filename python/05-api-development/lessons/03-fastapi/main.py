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
def get_students(min_age: int | None = None):
    student_list = list(students.values())

    if min_age is not None:
        student_list = [student for student in student_list if student.age >= min_age]

    return student_list


@app.get("/student/{student_id}", response_model=Student)
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
