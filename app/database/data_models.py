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

class Tag(BaseModel):
    tag_name: str

class Role(BaseModel):
    role_type: str

class ForumThread(BaseModel):
    name: str
    content: str

class RoleAssign(BaseModel):
    role_id: int
    user_id: int
