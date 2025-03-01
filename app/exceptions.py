from fastapi import HTTPException

class FileNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="File not found")
