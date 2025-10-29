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
    