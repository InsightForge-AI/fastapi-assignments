from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# In-memory storage
students = []

# Home
@app.get('/')
def home():
    return {"message": "Student API is running"}

# create student
@app.post('/create')
def create_student(student: Student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="ID already exists")

    students.append(student)
    return {
        "message": "Student created successfully",
        "student": student
    }

# fetch all
@app.get('/students')
def get_students():
    return students

# fetch by ID
@app.get('/students/{student_id}')
def get_student(student_id: int):
    for s in students:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

# update
@app.put('/update/students/{student_id}')
def update_student(student_id: int, updated_student: Student):
    for index, s in enumerate(students):
        if s.id == student_id:
            students[index] = updated_student
            return {
                "message": "Student updated successfully",
                "student": updated_student
            }
    raise HTTPException(status_code=404, detail="Student not found")

# delete
@app.delete('/delete/students/{student_id}')
def delete_student(student_id: int):
    for index, s in enumerate(students):
        if s.id == student_id:
            deleted = students.pop(index)
            return {
                "message": "Student deleted successfully",
                "student": deleted
            }
    raise HTTPException(status_code=404, detail="Student not found")