from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


#Create a Pydantic model
class Student(BaseModel):
   name: str
   age: int
   course: str


# Create an empty dictionary to store student data
students = {}


# Create a GET endpoint to all students
@app.get("/students")
async def all_students():
   return students


# Create a GET endpoint to single student
@app.get("/students/{student_id}")
async def single_student(student_id: int):


   if student_id in students:
       return students[student_id]


   return {"message": "Student not found"}


# Create a POST endpoint to add student data
@app.post("/students/{student_id}")
async def Create_student(student_id: int, student : Student):
  
   students[student_id] = student.model_dump()
  
   return {
       "message": "Student created successfully",
       "data" : students[student_id]
       }


# Create a PUT endpoint to Update student data
@app.put("/students/{student_id}")
async def Update_student(student_id: int, student : Student):
   if student_id in students:
       students[student_id] = student.model_dump()
      
       return{
           "message": "Student Updated successfully",
           "data" : students[student_id]
       }
  
   return{"message": "Student not found"}


# Create a DELETE endpoint to Delete student data
@app.delete("/students/{student_id}")
async def Delete_data(student_id: int):
  if student_id in students:


       deleted_data = students.pop(student_id)


       return{
           "message": "Student Deleted successfully",
           "data": deleted_data
       }
  return{"message": "Student not found"}