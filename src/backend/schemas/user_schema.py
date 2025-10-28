from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    telegram_id: int = Field(..., description="Telegram ID")
    name: Optional[str] = Field(None, description="User name")
    email: Optional[str] = Field(None, description="User email")
    is_registrated: Optional[bool] = Field(False, description="Registration status")

class UserCreate(UserSchema):
    pass

class UserResponse(UserSchema):
    user_id: int

    class Config:
        from_attributes = True