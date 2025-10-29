from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.models import Task
from backend.schemas.task_schema import TaskCreate, TaskResponse
from core.database import get_session_local

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    session: AsyncSession = Depends(get_session_local)
):
    print("Создание задачи с данными:", task_data)
    existing_task = await session.execute(
        select(Task).where(Task.title == task_data.title)
    )
    if existing_task.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Задача с таким названием уже существует."
        )
    task = Task(**task_data.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task