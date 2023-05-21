from database.database_connection import DatabaseConnection
from database.data_models import Course
import sqlalchemy as db
from sqlalchemy import text

class CoursesDb(DatabaseConnection):
    def get_courses(self) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("courses", self.metadata, autoload_with=connection)
            query = db.select(my_table)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def create_course(self, course: Course) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertCourse(:course_name, :creation_date, :update_date, :description, :level)")
            params = {
                'course_name': course.course_name,
                'creation_date': course.creation_date,
                'update_date': course.update_date,
                'description': course.description,
                'level': course.level
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Course created successfully!"}