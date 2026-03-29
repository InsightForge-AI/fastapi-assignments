from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def login():
    return {"message":"Hi!"}

@app.get("/hello")
def user():
    return {"message":"This is my first API"}