from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate(
    [
        #Note: This will not work
        # SystemMessage(content="You a helpful {domain} expert."),
        # HumanMessage(content = "Explain in simple terms, what is {topic}")
        ('system', 'You a helpful {domain} expert.'),
        ('human', 'Explain in simple terms, what is {topic}')
    ]
)

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})

print(prompt)