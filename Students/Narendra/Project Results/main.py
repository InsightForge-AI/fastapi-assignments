from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pandas as pd
from num2words import num2words

app = FastAPI()


def load_data():

    df = pd.read_csv("data.csv")

    subjects = [
        "Telugu",
        "Hindi",
        "English",
        "Mathematics",
        "Science",
        "Social_Studies"
    ]

    df["Total"] = df[subjects].sum(axis=1)

    df["Percentage"] = (df["Total"] / 600 * 100).round(2)

    def result_status(row):

        for sub in subjects:

            if row[sub] < 35:
                return "FAIL"

        return "PASS"


    df["Result"] = df.apply(result_status, axis=1)


    def division(total):

        if total >= 360:
            return "FIRST DIVISION"

        elif total >= 300:
            return "SECOND DIVISION"

        elif total >= 195:
            return "THIRD DIVISION"

        else:
            return "FAIL"


    df["Division"] = df["Total"].apply(division)

    return df



@app.get("/", response_class=HTMLResponse)
def search():

    return """

    <html>

    <head>

    <title>Student Result</title>

    <style>

    body{
    font-family:Arial;
    text-align:center;
    margin-top:120px;
    background:#f2f2f2;
    }

    input{
    padding:12px;
    width:250px;
    font-size:16px;
    }

    button{
    padding:12px;
    background:#2c7be5;
    color:white;
    border:none;
    font-size:16px;
    }

    </style>

    </head>

    <body>

    <h2>SCHOOL EXAM RESULT</h2>

    <form action="/result" method="post">

    Enter Roll Number

    <br><br>

    <input name="roll_no" required>

    <br><br>

    <button>Search</button>

    </form>

    </body>

    </html>

    """



@app.post("/result", response_class=HTMLResponse)
def result(roll_no: int = Form(...)):

    df = load_data()

    student = df[df["Roll_NO"] == roll_no]

    if student.empty:

        return "<h3>Result not found</h3>"

    s = student.iloc[0]


    subjects = [
        ("FIRST LANGUAGE (TELUGU)", s.Telugu),
        ("SECOND LANGUAGE (HINDI)", s.Hindi),
        ("THIRD LANGUAGE (ENGLISH)", s.English),
        ("MATHEMATICS", s.Mathematics),
        ("GENERAL SCIENCE", s.Science),
        ("SOCIAL STUDIES", s.Social_Studies)
    ]


    rows = ""

    for subject, mark in subjects:

        color = "red" if mark < 35 else "black"

        rows += f"""

        <tr>

        <td>{subject}</td>

        <td style="color:{color}">{mark}</td>

        <td>{num2words(int(mark)).title()}</td>

        </tr>

        """


    total_words = num2words(int(s.Total)).title()

    result_color = "green" if s.Result == "PASS" else "red"



    return f"""

<html>

<head>

<style>

body{{
font-family:Arial;
background:#f2f2f2;
}}

.container{{
width:750px;
margin:auto;
background:white;
padding:40px;
}}

.title{{
text-align:center;
font-size:20px;
font-weight:bold;
}}

.info{{
margin-top:20px;
line-height:30px;
}}

table{{
width:100%;
border-collapse:collapse;
margin-top:20px;
}}

td,th{{
border:1px solid black;
padding:8px;
}}

th{{
background:#eee;
}}

.result{{
text-align:center;
margin-top:20px;
}}

.print-btn{{
text-align:center;
margin-top:25px;
}}

button{{
padding:10px 20px;
background:#28a745;
color:white;
border:none;
cursor:pointer;
}}

@media print {{

button{{
display:none;
}}

}}

</style>

</head>

<body>

<div class="container">

<div class="title">

MEMORANDUM OF SUBJECT-WISE MARKS

</div>

<div class="info">

<b>ROLL NUMBER :</b> {s.Roll_NO} <br>

<b>CANDIDATE NAME :</b> {s.Student_Name} <br>

<b>SCHOOL NAME :</b> {s.School_Name} <br>

<b>DATE OF BIRTH :</b> {s.Date_of_Birth}

</div>


<table>

<tr>

<th>SUBJECT</th>

<th>MARKS IN FIGURES</th>

<th>MARKS IN WORDS</th>

</tr>

{rows}


<tr>

<th>GRAND TOTAL</th>

<th>{s.Total}</th>

<th>{total_words}</th>

</tr>

</table>


<div class="result">

<h2 style="color:{result_color}">

RESULT : {s.Result}

</h2>

<h3>

DIVISION : {s.Division}

</h3>

</div>


<div class="print-btn">

<button onclick="window.print()">

Print Result

</button>

</div>


<br>

<div style="text-align:center">

<a href="/">Search Another</a>

</div>

</div>

</body>

</html>

"""