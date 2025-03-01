from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.services.file_storage import FileStorage
from app.services.data_processor import DataProcessor

router = APIRouter()

@router.get("/visualize/{file_id}")
def visualize_data(file_id: str, chart_type: str = Query(...), columns: List[str] = Query(...)):
    df = FileStorage.get_file(file_id)
    if df is None:
        raise HTTPException(status_code=404, detail="File not found")
    image_path = DataProcessor.generate_visualization(df, chart_type, columns)
    return {"message": "Visualization generated successfully", "image_path": image_path}
