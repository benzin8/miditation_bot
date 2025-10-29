from fastapi import FastAPI
from .routers import user, task

app = FastAPI()

app.include_router(user.router, prefix="/api/v1", tags=["users"])
app.include_router(task.router, prefix="/api/v1", tags=["tasks"])


@app.get("/")
async def root():
    return {"message": "Welcome to the User API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}