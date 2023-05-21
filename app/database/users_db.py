from database.database_connection import DatabaseConnection
from database.data_models import User, RoleAssign
import sqlalchemy as db
from sqlalchemy import text

class UsersDb(DatabaseConnection):
    def get_users(self) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("users", self.metadata, autoload_with=connection)
            query = db.select(my_table)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]
          
    def insert_users(self, user: User) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUser(:username, :password, :email, :country)")
            params = {
                'username': user.username,
                'password': user.password,
                'email': user.email,
                'country': user.country
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User created successfully!"}
    
    def assign_user_role(self, user_role_id: RoleAssign):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserRole(:role_id, :user_id)")
            params = {
                'role_id': user_role_id.role_id,
                'user_id': user_role_id.user_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Role assigned successfully!"}