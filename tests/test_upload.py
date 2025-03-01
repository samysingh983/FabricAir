from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload():
    file = ("test.csv", "column1,column2\n1,2\n3,4\n".encode("utf-8"))
    response = client.post("/upload", files={"file": file})
    assert response.status_code == 200
    assert "file_id" in response.json()
