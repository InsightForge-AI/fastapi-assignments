from fastapi import FastAPI

# Create the app
app = FastAPI()

# Root endpoint: "/"
@app.get("/")
def read_root():
    return {"message": "Welcome to my first FastAPI app!"}

# Hello endpoint: "/hello"
@app.get("/hello")
def say_hello():
    return {"message": "Hello, beginner! You just built your first API 🎉"}