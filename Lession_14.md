## RAG System 

### Improvements

- While developing a RAG system for a industry level what all improvments we can use: 

1. UI based Enhancements
2. Evaluation
    - [Ragas:](https://docs.ragas.io/en/stable/) For evaluation of LLM and RAGs
        Metrics: Faithfulness, Answer_Relevancy, Context precision, Context Recall
    - Langsmith
3. Indexing
    - Document ingestion
    - Text Splitting
    - Vector store
4. Retrieval
    - Pre-Retrieval:
        - Query rewriting using LLM
        - Multi-query generation
        - Domain aware routing
    - During Retrieval
        - MMR
        - Hybrid-Retrieval
        - Reranking
    - Post-Retieval
        - Contextual Compression
5. Augmentation
    - Prompt Templating
    - Answer grounding
    - Context window optimization
6. Generation
    - Answer with Citation
    - Guard Railing
7. System Design
    - Multimodal
    - Agentic
    - Memory based