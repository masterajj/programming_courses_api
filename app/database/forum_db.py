from database.database_connection import DatabaseConnection
from database.data_models import ForumThread, ForumThreadComment, UserForumThreadComment
from sqlalchemy import text

class ForumDb(DatabaseConnection):
    def create_forum_thread(self, forum_thread: ForumThread) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertForumThread(:name, :content)")
            params = {
                'name': forum_thread.name,
                'content': forum_thread.content,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Forum Thread created successfully!"}
    
    def insert_forum_thread_comment(self, forum_thread_comment: ForumThreadComment) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertForumThreadComment(:content, :thread_id)")
            params = {
                'content': forum_thread_comment.content,
                'thread_id': forum_thread_comment.thread_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Forum Thread Comment added successfully!"}
    
    def assign_user_forum_thread_comment(self, user_forum_thread_comment: UserForumThreadComment) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserForumThreadComment(:user_id, :comment_id, :thread_id)")
            params = {
                'user_id': user_forum_thread_comment.user_id,
                'comment_id': user_forum_thread_comment.comment_id,
                'thread_id': user_forum_thread_comment.thread_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Forum Thread Comment assigned to User successfully!"}