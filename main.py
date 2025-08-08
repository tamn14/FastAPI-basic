from fastapi import FastAPI ,Path
from typing import Optional , List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio : Optional[str]


@app.get("/users" , response_model=List[User])
async def get_users():
    return users

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return users

@app.get("/user/{id}")
async def get_user(
        id : int = Path(..., description="The Id of the user you want to get")):
    return users[id]