from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def ask_gpt(api_key, instructions, question, show_logs=False):

    chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.1, api_key=api_key)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",instructions,),
            ("human", question),
        ]
    )

    chain = prompt | chat

    response = chain.invoke({})
    if show_logs:
        print(response.content)
        
    return response.content