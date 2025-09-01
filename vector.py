import re
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os

def create_documents_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # Clean up the text
    text = text.replace('"', '')
    text = text.replace('\r', '')

    # Split into topics
    # The form feed character seems to be a good delimiter
    topics = re.split('\n\f ', text)
    
    documents = []
    doc_id = 0
    
    # Skip the first part which is metadata
    for topic_text in topics[1:]:
        if not topic_text.strip():
            continue
            
        parts = topic_text.split('Example:')
        
        # The first part is the definition, which also contains the topic title
        definition_part = parts[0]
        
        # The first line of the definition part is the topic title
        lines = definition_part.strip().split('\n')
        topic_title = lines[0].strip()
        definition = '\n'.join(lines[1:]).strip()
        
        example = parts[1].strip() if len(parts) > 1 else ""
        
        page_content = definition
        if example:
            page_content += f"\n\nExample:\n{example}"
            
        document = Document(
            page_content=page_content,
            metadata={"source": topic_title, "id": str(doc_id)}
        )
        documents.append(document)
        doc_id += 1
        
    return documents

# The rest of the file remains the same
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = create_documents_from_file("SQL-FUNDAMENTALS_FOUZIA-_1_.csv")
    if documents:
        ids = [doc.metadata['id'] for doc in documents]
    
        vectordb = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=db_location,
            collection_name="sql_fundamentals",
            ids=ids
        )
    else:
        # Create an empty DB if there are no documents
        vectordb = Chroma(
            collection_name="sql_fundamentals",
            persist_directory=db_location,
            embedding_function=embeddings
        )
else:
    vectordb = Chroma(
        collection_name="sql_fundamentals",
        persist_directory=db_location,
        embedding_function=embeddings
    )

retriever = vectordb.as_retriever(
    search_kwargs={"k": 5}
)
