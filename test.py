import backend.ingestion.parse as ps
import backend.ingestion.chunk as chnk
import backend.ingestion.store as store

arr = ps.parse_pdf("/home/rishav/Downloads/hello.pdf")
chunks = chnk.chunk_pages(arr)
store.store_chunks(chunks)
print("stored successfully :)")
