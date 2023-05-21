from database.database_connection import DatabaseConnection
from database.data_models import User, RoleAssign, UserProgress, UserSession, UserCourse, UserTest, UserAssignments, Certificate, UserForumThread
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
    
    def insert_user_progress(self, user_progress: UserProgress):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserProgress(:courses_completed, :user_id)")
            params = {
                'courses_completed': user_progress.courses_completed,
                'user_id': user_progress.user_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Progress inserted successfully!"}

    def insert_user_session(self, user_session: UserSession):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertSession(:session_start, :session_end, :user_id)")
            params = {
                'session_start': user_session.session_start,
                'session_end': user_session.session_end,
                'user_id': user_session.user_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Session inserted successfully!"}
    
    def assign_user_course(self, user_course: UserCourse):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserCourse(:course_id, :user_id)")
            params = {
                'course_id': user_course.course_id,
                'user_id': user_course.user_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Course assigned successfully!"}
    
    def assign_user_test(self, user_test: UserTest):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserTests(:user_id, :course_id, :test_id)")
            params = {
                'user_id': user_test.user_id,
                'course_id': user_test.course_id,
                'test_id': user_test.test_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Test assigned successfully!"}
    
    def assign_user_assignment(self, user_assignment: UserAssignments):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserAssignments(:user_id, :assignment_id, :lecture_id, :course_id)")
            params = {
                'user_id': user_assignment.user_id,
                'assignment_id': user_assignment.assignment_id,
                'lecture_id': user_assignment.lecture_id,
                'course_id': user_assignment.course_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Assignment assigned successfully!"}
    
    def create_certificate(self, certificate: Certificate):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertCertificate(:certificate, :user_id, :course_id)")
            params = {
                'certificate': certificate.certificate,
                'user_id': certificate.user_id,
                'course_id': certificate.course_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Created certificate successfully!"}
    
    def assign_user_forum_thread(self, user_forum_thread: UserForumThread):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertCertificate(:certificate, :user_id, :course_id)")
            params = {
                'user_id': user_forum_thread.user_id,
                'thread_id': user_forum_thread.thread_id,
            } 
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User forum thread assigned successfully!"}
    
    def delete_user(self, user_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteUser(:user_id)")
            connection.execute(procedure_call, {'user_id': user_id})
            connection.commit()
        return {"message": "User deleted successfully!"}        
      