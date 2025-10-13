
from sqlalchemy import select
from backend.models import *
from core.database import async_session

async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        
        users = result.scalars().all()
        return users
    
if __name__ == "__main__":
    import asyncio
    users = asyncio.run(get_users())
    for user in users:
        print(f"ID: {user.user_id}, Telegram_id: {user.telegram_id}, Name: {user.name}, Registration: {user.is_registrated}")