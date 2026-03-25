from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first API"}

@app.get("/hello")
def hello():
    return {"message": "helloooo"}