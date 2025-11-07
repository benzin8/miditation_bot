from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models import Task
from core.database import async_session

async def get_random_task() -> Task:
    async with async_session() as session:
        result = await session.execute(
            select(Task).order_by(func.random()).limit(1)
        )
        task = result.scalar_one_or_none()
        return task

async def execute_task(task_id):
    async with async_session() as session:
        result = await session.execute(
            select(Task).where(Task.task_id == task_id)
        )
        task = result.scalar_one_or_none()

        if task is None:
            raise f"Task {task_id} not found"

        task.complited = True
        await session.commit()
        return task