from fastapi import FastAPI
<<<<<<< HEAD
=======
from pydantic import BaseModel
>>>>>>> 3b20eb1d2e58c31e75dcade88a23ddef26902eba

app = FastAPI()

@app.get("/")
def home():
<<<<<<< HEAD
    return {"message": "Welcome to my first FastAPI app"}

@app.get("/hello")
def hello():
    return {"message": "Hello Renuka"}
=======
    return {"message": "Welcome to my API"}

@app.get("/hello")
def hello():
    return {"message": "Hello Renuka"}

# Model for POST request
class User(BaseModel):
    name: str
    age: int

# Existing GET APIs
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# POST API
@app.post("/user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }
>>>>>>> 3b20eb1d2e58c31e75dcade88a23ddef26902eba
