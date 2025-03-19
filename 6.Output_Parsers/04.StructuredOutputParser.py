from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.outputparsers import StructuredOutputParser, ResponseSchema

load_dotenv() 

#define the model
llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name = 'fact_1', description = 'Fact 1 about the topic'),
    ResponseSchema(name = 'face_2', description = 'Fact 2 about the topic'),
    ResponseSchema(name = 'fact_3', description = 'Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schema(schema)

template = PromptTemplate(
    template = 'Give 3 face about {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser 

result = chain.invoke({'topic': 'black hole'})

print(result)