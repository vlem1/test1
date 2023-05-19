from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from datetime import datetime
from db import Base


class Task(Base):
    __tablename__ = 'Task'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    createData = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    idProject = Column(Integer, ForeignKey("Project.id"), index=True)

