from fastapi import APIRouter
from database.users_db import UsersDb
from database.data_models import User, RoleAssign

router = APIRouter()

@router.get("/users")
async def get_users():
    db = UsersDb()
    return db.get_users()

@router.post("/users/")
async def create_user(user: User):
    db = UsersDb()
    return db.insert_users(user)

@router.post("/assign_role/")
async def assign_user_role(user_role_id: RoleAssign):
    db = UsersDb()
    return db.assign_user_role(user_role_id)