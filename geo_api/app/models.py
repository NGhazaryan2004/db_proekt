from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from .database import Base

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    capital = Column(String)
    government_type = Column(String)

    populations = relationship("Population", back_populates="state")


class Nationality(Base):
    __tablename__ = "nationalities"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    total_population = Column(Integer)
    meta = Column(JSONB)  # 🔥 JSON поле (понадобится позже)

    populations = relationship("Population", back_populates="nationality")


class Population(Base):
    __tablename__ = "population"

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey("states.id"))
    nationality_id = Column(Integer, ForeignKey("nationalities.id"))
    male = Column(Integer)
    female = Column(Integer)
    total = Column(Integer)

    state = relationship("State", back_populates="populations")
    nationality = relationship("Nationality", back_populates="populations")
