import requests
import random


gov_types = ["Republic", "Monarchy", "Federation"]
languages = ["English", "Russian", "Armenian", "Spanish"]

def populate():
    
    for i in range(5):
        nat = {"name": f"Nationality_{i}", "language": random.choice(languages)}
        requests.post("http://localhost:8000/nationalities/", json=nat)

   
    for i in range(100):
        state = {
            "name": f"Country_{i}",
            "capital": f"Capital_{i}",
            "governance_type": random.choice(gov_types),
            "details": {
                "climate": random.choice(["tropical", "temperate", "arctic"]),
                "population_density": random.randint(10, 500),
                "description": "Historical data about " + f"Country_{i}"
            }
        }
        requests.post("http://localhost:8000/states/", json=state)