# FastAPI Learning Journey – Day 1 to Day 6

This repository documents my hands-on learning of **FastAPI**, API development, testing, and GitHub workflow over 6 days.

---

## 📅 Day 1 – Introduction to API + FastAPI Setup

**Topics Covered:**

* What is an API
* REST API basics
* FastAPI introduction
* Installing FastAPI & Uvicorn
* Creating first FastAPI application

**Task Completed:**

* Created basic FastAPI app
* Implemented endpoints:

  * `/` → Welcome message
  * `/hello` → Hello response

**Outcome:**

* Successfully ran FastAPI server using `uvicorn`
* Verified endpoints in browser

---

## 📅 Day 2 – GET APIs

**Topics Covered:**

* Query parameters
* GET request handling
* Returning dynamic responses

**Task Completed:**

* Created GET APIs:

  * `/greet?name=YourName`
  * `/add?a=5&b=10`

**Outcome:**

* Learned how to accept inputs via URL
* Implemented simple calculation API

---

## 📅 Day 3 – POST APIs

**Topics Covered:**

* POST request
* Request body
* Pydantic models
* JSON input handling

**Task Completed:**

* Created POST API to accept:

  * `name`
  * `age`
* Returned structured JSON response

**Outcome:**

* Learned data validation using Pydantic
* Built first POST API

---

## 📅 Day 4 – Postman Testing

**Topics Covered:**

* Introduction to Postman
* Sending GET requests
* Sending POST requests
* JSON body testing

**Task Completed:**

* Tested all APIs in Postman
* Verified responses for:

  * GET APIs
  * POST APIs

**Outcome:**

* Learned API testing workflow
* Verified endpoints independently

---

## 📅 Day 5 – Mini Project (Todo API)

**Project Built:** Todo API

**Features Implemented:**

* Get all todos
* Create new todo
* Update todo
* Delete todo
* Method not allowed handling

**Outcome:**

* Built a complete CRUD API
* Structured FastAPI project
* Tested using Postman

---

## 📅 Day 6 – GitHub Workflow (Push & Pull Request)

**Topics Covered:**

* Git basics
* GitHub repository
* Branch creation
* Commit & Push
* Pull Request creation

**Steps Followed:**

1. Initialized git repository

```
git init
```

2. Added files

```
git add .
```

3. Committed changes

```
git commit -m "Added FastAPI Day 1 to Day 5 tasks"
```

4. Created new branch

```
git checkout -b feature/fastapi-learning
```

5. Pushed project to GitHub

```
git push origin feature/fastapi-learning
```

6. Created Pull Request

* Opened GitHub repository
* Clicked **Compare & Pull Request**
* Added description of changes
* Submitted Pull Request

**Outcome:**

* Successfully pushed project to GitHub
* Created Pull Request for review
* Learned GitHub collaboration workflow

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Postman
* Git
* GitHub

---

## 🎯 Learning Outcome

* Understood API fundamentals
* Built GET & POST APIs
* Tested APIs using Postman
* Developed mini Todo API project
* Learned GitHub workflow with Pull Requests


