# Hyde RAG Implementation

## Overview

A RAG implementing the HyDE (Hypothetical Document Embeddings) technique. Instead of directly using user queries for retrieval, the system generates hypothetical documents that better match the semantic space of the knowledge base.
<img width="1833" height="572" alt="image" src="https://github.com/user-attachments/assets/47dc949f-e733-43c5-b98a-56b5a30dae8c" />

## Architecture

There are two main chains:
- **Hyde Chain**: Generates hypothetical documents from user queries
- **RAG Chain**: Uses generated documents for retrieval and final answer generation

## Project Structure

```
├── config.py          # Configuration settings
├── ingestion.py       # Document ingestion and vector store creation
├── main.py           # Main application entry point
└── chains/
    ├── hyde.py       # Hypothetical document generation
    └── rag.py        # RAG chain implementation
```


### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure Ollama is running, and change the models in config.:
```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Configuration

Modify `config.py` to adjust:
- **EMBEDDING_MODEL**: Embedding model for document vectors
- **LLM_MODEL**: Language model for text generation
- **CHUNK_SIZE**: Document chunk size (default: 1000)
- **CHUNK_OVERLAP**: Chunk overlap (default: 200)

## Usage

### 1. Document Ingestion
Place your PDF document in the root directory and update the filepath in `ingestion.py`:

```bash
python ingestion.py
```

### 2. Query the System
```bash
python main.py
```

## How It Works
1. User submits a query
2. Hyde chain generates a hypothetical document answering the query
3. The hypothetical document is used to retrieve relevant chunks from the vector store
4. Retrieved chunks provide context for generating the final answer
