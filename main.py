from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """

"""

# https://www.youtube.com/watch?v=d0o89z134CQ

model = OllamaLLM(model="gemma2:2b")

result = model.invoke(input="Xin chào giáo viên tiếng anh và ngoại ngữ cấp 3")
print(result)

