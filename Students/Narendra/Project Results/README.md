# Student Result Dashboard using FastAPI

This project is a web-based **Student Result Dashboard** built using **FastAPI**.  
It allows users to search student exam results using **Roll Number** and displays subject-wise marks in a memo format.

---

## Features

- Search student result using Roll Number
- Displays subject-wise marks
- Shows marks in figures and words
- Calculates Total and Percentage
- Shows PASS / FAIL status
- Shows Division (First / Second / Third)
- Print result option
- Data loaded from CSV file or Google Sheet
- Simple HTML dashboard
- Ready for deployment (Render compatible)

---

## Technologies Used

- Python
- FastAPI
- Pandas
- HTML
- Num2Words
- Uvicorn

---

## Project Structure

---

## CSV File Format

The CSV file should contain the following columns:
Roll_NO
Student_Name
School_Name
Date_of_Birth
Telugu
Hindi
English
Mathematics
Science
Social_Studies

---

## How it works

1. User enters Roll Number
2. FastAPI fetches student data from CSV
3. Calculates:

- Total marks
- Percentage
- Result (PASS / FAIL)
- Division

4. Displays formatted result memo
5. User can print or save as PDF

---

## Division Rules

| Division | Marks Range |
|----------|------------|
| First Division | 360 – 600 |
| Second Division | 300 – 359 |
| Third Division | 195 – 299 |
| Fail | Below 195 |

---

## Result Rules

Student must score minimum **35 marks in each subject** to PASS.

If any subject marks < 35 → FAIL

## Run Application

uvicorn main:app --reload

Open browser:

http://127.0.0.1:8000

---

## Sample Roll Numbers for Testing

If you need to check results, use the following Roll Numbers:

1001  
1100  
1200  
1300  
1400  
1500 