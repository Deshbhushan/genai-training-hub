import os
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

# Persistence directory for ChromaDB
CHROMA_PATH = "data/chroma_db"

def get_embedding_function():
    return OllamaEmbeddings(model="llama3")

def create_vector_db(chunks):
    """
    Creates or updates the vector database with new chunks.
    """
    if not chunks:
        return None

    db = Chroma.from_documents(
        documents=chunks, 
        embedding=get_embedding_function(),
        persist_directory=CHROMA_PATH
    )
    return db

def get_retriever():
    """
    Returns a retriever object from the existing vector database.
    """
    db = Chroma(
        persist_directory=CHROMA_PATH, 
        embedding_function=get_embedding_function()
    )
    return db.as_retriever(search_kwargs={"k": 5})
