from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to The First Day Project - FastAPI"}

@app.get("/hello")
def hello():
    return {"message": "Hello, DataMites"}