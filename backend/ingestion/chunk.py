# split text into chunks

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_pages(arr, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,          # max characters per chunk
        chunk_overlap=chunk_overlap,    # characters shared between chunks
        separators=["\n\n", "\n", ".", " ", ""]
    )
    
    chunks_arr = []
    for page_dict in arr:
        chunks = splitter.split_text(page_dict["text"])
        page = page_dict["page"]
        source = page_dict["source"]
        for j in range(len(chunks)):
            chunks_arr.append({
                "text" : chunks[j],
                "page" : page,
                "source" : source,
                "chunk_id" : f"{source}_page{page}_chunk{j+1}" 
            })
    
    return chunks_arr
