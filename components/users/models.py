from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, MetaData
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from db import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    idRole = Column(Integer, ForeignKey("Role.id"))
    position = Column(String)
    login = Column(String, nullable=False)
    passwordHash = Column(String, nullable=False)
    idCluster = Column(Integer, ForeignKey("Cluster.id"))
    markingDeletion = Column(Boolean, nullable=False)
    createData = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    users_project = relationship('Project', backref=backref('User', cascade="save-update, merge, delete"))
