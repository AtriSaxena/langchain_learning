# Retreivers in LangChain

## What are Retrievers

- A retriever is a component in langchain that fetches relevant document from a data source in response to a user query. 

- There are multiple type of retrievers. 

- *All retrievers in Langchain are Runnables.*

![alt text](images/image12_01.png)

## Type of Retrievers

### Based on Data source: 

- **Wikipedia Retrievers**
- **Vector Store Retrievers**
- **Arxiv Retreivers**

*Read More: https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/*

### Based on Search Strategy

- **MMR: Maximal Marginal Retreivar**
- **Multi Query Retreiver**
- **Contexual Compression Retreiver**

### Wikipedia Retrievers: 

- A wikipedia retriever is a retriever that queries the Wikipedia API to fetch relevant content for a given query. 

#### ⚙️How it works:

1. You gave it a query (e.g., Alberts Einstein)

2. It sends the query to Wikipedia's API.

3. It retreives the most *relevant article.*(some keyword matching in background) 

4. It returns them as LangChain `Document` object.

### Vector Stores Retrievers

A vector store retriever in Langchain is the most common type of retriever that lets you search and fetch documents from a vector store based on semantic similarity using vector embedding.

#### ⚙️How it works:

1. You store your documents in a vector store like FAISS, Chroma, Weaviate.
2. Each document is coverted into a dense vector using an embedding model. 
3. When the user enters a query:
    - Its also turned into vector 
    - The retriever compares the query vector with the stored vector.
    - It retrieves the top k-most similar ones.
    