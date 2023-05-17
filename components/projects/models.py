from sqlalchemy import Column, ForeignKey, Integer, String

from db import Base


class Project(Base):
    __tablename__ = 'Project'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    idAutor = Column(Integer, ForeignKey("User.id"), nullable=False)







