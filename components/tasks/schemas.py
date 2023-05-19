from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    name: str
    description: str
    idProject: int
    createData: datetime

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class TaskFeatures(BaseModel):
    id: int
    name: str
    description: str
    idProject: int
    createData: datetime

    class Config:
        orm_mode = True
