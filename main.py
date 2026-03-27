from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"info": "This is my first API"}


@app.post("/test")
def test_post():
    return {"message": "post is working"}


from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


@app.post("/user")
def create_user(user: User):
    return {"message": "User received", "data": user.dict()}


from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# ------------------- BASIC ROUTES -------------------


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"info": "This is my first API"}


@app.post("/test")
def test_post():
    return {"message": "post is working"}


# ------------------- USER MODEL -------------------


class User(BaseModel):
    name: str
    age: int


@app.post("/user")
def create_user(user: User):
    return {"message": "User received", "data": user.dict()}



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalcInput(BaseModel):
    a: float
    b: float
    op: str

@app.post("/calculate_post")
def calculate_post(data: CalcInput):
    if data.op == "add":
        result = data.a + data.b
    elif data.op == "sub":
        result = data.a - data.b
    elif data.op == "mul":
        result = data.a * data.b
    elif data.op == "div":
        if data.b == 0:
            return {"error": "Division by zero"}
        result = data.a / data.b
    else:
        return {"error": "Invalid operation"}

    return {
        "a": data.a,
        "b": data.b,
        "operation": data.op,
        "result": result
    }