from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('dl-curriculum.pdf')]

docs = loader.load() 

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap =0,
    seperator = ''
)

result = splitter.split_documents(docs) #Split all the documents at once.

print(result[1].page_content)