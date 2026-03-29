from fastapi import FastAPI
<<<<<<< HEAD
<<<<<<< HEAD
=======
from pydantic import BaseModel
>>>>>>> 3b20eb1d2e58c31e75dcade88a23ddef26902eba
=======
from pydantic import BaseModel
>>>>>>> e64b9f7e74270c30bbc2e8ebbcc812da4bc44694

app = FastAPI()

@app.get("/")
def home():
<<<<<<< HEAD
<<<<<<< HEAD
    return {"message": "Welcome to my first FastAPI app"}

@app.get("/hello")
def hello():
    return {"message": "Hello Renuka"}
=======
=======
>>>>>>> e64b9f7e74270c30bbc2e8ebbcc812da4bc44694
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
<<<<<<< HEAD
    }
>>>>>>> 3b20eb1d2e58c31e75dcade88a23ddef26902eba
=======
    }
>>>>>>> e64b9f7e74270c30bbc2e8ebbcc812da4bc44694
