from langchain_openai import ChatOpenAI
import streamlit as st 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv() 

st.header("Research Tool")

model = ChatOpenAI(model = 'gpt-4', temperature = 0.3, max_completion_token=10)

paper_input = st.selectbox("Select Research Paper Name:",
                           ["Select...",
                            "Attention is all you need.",
                            "BERT: pre-training of Deep Bi-directional Transformers",
                            "GPT-3: Language Models are Few-Shot Learners",
                            "Diffusion Models beat GANs on Image synthesis"
                            ])

style_input = st.selectbox("Select Explanation Style",
                           ["Begineer Friendly",
                            "Technical",
                            "Code Oriented",
                            "Mathematical"])

length_input = st.selectbox("Select Explanation Length",
                            ["Short (1-2 paragraphs)",
                             "Medium (3-5 paragraphs)",
                             "Long (detailed explanation)"])

#Template 
template = PromptTemplate(
    template = """
        Please summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation Style: {style_input}
        Explanation Length: {length_input}
        1. Mathematical Details: 
            - Include Relevant mathematical equations if present in the paper.
            - Explain the mathematical concepts using simple, intutive code snippets where applicable.
        2. Analogies:
            - Use relatable anologies to simplify complex ideas. 
        If certain information is not available in the paper, respond with: "Insufficient Information available" Instead of guessing.
        Ensure the summary is clear, accurate, and aligned with the provided style and length.
        """,
        input_variables = ['paper_input', 'style_input', 'length_input']
)

# FIll the placeholder
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})


if st.button('Summarize'): 
    result = model.invoke(prompt)
    st.write(result.content)

  