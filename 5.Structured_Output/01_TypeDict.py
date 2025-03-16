# Take review, extract data and get structured output
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypeDict 

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypeDict)
    
    summary: str 
    sentiment: str 

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""""
        The hardware is great, but the software feels bloated.
            There are too many pre-installed apps that I can't remove. Also,
                the UI looks outdated compared to other brands. Hoping for a software update to fix this.
                                 """)

print(type(result))
print(result)
print(result['summary'])
print(result['sentiment'])