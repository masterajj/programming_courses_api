from fastapi import APIRouter
from database.forum_db import ForumDb
from database.data_models import ForumThread

router = APIRouter()

@router.post("/forum_thread/")
async def create_forum_thread(forum_thread: ForumThread):
    db = ForumDb()
    return db.create_forum_thread(forum_thread)