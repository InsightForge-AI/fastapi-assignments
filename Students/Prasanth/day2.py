from fastapi import FastAPI

app = FastAPI()

# Sample database (temporary)
students = []

@app.get("/")
def home():
    return {"message": "Day 2 API 🚀"}

# GET all students
@app.get("/students")
def get_students():
    return students

# POST add student
@app.post("/students")
def add_student(name: str, age: int):
    student = {"name": name, "age": age}
    students.append(student)
    return {"message": "Student added", "data": student}