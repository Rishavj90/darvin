# 1. Load an embedding model
# 2. Embed each chunk's text into a vector
# 3. Store the vector + text + metadata into ChromaDB

import chromadb
from dotenv import load_dotenv

load_dotenv()

def store_chunks(chunks_arr, chromadb_path=".../chromaDB"):
    