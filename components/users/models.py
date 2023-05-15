from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from db import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    idRole = Column(Integer, ForeignKey("Role.id"), nullable=False)
    position = Column(String)
    login = Column(String, nullable=False)
    passwordHash = Column(String, nullable=False)
    idCluster = Column(Integer)
    markingDeletion = Column(Boolean, nullable=False)






