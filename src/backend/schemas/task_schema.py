from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskSchema(BaseModel):
    title: str = Field(..., description="Title task")
    description: str = Field(..., description="Description task")
    complited: bool = Field(default=False, description="Task status")
    category: str = Field(..., description="Task category")

class TaskCreate(TaskSchema):
    pass

class TaskResponse(TaskSchema):
    id: int = Field(..., alias="task_id")

    class Config:
        from_attributes = True