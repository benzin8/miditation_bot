from sqlalchemy import Column, Integer, String, Float, Text, BigInteger
from backend.models.base import Base

class Task(Base):
    __tablename__ = "tasks"

    taks_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    task_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Task task_id= {self.taks_id}, task_name= {self.taks_name} added>"