from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskSchema(BaseModel):
    title: str = Field(..., description="Title task")
    description: str = Field(..., description="Description task")
    completed: bool = Field(default=False, description="Task status")
    category: str = Field(..., description="Task category")

class TaskCreate(TaskSchema):
    pass

class TaskResponse(TaskSchema):
    id: int

    class Config:
        from_attributes = True