from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
<<<<<<< HEAD
    return {"message": "Welcome"}

@app.get("/hello")
def hello():
    return {"message": "Hello Sreeja 👋"}

