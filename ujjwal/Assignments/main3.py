from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
async def first():
    return {"message":"Hi, you can create post here"}

@app.post("/createpost")
def create_post(payload:dict=Body(...)):
    print(payload)
    name = payload.get("name")
    age = payload.get("age")

    return {
        "message": "User created successfully",
        "data": f"Name: {name}, Age: {age}"
    }
    