from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship,backref
from db import Base


class Cluster(Base):
    __tablename__ = 'Cluster'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    # cluster = relationship('User', backref=backref('Cluster', cascade="save-update, merge, delete"))

