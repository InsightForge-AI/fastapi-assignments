from fastapi import FastAPI
from pydantic import BaseModel
import math


#calculator API will use postman to test the API

app = FastAPI()
# Root API
@app.get("/Calculator")
def read_root():
    return {"message": "Welcome to the Calculator API!"
    "This API supports the following operations: add, subtract, multiply, divide, modulus, exponentiation, floor_division, negation, multiplication_table, factorial, fibonacci, gcd, lcm, square_root. To perform an operation, send a POST request to /Calculator/operation with a JSON body containing the operation and operands.   Example JSON body for addition: {\"operation\": \"add\", \"a\": 5, \"b\": 3}"}



class CalcRequest(BaseModel):
    operation: str
    a: float
    b: float | None = None

@app.post("/Calculator/operation")
def calculate(req: CalcRequest):
    operation = req.operation
    a = req.a
    b = req.b

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {"error": "Division by zero is not allowed"}
        result = a / b
    elif operation == "modulus":
        if b == 0:
            return {"error": "Modulus by zero is not allowed"}
        result = a % b
    elif operation == "exponentiation":
        result = a ** b
    elif operation == "floor_division":
        if b == 0:
            return {"error": "Floor division by zero is not allowed"}
        result = a // b
    elif operation == "negation":
        result = -a
    elif operation == "multiplication_table":
        result = [a * i for i in range(1, 11)]
    elif operation == "factorial":
        if a < 0:
            return {"error": "Factorial not defined for negative numbers"}
        result = 1
        for i in range(1, int(a) + 1):
            result *= i
    elif operation == "fibonacci":
        n = int(a)
        result = []
        x, y = 0, 1
        for _ in range(n):
            result.append(x)
            x, y = y, x + y
    elif operation == "gcd":   
        result = math.gcd(int(a), int(b))
    elif operation == "lcm":
        result = abs(a * b) // math.gcd(int(a), int(b)) if a and b else 0
    elif operation == "square_root":
        result = a ** 0.5
    else:
        return {"error": "Invalid operation"}

    return {"result": result}