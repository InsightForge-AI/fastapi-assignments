from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome Sayali 🚀",
        "status": "success"
    }

@app.get("/hello")
def hello(name: str = "User"):
    return {
        "message": f"Hello, {name} 👋"
    }

@app.get("/health")
def health():
    return {
        "status": "API running successfully ✅"
    }