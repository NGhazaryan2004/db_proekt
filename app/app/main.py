from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from . import models, database

app = FastAPI()

@app.get("/states/")
def get_states(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return db.query(models.State).offset(skip).limit(limit).all()

@app.get("/population-info/")
def get_population_details(db: Session = Depends(database.get_db)):
    return db.query(
        models.Population.total_count,
        models.State.name.label("state_name"),
        models.Nationality.name.label("nationality_name")
    ).join(models.State).join(models.Nationality).all()

@app.get("/search-details/")
def search_json(regex: str, db: Session = Depends(database.get_db)):
    return db.query(models.State).filter(models.State.details.cast(String).op("~")(regex)).all()


@app.get("/stats/governance")
def get_gov_stats(db: Session = Depends(database.get_db)):
    from sqlalchemy import func
    return db.query(
        models.State.governance_type, 
        func.sum(models.Population.total_count)
    ).join(models.Population).group_by(models.State.governance_type).all()