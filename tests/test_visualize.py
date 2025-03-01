from fastapi.testclient import TestClient
from app.main import app
from services.file_storage import data_store
import pandas as pd

client = TestClient(app)

def test_visualization():
    # Create test data
    df = pd.DataFrame({"column1": [1, 2, 3, 4, 5], "column2": [10, 20, 30, 40, 50]})
    file_id = "test_visual_file"
    data_store[file_id] = df

    params = {
        "chart_type": "scatter",
        "columns": ["column1", "column2"]
    }

    response = client.get(f"/visualize/{file_id}", params=params)
    
    assert response.status_code == 200
    json_response = response.json()
    assert "image_path" in json_response
