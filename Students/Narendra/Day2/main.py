from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Model (data format)
class Student(BaseModel):
   name: str
   age: int
   course: str


# GET method for testing
@app.get("/")
def home():
   return {"message": "Day 2 POST API working"}


# POST method for creating a student
@app.post("/student")
def create_student(student: Student):
   return {
       "message": "Student created successfully",
       "data": student
   }
