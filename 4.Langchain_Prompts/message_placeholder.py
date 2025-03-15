from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder

# Message Placeholder to retrive and restore chat history

#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagePlaceholder(variable_name = 'chat_history')
    ('human', '{query}') # Where is my order?
])

#load chat history
chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt

prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'where is my refund?'})

print(prompt)