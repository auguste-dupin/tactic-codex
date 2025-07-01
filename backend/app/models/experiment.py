from sqlalchemy import Column, Integer, String, Text
from ..database import Base

class Experiment(Base):
    __tablename__ = 'experiments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
