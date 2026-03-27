# STUDENT MANAGEMENT API  
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# Creating a List
students = []

# Home
@app.get("/")
def home():
    return {"message": "Day 5: Student Management API"}

# Create Student
@app.post("/students")
def create_student(student: Student):
    # Check duplicate ID
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")

    if student.age <= 0:
        raise HTTPException(status_code=400, detail="Age must be positive")

    students.append(student)
    return {"message": "Student created", "data": student}

# Get all students
@app.get("/students")
def get_students():
    return students

# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = updated_student
            return {"message": "Student updated", "data": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            students.pop(i)
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")