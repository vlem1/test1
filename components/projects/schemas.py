from pydantic import BaseModel
from datetime import datetime


class Project(BaseModel):
    name: str
    description: str
    idAutor: int
    createData: datetime

    class Config:
        orm_mode = True


class ProjectUpdate(BaseModel):
    name: str
    idAutor: int

    class Config:
        orm_mode = True


class ProjectFeatures(BaseModel):
    id: int
    name: str
    description: str
    idAutor: int
    createData: datetime

    class Config:
        orm_mode = True


class UserFromProject(BaseModel):
    name: str
    surname: str
    login: str
    passwordHash: str
    idRole: int
    position: str
    idCluster: int
    markingDeletion: bool
    createData: datetime

    class Config:
        orm_mode = True
