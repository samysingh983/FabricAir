from fastapi.testclient import TestClient
from app.main import app
from services.file_storage import data_store
import pandas as pd

client = TestClient(app)

def test_summary():
    # Create test data and save it in memory
    df = pd.DataFrame({"column1": [10, 20, 30], "column2": [40, 50, 60]})
    file_id = "test_summary_file"
    data_store[file_id] = df

    response = client.get(f"/summary/{file_id}")
    
    assert response.status_code == 200
    json_response = response.json()
    assert "summary" in json_response
    assert "column1" in json_response["summary"]
    assert "mean" in json_response["summary"]["column1"]
