from sqlalchemy import Column, Integer, String, Float, Text, BigInteger, Boolean
from backend.models.base import Base
from dataclasses import dataclass

@dataclass  
class Task(Base):
    __tablename__ = "tasks"

    taks_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    complited = Column(Boolean, default=False)
    category = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Task task_id= {self.taks_id}, title= {self.title} added>"