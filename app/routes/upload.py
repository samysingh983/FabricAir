from fastapi import APIRouter, UploadFile, File
from app.services.file_storage import FileStorage

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_id = FileStorage.save_csv(file)
    return {"message": "File uploaded successfully", "file_id": file_id}
