from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hii {name}, Welcome to my API"}


@app.get("/calculate")
def calculate(operation: str, a: int, b: int):

    if operation == "add":
        return {
            "operation": "add",
            "a": a,
            "b": b,
            "result": a + b,
            "message": f"Addition of {a} and {b} is {a + b}"
        }

    elif operation == "subtract":
        return {
            "operation": "subtract",
            "a": a,
            "b": b,
            "result": a - b,
            "message": f"Subtraction of {a} and {b} is {a - b}"
        }

    elif operation == "multiply":
        return {
            "operation": "multiply",
            "a": a,
            "b": b,
            "result": a * b,
            "message": f"Multiplication of {a} and {b} is {a * b}"
        }

    elif operation == "divide":
        if b == 0:
            return {"error": "Division by zero is not allowed"}

        return {
            "operation": "divide",
            "a": a,
            "b": b,
            "result": a / b,
            "message": f"Division of {a} and {b} is {a / b}"
        }

    else:
        return {"error": "Invalid operation"}