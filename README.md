# SQL Fundamentals Q&A Agent with RAG and Ollama

This project is a Retrieval-Augmented Generation (RAG) application that answers questions about SQL fundamentals using locally-run AI models. It combines the power of vector databases for information retrieval with large language models for natural language understanding.

## Features

- **Local AI Processing**: Uses Ollama to run language models locally, ensuring privacy and eliminating API costs
- **Accurate Information Retrieval**: Employs ChromaDB vector database to retrieve relevant SQL concepts
- **Interactive Q&A**: Command-line interface for asking questions about SQL fundamentals
- **Persistent Knowledge Base**: Vector embeddings are stored locally for fast retrieval

## Architecture

The application consists of three main components:

1. **Vector Database (ChromaDB)**: Stores embeddings of SQL fundamentals text for efficient similarity search
2. **Retriever**: Finds the most relevant SQL concepts based on user questions
3. **Language Model (Ollama)**: Generates natural language answers using retrieved context

## Prerequisites

- Python 3.8 or higher
- Ollama (with `llama3.2` and `mxbai-embed-large` models)
- Git (optional, for cloning the repository)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SHYAMFRANCIS/sql-fundamentals-rag-agent.git
   cd sql-fundamentals-rag-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Ollama from [https://ollama.com/](https://ollama.com/)

5. Pull the required models:
   ```bash
   ollama pull llama3.2
   ollama pull mxbai-embed-large
   ```

## Usage

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Ask questions about SQL fundamentals when prompted
4. Type `q` to quit the application

## How It Works

1. On first run, the application processes `SQL-FUNDAMENTALS_FOUZIA-_1_.csv` and creates vector embeddings stored in ChromaDB
2. When you ask a question:
   - The retriever finds the 5 most relevant SQL concepts from the vector database
   - These concepts are sent to the LLM along with your question
   - The LLM generates an answer based on the provided context
3. The vector database is persisted locally, so subsequent runs are faster

## Project Structure

```
├── main.py                 # Main application interface
├── vector.py               # Vector database creation and retrieval
├── SQL-FUNDAMENTALS_FOUZIA-_1_.csv  # SQL fundamentals knowledge base
├── requirements.txt        # Python dependencies
└── chroma_langchain_db/    # Persistent vector database (created on first run)
```

## Dependencies

- langchain: Framework for developing applications with LLMs
- langchain-ollama: Integration with Ollama for running LLMs locally
- langchain-chroma: Integration with ChromaDB for vector storage
- pandas: Data processing library

## Customization

To use your own knowledge base:
1. Replace `SQL-FUNDAMENTALS_FOUZIA-_1_.csv` with your own text file
2. Update the parsing logic in `vector.py` if your file format differs
3. Delete the `chroma_langchain_db` folder to force recreation of the vector database

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- SQL fundamentals content by Ms. K.F. Fouzia Sulthana
- Ollama for making local LLMs accessible
- ChromaDB for vector database functionality
- Langchain for the RAG framework