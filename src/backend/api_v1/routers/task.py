from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text

from typing import Optional

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

@router.get("/tasks/", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def get_tasks(
    task_id: Optional[int] = None,
    title: Optional[str] = None,
    session: AsyncSession = Depends(get_session_local)
):
    if title:
        result_title = await session.execute(
            select(Task).where(Task.title == title)
        )
        task = result_title.scalar_one_or_none()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Задача с таким названием не найдена"
            )
        return task
    
    elif task_id:
        result = await session.execute(
            select(Task).where(Task.task_id == task_id)
        )
        task = result.scalar_one_or_none()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Задача с таким id не найдена"
            )
        return task
    
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Необходимо ввести хотя бы один аргумент"
        )