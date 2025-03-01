from fastapi import APIRouter, HTTPException
from app.services.file_storage import FileStorage
from app.services.data_processor import DataProcessor

router = APIRouter()

@router.get("/summary/{file_id}")
def get_summary(file_id: str):
    df = FileStorage.get_file(file_id)
    if df is None:
        raise HTTPException(status_code=404, detail="File not found")
    return DataProcessor.get_summary(df)
