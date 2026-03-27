from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}