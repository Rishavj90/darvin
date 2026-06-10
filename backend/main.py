from fastapi import FastAPI
from backend.api import router
from pathlib import Path

Path('./tmp_files').mkdir(exist_ok=True)
Path('./chromaDB').mkdir(exist_ok=True)

app=FastAPI()
app.include_router(router)
