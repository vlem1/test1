from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    idAutor: int

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

    class Config:
        orm_mode = True
