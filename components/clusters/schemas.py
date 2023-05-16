from pydantic import BaseModel


class Input(BaseModel):
    id: int
    name: str


class Cluster(BaseModel):
    name: str

    class Config:
        orm_mode = True

