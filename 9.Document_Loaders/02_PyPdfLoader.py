from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("basic-text.pdf")

docs = loader.load()

print(docs)

#First document
print(docs[0].page_content)
print(docs[1].metadata)