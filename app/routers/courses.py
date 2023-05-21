from fastapi import APIRouter
from database.courses_db import CoursesDb
from database.data_models import Course

router = APIRouter()

@router.get("/courses")
async def get_courses():
    db = CoursesDb()
    return db.get_courses()

@router.post("/courses/")
async def create_course(course: Course):
    db = CoursesDb()
    return db.create_course(course)