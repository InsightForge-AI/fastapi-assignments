from fastapi import FastAPI

app = FastAPI()

# 1. Root API
@app.get("/")
def home():
    return {"message": "Welcome to API"}

# 2. Hello API
@app.get("/hello")
def hello():
    return {"message": "Hello Dharmika"}

# 3. Greet API with query
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

# 4. Add API
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# 5. POST API
@app.post("/user")
def create_user(data: dict):
    return {"received": data}