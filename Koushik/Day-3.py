from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Day3 POST API"}

@app.post("/student")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }