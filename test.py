# 
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# from os import getenv

# load_dotenv()
# llm = ChatGroq(
#     api_key=getenv("GROQ_API_KEY"),
#     model=getenv("GROQ_MODEL")
# )
# response = llm.invoke("say hello")
# print(response.content)

import backend.query.result as result
import json
answer = result.ask("what is software engineering?")
print(json.dumps(answer, indent=4))