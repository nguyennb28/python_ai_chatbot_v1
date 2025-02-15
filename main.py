from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Video youtube: https://www.youtube.com/watch?v=d0o89z134CQ

model = OllamaLLM(model="llama3.2:3b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = "You are Ms.Quỳnh Vy and you are a super good English teacher in Vietnam."
    print("Chào bạn 🙌, tôi là giáo viên dạy tiếng anh, tôi có thể giúp gì cho bạn. \n Gõ 'exit' để thoát.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Rất vui khi được đồng hành cùng bạn 😁")
            break
        
        
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

# print(handle_conversation())
if __name__ == "__main__":
    handle_conversation()
