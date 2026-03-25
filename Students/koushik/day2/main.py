from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Day2 FastAPI API"}

@app.get("/students")
def get_students():
    return ["Koushik", "Rahul", "Priya"]

@app.get("/course")
def course():
    return {"course": "FastAPI"}

@app.get("/status")
def status():
    return {"status": "API working"}