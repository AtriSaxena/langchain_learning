from langchain_openai import ChatOpenAI
import streamlit as st 
from dotenv import load_dotenv

load_dotenv() 

st.header("Research Tool")

model = ChatOpenAI(model = 'gpt-4', temperature = 0.3, max_completion_token=10)
user_input = st.text_input('Enter your prompt')

if st.button('Summarize'): 
    result = model.invoke(user_input)
    st.write(result.content)

  