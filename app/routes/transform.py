from fastapi import APIRouter
from app.services.file_storage import FileStorage
from app.services.data_processor import DataProcessor
from typing import Dict
from uuid import uuid4

router = APIRouter()

@router.post("/transform/{file_id}")
def transform_data(file_id: str, transformations: Dict):
    df = FileStorage.get_file(file_id)
    new_df = DataProcessor.transform_data(df, transformations)
    new_file_id = str(uuid4())
    FileStorage.data_store[new_file_id] = new_df
    return {"message": "Transformations applied successfully", "file_id": new_file_id}
