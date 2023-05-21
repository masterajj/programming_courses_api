from database.database_connection import DatabaseConnection
from database.data_models import ForumThread
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