from fastapi import APIRouter
from database.users_db import UsersDb
from database.data_models import User, RoleAssign, UserProgress, UserSession, UserCourse, UserTest, UserAssignments, Certificate, UserForumThread

router = APIRouter()

@router.get("/users")
async def get_users():
    db = UsersDb()
    return db.get_users()

@router.post("/users/")
async def create_user(user: User):
    db = UsersDb()
    return db.insert_users(user)

@router.post("/users/role/")
async def assign_user_role(user_role_id: RoleAssign):
    db = UsersDb()
    return db.assign_user_role(user_role_id)

@router.post("/users/user_progress/")
async def insert_user_progress(user_progress: UserProgress):
    db = UsersDb()
    return db.insert_user_progress(user_progress)

@router.post("/users/user_session/")
async def insert_user_session(user_session: UserSession):
    db = UsersDb()
    return db.insert_user_session(user_session)

@router.post("/users/course/")
async def assign_user_course(user_course: UserCourse):
    db = UsersDb()
    return db.assign_user_course(user_course)

@router.post("/users/course/test")
async def assign_user_test(user_test: UserTest):
    db = UsersDb()
    return db.assign_user_test(user_test)

@router.post("/users/course/assignment")
async def assign_user_assignment(user_assignment: UserAssignments):
    db = UsersDb()
    return db.assign_user_assignment(user_assignment)

@router.post("/users/certificate")
async def create_certificate(certificate: Certificate):
    db = UsersDb()
    return db.assign_user_assignment(certificate)

@router.post("/users/forum_thread")
async def assign_user_forum_thread(user_forum_thread: UserForumThread):
    db = UsersDb()
    return db.assign_user_forum_thread(user_forum_thread)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    db = UsersDb()
    return db.delete_user(user_id)