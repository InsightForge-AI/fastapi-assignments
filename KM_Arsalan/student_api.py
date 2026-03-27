from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector


# creating student model
class Student(BaseModel):
    s_name: str
    s_rno: str
    s_address: str
    s_phno: str
    s_email: str


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "welcome home"}

# DB connection
def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        database="fastapi",
        user="root",
        password="******"
    )

# post api for data storage
@app.post("/students")
async def create_student(st: Student):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO students (s_name, s_rno, s_address, s_phno, s_email)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            st.s_name,
            st.s_rno,
            st.s_address,
            st.s_phno,
            st.s_email
        ))

        conn.commit()

        cursor.close()
        conn.close()

        return {"message": "Student stored successfully"}

    except Exception as e:
        return {"error": str(e)}
    

# get api for single student
@app.get("/getstudent/{id}")
async def getstudents(id: int):
  try:
    
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT s_name, s_rno, s_address, s_phno, s_email FROM STUDENTS WHERE id = %s"
    cursor.execute(query,(id,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user is None:
        return {"message" : "user not found"}
    else:
        return {"user" : user}
  except Exception as e:
      return {"error" : str(e)}


# get api for all students


@app.get("/getstudents")
async def getstudent():
  try:
    
    conn = get_connection()
    cursor = conn.cursor()

    query = "select * from students"
    cursor.execute(query)

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    if users is None:
        return {"message" : "no users found"}
    else:
        return {"users" : users}
    
  except Exception as e:
     return {"error" : str(e)}