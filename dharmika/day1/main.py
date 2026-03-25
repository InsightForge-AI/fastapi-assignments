from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, Dharmika!"}