from fastapi.testclient import TestClient
from app.main import app
from services.file_storage import data_store
import pandas as pd

client = TestClient(app)

def test_transform():
    # Create test data
    df = pd.DataFrame({"column1": [1, 2, 3], "column2": [None, 5, 6]})
    file_id = "test_transform_file"
    data_store[file_id] = df

    transformations = {
        "normalize": ["column1"],
        "fill_missing": {"column2": 0}
    }

    response = client.post(f"/transform/{file_id}", json=transformations)
    
    assert response.status_code == 200
    assert "file_id" in response.json()

    new_file_id = response.json()["file_id"]
    assert new_file_id in data_store
    assert data_store[new_file_id]["column2"].isnull().sum() == 0  # Ensure missing values are filled
