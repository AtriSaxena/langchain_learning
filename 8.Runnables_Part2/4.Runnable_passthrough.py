from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Explain the following joke - {text}',
    input_variables = ['text']
)

model = ChatOpenAI()

prompt2 = PromptTemplate(
    template = 'Explain the following joke - {text}',
    input_variables =['text']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic': 'Cricket'}))
