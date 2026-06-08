from backend.query.result import llm

def update_history(ques, ans, history):
    history.append({
        "user" : ques,
        "bot" : ans
    })
    return history

def get_standalone_question(ques, history):
    context="Given the following chat : \n"
    if len(history)==0:
        return ques
    elif len(history)<=5:
        for chat in history:
            user=chat["user"]
            bot = chat["bot"]
            context+=f"""
                user : {user}
                bot : {bot}
             
            """
    else:
        num=-1
        while num>-6:
            user=history[num]["user"]
            bot =history[num]["bot"]
            context+=f""" 
                user : {user}
                bot : {bot}
                
            """
            num-=1
    context+=f"Rewrite the following question such as all that chat is not required to understand it. \n question : {ques}"
    
    response = llm.invoke(context)
    return response.content
    
    