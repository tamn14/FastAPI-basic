import fastapi
from typing import Optional , List
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []
class User(BaseModel):
    email: str
    is_active: bool
    bio : Optional[str]


@router.get("/users" , response_model=List[User])
async def get_users():
    return users

@router.post("/users")
def create_user(user: User):
    users.append(user)
    return users

@router.get("/user/{id}")
async def get_user(id : int):
    return users[id]