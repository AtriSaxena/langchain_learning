from langchain_huggingface import ChatHuggingFace, HuggingFaceEndPoint
from dotenv import load_dotenv

load_dotenv() 

llm = HuggingFaceEndPoint(
    repo_id ="TinyLlama/TinyLlama-1.1B-Chat-v1.0", #Currently this model is on hugging face server
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of India?")
print(result.content)


