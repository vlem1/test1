from pydantic import BaseModel


class Input(BaseModel):
    id: int
    name: str


class AddNewRole(BaseModel):
    description: str
    name: str

    class Config:
        orm_mode = True


class RoleUpdate(BaseModel):
    description: str
    name: str

    class Config:
        orm_mode = True


class Role(BaseModel):
    description: str
    name: str

    class Config:
        orm_mode = True


class RoleFeatures(BaseModel):
    id: int
    description: str
    name: str

    class Config:
        orm_mode = True
