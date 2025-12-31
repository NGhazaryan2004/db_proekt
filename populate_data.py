import requests

API_URL = "http://localhost:8000"

def fill_data():
    state_data = {
        "name": "France", 
        "capital": "Paris", 
        "governance_type": "Republic",
        "details": {"climate": "temperate", "continent": "Europe"}
    }
    requests.post(f"{API_URL}/states/", json=state_data)
    
    print("Данные успешно загружены через API")

if __name__ == "__main__":
    fill_data()