from fastapi import FastAPI
from Day2.routes import ai_routes, file_routes

app = FastAPI()   # ✅ FIRST create app

app.include_router(ai_routes.router)
app.include_router(file_routes.router)

@app.get("/")
def root():
    return {"message": "Day 2 Running 🚀"}