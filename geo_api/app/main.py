from fastapi import FastAPI
from db import conn
import json

app = FastAPI()

@app.post("/states")
def create_state(name: str, capital: str, government_type: str):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO states (name, capital, government_type) VALUES (%s,%s,%s)",
        (name, capital, government_type)
    )
    conn.commit()
    return {"status": "created"}
