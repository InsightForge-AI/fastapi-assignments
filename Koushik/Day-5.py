from fastapi import FastAPI, HTTPException

# Initialize the FastAPI app
app = FastAPI(title="Sai's Calculator API")

@app.get("/")
def read_root():
    return {"message": "Calculator API is online! Go to /docs to start calculating."}

# Addition Endpoint
@app.get("/add")
def add(num1: float, num2: float):
    return {"operation"
    "": "addition", "result": num1 + num2}

# Subtraction Endpoint
@app.get("/subtract")
def subtract(num1: float, num2: float):
    return {"operation": "subtraction", "result": num1 - num2}

# Multiplication Endpoint
@app.get("/multiply")
def multiply(num1: float, num2: float):
    return {"operation": "multiplication", "result": num1 * num2}

# Division Endpoint (with error handling!)
@app.get("/divide")
def divide(num1: float, num2: float):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Error: You cannot divide by zero!")
    return {"operation": "division", "result": num1 / num2}


@app.get("/pow")
def power(base: float, exponent: float):
    return {
        "operation": "power", 
        "base": base, 
        "exponent": exponent, 
        "result": base ** exponent
    }