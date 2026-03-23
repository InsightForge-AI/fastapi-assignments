from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI app!.."}


@app.get("/Hello")

def say_hello():
    return {"message": "Hello! The FastAPI app is working fine!.."}