from fastapi import APIRouter
from database.courses_db import CoursesDb
from database.data_models import Course, CourseRating, CourseComment, CourseFaq, CourseTagAssign, Lecture, Assignment

router = APIRouter()

@router.get("/courses")
async def get_courses():
    db = CoursesDb()
    return db.get_courses()

@router.post("/courses/")
async def create_course(course: Course):
    db = CoursesDb()
    return db.create_course(course)

@router.post("/courses/rating")
async def rate_course(course_rating: CourseRating):
    db = CoursesDb()
    return db.rate_course(course_rating)

@router.post("/courses/comment")
async def comment_course(course_comment: CourseComment):
    db = CoursesDb()
    return db.comment_course(course_comment)

@router.post("/courses/faq")
async def create_course_faq(course_faq: CourseFaq):
    db = CoursesDb()
    return db.create_course_faq(course_faq)

@router.post("/courses/tag")
async def assign_course_tag(assign_course_tag: CourseTagAssign):
    db = CoursesDb()
    return db.assign_course_tag(assign_course_tag)

@router.post("/courses/lectures")
async def create_lecture(lecture: Lecture):
    db = CoursesDb()
    return db.create_lecture(lecture)

@router.post("/courses/lectures/assignments")
async def create_assignment(assingment: Assignment):
    db = CoursesDb()
    return db.create_assignment(assingment)