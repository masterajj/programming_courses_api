from database.database_connection import DatabaseConnection
from database.data_models import Tag, Role
from sqlalchemy import text
import sqlalchemy as db


class SysDb(DatabaseConnection):
    def create_tag(self, tag: Tag):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertTag(:tag)")
            params = {
                "tag": tag.tag_name,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Tag created successfully!"}

    def create_role(self, role: Role):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertRole(:role_type)")
            params = {
                "role_type": role.role_type,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Role created successfully!"}

    def delete_tag(self, tag_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteTag(:tag_id)")
            connection.execute(procedure_call, {"tag_id": tag_id})
            connection.commit()
        return {"message": "Tag deleted successfully!"}

    def delete_role(self, role_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteRole(:role_id)")
            connection.execute(procedure_call, {"role_id": role_id})
            connection.commit()
        return {"message": "Role deleted successfully!"}
