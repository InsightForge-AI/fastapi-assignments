from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class user(BaseModel): 
    name: str
    age: int

@app.post('/user')
async def create_user(user: user):
    return {
        'satus': 'success',
        'data': {
            'name': user.name,
            'age': user.age
        }
    }

