from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.models import User
from backend.schemas.user_schema import UserCreate, UserResponse
from core.database import get_session_local


router = APIRouter()

@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    session: AsyncSession = Depends(get_session_local)
):
    existing_user = await session.execute(
        select(User).where(User.telegram_id == user_data.telegram_id)
    )
    if existing_user.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким Telegram ID уже существует."
        )
    
    user = User(**user_data.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@router.get("/users/{telegram_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user(
    telegram_id: int,
    session: AsyncSession = Depends(get_session_local)
):
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден."
        )
    return user