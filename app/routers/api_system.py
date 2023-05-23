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


@router.delete("/tags/{tag_id}")
async def delete_tag(tag_id: int):
    db = SysDb()
    return db.delete_tag(tag_id)


@router.delete("/roles/{role_id}")
async def delete_role(role_id: int):
    db = SysDb()
    return db.delete_role(role_id)
