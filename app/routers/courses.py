from fastapi import APIRouter
from database.courses_db import CoursesDb
from database.data_models import Course, CourseRating, CourseComment, CourseFaq, CourseTagAssign, Lecture, Assignment, Test

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

@router.post("/courses/lectures/tests")
async def create_test(test: Test):
    db = CoursesDb()
    return db.create_test(test)

@router.delete("/courses/{course_id}")
async def delete_user(course_id: int):
    db = CoursesDb()
    return db.delete_course(course_id)

@router.delete("/courses/{course_id}/users/{user_id}/ratings")
async def delete_rating(course_id: int, user_id: int):
    db = CoursesDb()
    return db.delete_rating(course_id, user_id)

@router.delete("/courses/{course_id}/users/{user_id}/comments")
async def delete_comment(course_id: int, user_id: int):
    db = CoursesDb()
    return db.delete_comment(course_id, user_id)

@router.delete("/courses/faq/{faq_id}/")
async def delete_course_faq(faq_id: int):
    db = CoursesDb()
    return db.delete_course_faq(faq_id)

@router.delete("/courses/{course_id}/tags/{tag_id}/")
async def delete_course_tag(course_id: int, tag_id: int):
    db = CoursesDb()
    return db.delete_course_tag(course_id, tag_id)

@router.delete("/courses/lectures/{lecture_id}/")
async def delete_lecture(lecture_id: int):
    db = CoursesDb()
    return db.delete_lecture(lecture_id)

@router.delete("/courses/tests/{test_id}/")
async def delete_test(test_id: int):
    db = CoursesDb()
    return db.delete_test(test_id)

@router.delete("/courses/assignments/{assignment_id}/")
async def delete_assignment(assignment_id: int):
    db = CoursesDb()
    return db.delete_assignment(assignment_id)