from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
import sqlalchemy as sa
from db import Base


class Task(Base):
    __tablename__ = 'Task'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    idProject = Column(Integer, ForeignKey("Project.id"), index=True)

