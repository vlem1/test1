from sqlalchemy import Column, Integer, String

from db import Base


class Cluster(Base):
    __tablename__ = 'Cluster'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)

