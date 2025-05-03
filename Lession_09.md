# Lession 09: Document Loaders in Langchain

----------------------------------------------

## RAG:
RAG is technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded response. 

Benefits of using RAG: 
1. Use of up to date information
2. Better privacy
3. No limit of document size

![alt text](images/image_09_01.png)

## Document Loaders

![alt text](images/image_09_02.png)

Document Loaders are components in langchain used to load data from various sources into a standardized format (usually as document object), which can then be used for chunking, embedding, retreival and generation. 

*Standard format:*
```
Document{
    page_content = "The actual text content",
    metadata = {"source": "filename.pdf" ...}
}
```

### 1. Text Loader:

Text loader is a simple and commonly used document loader in LangChain that reads plain text(.txt) files and convert them into Langchain Document Object.

#### UseCase:
- Ideal for loading chat logs, scaped text, transcripts, code snippets, or any plain text data into a Langchain pipeline. 

#### Limitation
- Works only with .txt file

### 2. PyPDFLoader: 

PyPDFLoader is a document loader in LangChain used to load content from PDF files and convert each page into a Document object.

```
[
    Document(page_content = "Text from page 1", metadata = {"page": 0, "source": "file.pdf"}),
    Document(page_content = "Text from page 2", metadata = {"page": 1, "source": "file.pdf"})
]

```
#### Limitation

- It uses the PyPDF library under the hood - not great with scanned PDFs or complex layouts. 

## Some other PDF loaders which are for scanned PDF files

| Use Case                          | Recommended Loader                                         |
|----------------------------------|------------------------------------------------------------|
| Simple, clean PDFs               | `PyPDFLoader`                                              |
| PDFs with tables/columns         | `PDFPlumberLoader`                                         |
| Scanned/image PDFs               | `UnstructuredPDFLoader` or `AmazonTextractPDFLoader`       |
| Need layout and image data       | `PyMuPDFLoader`                                            |
| Want best structure extraction   | `UnstructuredPDFLoader`                                    |

### 3. DirectoryLoader

`DirectoryLoader` is a document loader that lets you load multiple documents from a directory(folder) of files. 

| Glob Pattern      | What It Loads                                  |
|-------------------|-------------------------------------------------|
| `"**/*.txt"`      | All `.txt` files in all subfolders              |
| `"*.pdf"`         | All `.pdf` files in the root directory          |
| `"data/*.csv"`    | All `.csv` files in the `data/` folder          |
| `"**/*"`          | All files (any type, all folders)               |

> `**` = recursive search through subfolders

## Load vs LazyLoad
- ✅`load()`
- **Eager Loading** (loads everything at once). 
- Returns: A list if `Document` objects.
- Loads all documents **immediately** into memory.
- Best When:
    - The number of documents is small. 
    - You want everything loaded upfront.

- ✅`lazy_load()`
- **Lazy Loading**(loads on demand using `generators`)
- Returns: A generator of `Document` objects. 
- Documents are not all loaded at once; they are fetched one at a time as needed. 
- Best when:
    - You are dealing with **large documents of loat of files.**
    - You want to stream processing(e.g., chunking, embedding) without using lots of memory.

### 4. WebBaseLoader

WebBaseLoader is a document loader in LangChain used to load and extract text content from web pages(URLs).

It uses BeautifulSoup under the hood to parse HTML and extract visible text.

**When to Use:**
- For blogs, news article, or public websites where the content is primarily text based and static. 

**Limitations:**
- Doesn't handle JavaScript heavy pages well (use **SeleniumURLLoader** for that). 
- Loads only static content(what's in the HTML, not what loads after the page renders).

### 5. CSVLoader

CSVLoader is a document loader used to load CSV files into LangChain Document objects one per row by default.

REF: https://python.langchain.com/docs/integrations/document_loaders/