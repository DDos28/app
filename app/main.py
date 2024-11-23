from fastapi import FastAPI
from fastapi.routing import APIRouter
from routers import user, task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)