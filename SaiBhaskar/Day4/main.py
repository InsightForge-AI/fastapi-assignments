# day1
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message":"Hello World!"}

@app.get("/hello")
def hello():
    return{"message":"Hi! I  am sai"}

# day2
from fastapi import FastAPI
app = FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# day3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define request body
class User(BaseModel):
    name: str
    age: int

# POST API
@app.post("/user")
def create_user(user: User):
    return {
        "message": "User received successfully",
        "name": user.name,
        "age": user.age
    }