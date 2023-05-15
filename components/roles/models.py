from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from db import Base


class Role(Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    description = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=True)

