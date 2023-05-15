from pydantic import BaseModel


class Input(BaseModel):
    id: int
    name: str


class UserBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    surname: str
    login: str
    password: str
    idRole: int
    position: str
    idCluster: int

    class Config:
        orm_mode = True


class AddNewUser(BaseModel):
    name: str
    surname: str
    idRole: int
    position: str
    login: str
    passwordHash: str
    idCluster: int
    markingDeletion: bool

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str
    surname: str

    class Config:
        orm_mode = True


class ValuesFromIdRole(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class UserFeatures(BaseModel):
    id: str
    name: str
    surname: str
    idRole: int
    position: str
    login: str
    passwordHash: str
    idCluster: int
    markingDeletion: bool

    class Config:
        orm_mode = True

