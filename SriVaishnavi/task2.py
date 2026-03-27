from fastapi import FastAPI

app = FastAPI()


@app.get("/greet")
async def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
async def add(a: int, b: int):
    result = a + b
    return {"result": result, "operation": f"{a} + {b} = {result}"}
