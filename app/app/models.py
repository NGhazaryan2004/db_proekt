from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from .database import Base

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    capital = Column(String)
    governance_type = Column(String)
    # Пункт 6: JSON поле
    details = Column(JSONB) 

class Nationality(Base):
    __tablename__ = "nationalities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    language = Column(String)

class Population(Base):
    __tablename__ = "populations"
    id = Column(Integer, primary_key=True, index=True)
    state_id = Column(Integer, ForeignKey("states.id"))
    nationality_id = Column(Integer, ForeignKey("nationalities.id"))
    male_count = Column(Integer)
    female_count = Column(Integer)
    total_count = Column(Integer)

    state = relationship("State")
    nationality = relationship("Nationality")