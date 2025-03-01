from fastapi import FastAPI
from app.routes import upload, summary, transform, visualize

app = FastAPI()

# Include routes
app.include_router(upload.router)
app.include_router(summary.router)
app.include_router(transform.router)
app.include_router(visualize.router)
