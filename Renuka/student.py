from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

# Model
class Student(BaseModel):
    id: int
    name: str
    age: int

# Home
@app.get("/")
def home():
    return {"message": "Student API Running"}

# Add student
@app.post("/student")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added", "data": student}

# Get all students
@app.get("/students")
def get_students():
    return {"students": students}

# Get single student
@app.get("/student/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    return {"message": "Student not found"}

# Delete student
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted"}
    return {"message": "Student not found"}