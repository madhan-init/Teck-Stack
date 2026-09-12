from fastapi import FastAPI

app = FastAPI()

# GET - Read data
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": "Getting user", "user_id": user_id}


# POST - Create new data
@app.post("/users")
def create_user(name: str, age: int):
    return {
        "message": "User created",
        "name": name,
        "age": age
    }


# PUT - Update existing data
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, age: int):
    return {
        "message": "User updated",
        "user_id": user_id,
        "name": name,
        "age": age
    }


# DELETE - Delete data
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted",
        "user_id": user_id
    }