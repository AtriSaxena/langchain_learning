#This code is intended to be used only for LLMs not chatbot. 
# But langchain also force to use chatbots. 

from langchain_openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model= "gpt-3.5-turbo-instruct")

result = llm.invoke("What is the capital of India.")

print(result)