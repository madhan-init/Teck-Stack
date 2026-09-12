"""
FastAPI Responses

1. Returning JSON
2. Response Models
3. Status Codes
    200 → OK
    201 → Created
    204 → No Content
    400 → Bad Request
    401 → Unauthorized
    403 → Forbidden
    404 → Not Found
    500 → Internal Server Error
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.get("/hello", status_code=status.HTTP_200_OK)
def hello():
    return {
        "message": "Hello World",
        "status": "success"
    }


@app.get("/user", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user():
    return {
        "id": 1,
        "name": "Madhan",
        "email": "madhan@example.com"
    }


@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created successfully"
    }


@app.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return None