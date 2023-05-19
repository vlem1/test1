from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str
    idProject: int

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

    class Config:
        orm_mode = True
