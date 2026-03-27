from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel, EmailStr
import mysql.connector

# pydantic model 
class signup(BaseModel):
  email: EmailStr
  phone: str
  password: str


# DB connection
def get_connection():
  return mysql.connector.connect(
    host="127.0.0.1",
    database = "fastapi",
    user = "root",
    password="********"
  )


app = FastAPI()

# signup
@app.post("/signup")
async def signup_fun(su: signup):
  try:
      conn = get_connection()
      cursor = conn.cursor()
      query = "INSERT INTO users (email, phone, password) VALUES (%s, %s, %s)"
      cursor.execute(query, (su.email, su.phone, su.password))
      conn.commit()
      cursor.close()
      conn.close()
      return {
            "message" : "user stored successfully"
        }
  except Exception as e:
        return {"error": str(e)}


# retrive users data
@app.get("/getusers")
async def getusers():
  try:
      conn = get_connection()
      cursor = conn.cursor(dictionary= True)

      query = "select id,email,phone from users"
      cursor.execute(query)

      users = cursor.fetchall()

      cursor.close()
      conn.close()
      return {
            "users" : users
        }
  except Exception as e:
        return {"error": str(e)}
  

# retrive user data
@app.get("/getuser/{id}")
async def getusers(id: int):
  try:
      conn = get_connection()
      cursor = conn.cursor(dictionary= True)

      query = "SELECT id, email, phone FROM users WHERE id = %s"
      
      cursor.execute(query, (id,))

      user = cursor.fetchone()

      cursor.close()
      conn.close()
      if user is None:
            return {"message": "User not found"}

      return {"user": user}

  except Exception as e:
        return {"error": str(e)}

# @app.get("/posts")
# async def post():
#   return {"post" : "latest post"}