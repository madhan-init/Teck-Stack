"""
FastAPI Dependency Injection

Depends() is used to provide a dependency to a path operation.

Common use cases:
1. Database connection
2. Authentication
3. Reusable logic
4. Common parameters
"""

from fastapi import FastAPI, Depends

app = FastAPI()


def common_parameters():
    return {
        "message": "This is a dependency"
    }


@app.get("/users")
def get_users(data=Depends(common_parameters)):
    return {
        "users": ["Madhan", "Arun"],
        "dependency": data
    }


@app.get("/protected")
def protected_route(token=Depends(verify_token)):
    return {
        "message": "Access granted",
        "token": token
    }