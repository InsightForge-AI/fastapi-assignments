Day 4: Postman Testing – Student API (CRUD Operations)
🚀 Overview

This project demonstrates how to test a simple Student API using Postman.
The API supports basic CRUD operations:

Create a student
Fetch student details
Delete a student

The backend is built using FastAPI, and all endpoints are tested using Postman.

🛠️ Tech Stack
Backend Framework: FastAPI
Testing Tool: Postman
Language: Python
📂 API Endpoints
1️⃣ Create Student (POST)
URL: /students
Method: POST
📥 Request Body
{
  "id": 1,
  "name": "Deepak",
  "age": 21,
  "course": "AI"
}
📤 Response
{
  "message": "Student created successfully",
  "student": {
    "id": 1,
    "name": "Deepak",
    "age": 21,
    "course": "AI"
  }
}
2️⃣ Get Student (GET)
URL: /students/{id}
Method: GET
📥 Example
/students/1
📤 Response
{
  "id": 1,
  "name": "Deepak",
  "age": 21,
  "course": "AI"
}
3️⃣ Delete Student (DELETE)
URL: /students/{id}
Method: DELETE
📥 Example
/students/1
📤 Response
{
  "message": "Student deleted successfully"
}
🧪 Postman Testing Steps
Open Postman
Select the HTTP method (POST, GET, DELETE)
Enter the API URL (e.g., http://127.0.0.1:8000/students)
For POST:
Go to Body → raw → JSON
Enter student data
Click Send
Verify the response