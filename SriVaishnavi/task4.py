from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API Testing with Postman", version="1.0.0")


#task1

@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI!",
        "task": "Task 1 - Basic Endpoints"
    }


@app.get("/hello")
async def hello():
    return {
        "message": "Hello, World!",
        "task": "Task 1"
    }


# TASK2

@app.get("/greet")
async def greet(name: str = "Guest"):
    return {
        "message": f"Hello, {name}!",
        "task": "Task 2 - Query Parameters"
    }


@app.get("/add")
async def add(a: int, b: int):
    result = a + b
    return {
        "result": result,
        "operation": f"{a} + {b} = {result}",
        "task": "Task 2"
    }


# task3

class Person(BaseModel):
    name: str
    age: int


@app.post("/person")
async def create_person(person: Person):
    return {
        "message": "Person created successfully!",
        "received_data": person,
        "status": "success",
        "task": "Task 3 - POST JSON"
    }


# task4

@app.get("/api-info")
async def api_info():
    return {
        "title": "FastAPI Testing Collection",
        "version": "1.0.0",
        "description": "All APIs for Postman testing",
        "endpoints": {
            "GET": ["/", "/hello", "/greet", "/add", "/api-info", "/status"],
            "POST": ["/person"]
        }
    }


@app.get("/status")
async def status():
    return {
        "status": "Server is running",
        "ready_for_postman": True
    }