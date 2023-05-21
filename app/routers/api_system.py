from fastapi import APIRouter
from database.sys_db import SysDb
from database.data_models import Tag, Role

router = APIRouter()

@router.post("/tags/")
async def create_tag(tag: Tag):
    db = SysDb()
    return db.create_tag(tag)

@router.post("/roles/")
async def create_role(role: Role):
    db = SysDb()
    return db.create_role(role)