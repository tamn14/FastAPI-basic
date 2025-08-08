from fastapi import FastAPI ,Path
from typing import Optional , List
from pip._internal.network import auth
from pydantic import BaseModel
from Api import users , course  , session

app = FastAPI()

app.include_router(users.router)
app.include_router(course.router)
app.include_router(session.router)






