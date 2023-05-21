from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    country: str

class Course(BaseModel):
    course_name: str
    creation_date: datetime
    update_date: datetime
    description: str
    level: str
