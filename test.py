import backend.ingestion.parse as ps
import backend.ingestion.chunk as chnk

arr = ps.parse_pdf("/home/rishav/Downloads/hello.pdf")
chunks = chnk.chunk_pages(arr)
print(f"total no. of chunks : {len(chunks)}")
print(chunks[0])
