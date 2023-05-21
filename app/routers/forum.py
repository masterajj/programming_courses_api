from fastapi import APIRouter
from database.forum_db import ForumDb
from database.data_models import ForumThread, ForumThreadComment

router = APIRouter()

@router.post("/forum_thread/")
async def create_forum_thread(forum_thread: ForumThread):
    db = ForumDb()
    return db.create_forum_thread(forum_thread)

@router.post("/forum_thread/comment")
async def insert_forum_thread_comment(forum_thread_comment: ForumThreadComment):
    db = ForumDb()
    return db.insert_forum_thread_comment(forum_thread_comment)

@router.delete("/forum_thread/{forum_thread_id}")
async def delete_forum_thread(forum_thread_id: int):
    db = ForumDb()
    return db.delete_forum_thread(forum_thread_id)

@router.delete("/forum_thread/comment/{comment_id}")
async def delete_forum_thread_comment(comment_id: int):
    db = ForumDb()
    return db.delete_forum_thread_comment(comment_id)