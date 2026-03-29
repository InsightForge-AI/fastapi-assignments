from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {
        "message": f"{user.name} is {user.age} years old"
    }
