"""
Pydantic BaseModel in FastAPI

BaseModel is used to define the structure and data types
of the data that an API expects.

FastAPI automatically validates the incoming data
based on the Pydantic model.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Define the request body structure
class User(BaseModel):
    name: str
    age: int
    email: str


# POST request using Pydantic model
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "name": user.name,
        "age": user.age,
        "email": user.email
    }