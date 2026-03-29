from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Day 1 Project - FastAPI"}

@app.get("/hello")
def hello():
    return {"message": "Hello World!"}