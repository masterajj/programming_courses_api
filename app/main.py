from fastapi import FastAPI, Request, Response, status
from routers import users, courses, api_system, forum

app = FastAPI()

@app.get("/ready/")
async def ready_check():
    return Response(status_code=status.HTTP_200_OK, content="ok")

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(forum.router)
app.include_router(api_system.router)