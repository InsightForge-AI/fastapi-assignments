from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Day 4 API"}

@app.get("/students")
def get_students():
    return {"students": ["Narayani", "Jas", "Ram"]}

@app.post("/add")
def add_student(name: str):
    return {"message": f"{name} added successfully"}

@app.put("/update")
def update_student(name: str):
    return {"message": f"{name} updated successfully"}

@app.delete("/delete")
def delete_student(name: str):
    return {"message": f"{name} deleted successfully"}