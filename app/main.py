from fastapi import FastAPI, Request, Response, status
from routers import users, courses

app = FastAPI()

@app.get("/ready/")
async def ready_check():
    return Response(status_code=status.HTTP_200_OK, content="ok")

app.include_router(users.router)
app.include_router(courses.router)