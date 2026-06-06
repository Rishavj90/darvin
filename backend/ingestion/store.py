# 1. Load an embedding model
# 2. Embed each chunk's text into a vector
# 3. Store the vector + text + metadata into ChromaDB
from dotenv import load_dotenv
from os import getenv
import chromadb
from sentence_transformers import SentenceTransformer


load_dotenv()
model = SentenceTransformer(getenv('EMBEDDING_MODEL'))

client = chromadb.PersistentClient(path=getenv("CHROMA_PATH"))
collection = client.get_or_create_collection(
    name=getenv("COLLECTION_NAME")
)

def store_chunks(chunks_arr):
    id_arr=[]
    txt_arr=[]
    embeddings_arr=[]
    metadata_arr=[]
    for chunk in chunks_arr:
        id_arr.append(chunk["chunk_id"])
        txt_arr.append(chunk["text"])
        embeddings_arr.append(model.encode(chunk["text"]).tolist())
        metadata_arr.append({
            "page" : chunk["page"],
            "source" : chunk["source"]
        })
    collection.upsert(
        ids=id_arr,
        embeddings=embeddings_arr,
        documents=txt_arr,
        metadatas=metadata_arr
    )