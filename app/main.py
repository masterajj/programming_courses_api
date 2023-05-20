from database_connection import DatabaseConnection
from data_models import User

from fastapi import FastAPI, Request, Response, status

app = FastAPI()

@app.get("/ready/")
async def ready_check():
    return Response(status_code=status.HTTP_200_OK, content="ok")

@app.get("/users")
async def get_users():
    db = DatabaseConnection()
    return db.get_users()

@app.post("/users/")
async def create_user(user: User):
    db = DatabaseConnection()
    return db.insert_users(user)