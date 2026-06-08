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
import backend.query.memory as memory

history=[]
while True:
    prompt = input("prompt > ")
    if prompt=="exit" or prompt=="quit":
        print("\n bye!")
        break;
    ques = memory.get_standalone_question(prompt, history)
    ans = result.ask(ques)
    history = memory.update_history(ques, ans["answer"], history)
    print(f"""\n {ans["answer"]} \n""")