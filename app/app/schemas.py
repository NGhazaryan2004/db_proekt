from pydantic import BaseModel
from typing import Optional, Dict, Any


class StateBase(BaseModel):
    name: str
    capital: str
    governance_type: str
    details: Optional[Dict[str, Any]] = None  


class StateCreate(StateBase):
    pass

class StateOut(StateBase):
    id: int
    class Config:
        from_attributes = True

class PopulationBase(BaseModel):
    state_id: int
    nationality_id: int
    male_count: int
    female_count: int
    total_count: int

class PopulationCreate(PopulationBase):
    pass

class PopulationOut(PopulationBase):
    id: int
    class Config:
        from_attributes = True