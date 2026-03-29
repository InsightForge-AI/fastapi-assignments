from fastapi import FastAPI, Body

app = FastAPI()

tasks = []

@app.post("/tasks")
def create_task(payload: dict = Body(...)):
    task = {
        "id": len(tasks) + 1,
        "title": payload.get("title"),
        "completed": False
    }
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return {"error": "Task not found"}

@app.put("/tasks/{id}")
def update_task(id: int, payload: dict = Body(...)):
    for task in tasks:
        if task["id"] == id:
            task["title"] = payload.get("title", task["title"])
            task["completed"] = payload.get("completed", task["completed"])
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for index, task in enumerate(tasks):
        if task["id"] == id:
            deleted = tasks.pop(index)
            return {"message": "Deleted", "task": deleted}
    return {"error": "Task not found"}