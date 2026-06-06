# extract raw text + page numbers from PDF

import fitz
from pathlib import Path

def parse_pdf(path):
    try:
        arr = []
        with fitz.open(path) as doc:
            for i in range(len(doc)):
                text = doc[i].get_text()
                if text.strip() :
                    arr.append({
                        "text" : text,
                        "page" : i+1,
                        "source" : Path(path).name
                    })
        
        if len(arr)==0:
            raise Exception("got no text. file must not contain scanned images")
        
        return arr
    
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF not found: {path}")
    

