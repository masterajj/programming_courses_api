from fastapi import APIRouter
from database.users_db import UsersDb
from database.data_models import User

router = APIRouter()

@router.get("/users")
async def get_users():
    db = UsersDb()
    return db.get_users()

@router.post("/users/")
async def create_user(user: User):
    db = UsersDb()
    return db.insert_users(user)