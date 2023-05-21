from fastapi import APIRouter
from database.forum_db import ForumDb
from database.data_models import ForumThread, ForumThreadComment, UserForumThreadComment

router = APIRouter()

@router.post("/forum_thread/")
async def create_forum_thread(forum_thread: ForumThread):
    db = ForumDb()
    return db.create_forum_thread(forum_thread)

@router.post("/forum_thread/comment")
async def insert_forum_thread_comment(forum_thread_comment: ForumThreadComment):
    db = ForumDb()
    return db.insert_forum_thread_comment(forum_thread_comment)

@router.post("/forum_thread/comment/user")
async def assign_user_forum_thread_comment(user_forum_thread_comment: UserForumThreadComment):
    db = ForumDb()
    return db.assign_user_forum_thread_comment(user_forum_thread_comment)