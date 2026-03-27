# FastAPI Calculator API

## 🚀 Features
- Basic routes (/ , /about)
- POST endpoint (/test)
- User creation API (/user)
- Calculator API (/calculate_post)

## 🛠 Tech Stack
- FastAPI
- Python
- Pydantic

## ▶️ How to Run
1. Clone repo
2. Create virtual environment
3. Install dependencies:
   pip install fastapi uvicorn

4. Run server:
   uvicorn main:app --reload

## 📌 API Endpoints

### GET /
Returns Hello World

### POST /calculate_post
Sample input:
{
  "a": 10,
  "b": 5,
  "op": "add"
}

## 📷 Screenshots
(Add Postman screenshots)

## 👨‍💻 Author
Mohammad Muneeb Ali
