from sqlalchemy import select
from backend.models import User
from core.database import async_session

async def create_user(telegram_id: int, name: str = None, email: str = None):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()

        if user is not None:
            if user.telegram_id != telegram_id:
                user.telegram_id = telegram_id
                await session.commit()
            return user
        else:
            user = User(
                telegram_id = telegram_id,
                name = name,
                email = email,
            )
            session.add(user)
            print(f"Новый пользователь ID:{telegram_id}")
            await session.commit()

async def add_name(telegram_id: int, name: str = None):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        
        if user.name is not None:
            return False
        else:
            user.name = name
            await session.commit()
            return user
        

async def add_email(telegram_id: int, email: str, is_registrated: bool = None):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()

        if user:
            user.email = email
            user.is_registrated = is_registrated
            await session.commit()
            return user
        

async def get_user(telegram_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        return user