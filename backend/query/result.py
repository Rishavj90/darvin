from backend.ingestion.store import model, collection
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from os import getenv

load_dotenv()

llm = ChatGroq(
    api_key=getenv("GROQ_API_KEY"),
    model=getenv("GROQ_MODEL")
)

def ask(query):
    contexts_arr=[]
    sources_arr=[]
     
    embedings = model.encode(query).tolist()
    result = collection.query(
        query_embeddings=[embedings],
        n_results=5
    )
    
    context=""
    for doc, meta in zip(result["documents"][0], result["metadatas"][0]):
        source=meta["source"]
        page=meta["page"]
        
        sources_arr.append({
            "source" : source,
            "page" : page
        })
        contexts_arr.append(doc)
        
        context+=f"""
        [Source: {source}, Page: {page}]
        {doc}
        
        """
    
    response = llm.invoke(f"""
        You are a research assistant. Answer the question using 
        ONLY the context provided below. 

        Rules:
        - If the answer is not in the context, say "I cannot find 
        this information in the provided documents"
        - Always cite your sources as [source, page X] after each 
        relevant statement
        - Do not use any outside knowledge

        Context:
        {context}

        Question:
        {query}
        
        Answer:
        
    """)
    
    return dict({
        "answer" : response.content,
        "sources" : sources_arr,
        "contexts" : contexts_arr
    })

