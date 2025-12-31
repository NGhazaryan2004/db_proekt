from sqlalchemy.orm import Session
from . import models, schemas

def create_state(db: Session, state: schemas.StateCreate):
    db_state = models.State(**state.model_dump())
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

def get_states(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.State).offset(skip).limit(limit).all()

def update_governance_by_detail(db: Session, detail_key: str, value: str, new_gov: str):
    targets = db.query(models.State).filter(models.State.details[detail_key].astext == value)
    count = targets.update({models.State.governance_type: new_gov}, synchronize_session=False)
    db.commit()
    return count