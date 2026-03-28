# Day 4: Postman Testing & API Validation

This phase of the sprint focuses on rigorous testing of the FastAPI endpoints developed during Day 2 and Day 3. Using **Postman**, we verify the request-response cycle, status codes, and data validation logic.

## API Status Report
All endpoints developed in the previous sessions have been tested and are **working as expected**:
- **GET Endpoints**: Operational with correct query parameter handling.
- **POST Endpoints**: Successfully validating JSON payloads using Pydantic models.

## Test Evidence
Screenshots demonstrating successful API calls and status codes have been added to this directory for reference. These images confirm that the server returns the correct data structures and HTTP 201/200 codes.

## How to Test

### 1. Initialize the Application
Navigate to your project directory and start the Uvicorn server:
```bash
uvicorn app:app --reload
```

### 2. Testing in Postman

#### GET Requests (Testing Day 2)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/add?a=10&b=20`
- **Action**: Click **Send**.
- **Expected Result**: `{"result": 30}`

#### POST Requests (Testing Day 3)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/user`
- **Body Tab**: Select `raw` and then `JSON` from the dropdown.
- **Payload**:
  ```json
  {
    "name": "Vineeth",
    "age": 25
  }
  ```
- **Action**: Click **Send**.
- **Expected Result**: 
  - **Status**: `201 Created`
  - **Body**: `{"message": "User Vineeth created successfully", "age": 25}`

## Conclusion
Using Postman helps verify that our Pydantic models (Day 3) are correctly validating incoming data and that our logic (Day 2) returns the correct output for different inputs.