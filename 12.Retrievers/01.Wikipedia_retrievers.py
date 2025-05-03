from langchain_community.retrievers import WikipediaRetriever

#Initialize the reteivers (optional set language and top_k)

retriever = WikipediaRetriever(top_k_results=2, lang='en')

#Define your query
query = "the geopolitical history of India and pakistan from a perspective of a chinese"

#Get Relevant Wikipedia documents
docs = retriever.invoke(query)


# Print Retreived document
for i, doc in enumerate(docs): 
    print(f"------RESULT {i}------")
    print(f"....Content: \n{doc.page_content}......")
    