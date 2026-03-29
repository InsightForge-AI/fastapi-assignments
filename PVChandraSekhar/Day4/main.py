from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}

@app.get("/posts")
def get_posts():
    return {"data": "This is my posts"}

@app.post("/createposts")
def create_posts():
    return {"data": "successfully created posts."}