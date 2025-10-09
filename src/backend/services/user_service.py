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

