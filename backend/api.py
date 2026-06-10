from backend.ingestion.parse import parse_pdf
from backend.ingestion.chunk import chunk_pages
from backend.ingestion.store import store_chunks
import backend.query.memory as mem
from backend.query.result import ask
from fastapi import APIRouter, UploadFile, HTTPException
from pydantic import BaseModel
from pathlib import Path

router = APIRouter()

class Prompt(BaseModel):
    query:str
    history : list

@router.post('/upload')
async def upload_pdf(file : UploadFile):
    try:
        name=file.filename
        file_ext = Path(name).suffix.lower()
        if file_ext != ".pdf":
            raise HTTPException(status_code=400, detail="upload a pdf") 
        
        content = await file.read()
        with open(f'./tmp_files/{name}', 'wb') as fl:
            fl.write(content)
        
        pages= parse_pdf(f'./tmp_files/{name}')
        chunks= chunk_pages(pages)
        store_chunks(chunks)
        
        return {
            "message": "uploaded successfully",
            "filename": name
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 

@router.post('/ask')
async def prompt_llm(prompt:Prompt):
    try:
        ques=mem.get_standalone_question(prompt.query, prompt.history)
        res = ask(ques)
        hist = mem.update_history(ques, res["answer"], prompt.history)
        return {
            "query": ques,
            "answer": res["answer"],
            "sources": res["sources"],
            "contexts": res["contexts"],
            "history": hist
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))