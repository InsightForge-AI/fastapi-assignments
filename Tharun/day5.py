from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate")
def do_math(body: CalculationRequest):
    n1 = body.num1
    n2 = body.num2
    op = body.operation.lower()

    if op == "add":
        result = n1 + n2
    elif op == "subtract":
        result = n1 - n2
    elif op == "multiply":
        result = n1 * n2
    elif op == "divide":
        if n2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = n1 / n2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    return {"result": result}