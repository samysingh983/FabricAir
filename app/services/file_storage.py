import pandas as pd
from fastapi import UploadFile, HTTPException
from uuid import uuid4

class FileStorage:
    """Handles file storage and retrieval."""
    data_store = {}

    @staticmethod
    def save_csv(file: UploadFile) -> str:
        file_id = str(uuid4())
        df = pd.read_csv(file.file)
        FileStorage.data_store[file_id] = df
        return file_id

    @staticmethod
    def get_file(file_id: str) -> pd.DataFrame:
        if file_id not in FileStorage.data_store:
            raise HTTPException(status_code=404, detail="File not found")
        return FileStorage.data_store[file_id]
