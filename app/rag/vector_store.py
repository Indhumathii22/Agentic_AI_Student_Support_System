import os
from langchain_community.vectorstores import FAISS
from app.rag.embedder import get_embedder
from langchain_core.documents import Document

FAISS_INDEX_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'faiss_index')

def init_vector_store():
    """
    Initializes a basic vector store with some sample course data if it doesn't exist.
    """
    embedder = get_embedder()
    
    # Check if index exists locally
    if os.path.exists(FAISS_INDEX_PATH) and os.path.exists(os.path.join(FAISS_INDEX_PATH, "index.faiss")):
        print("Loading existing FAISS index.")
        return FAISS.load_local(FAISS_INDEX_PATH, embedder, allow_dangerous_deserialization=True)
    
    print("Creating new FAISS index with sample data.")
    # Sample educational content for the MVP
    sample_texts = [
        "Assignment 3 is about using loops in Python. A for loop is used for iterating over a sequence.",
        "The deadline for the final project is December 15th. Extensions are only granted for medical reasons.",
        "To reset your password, go to the settings page and click 'Forgot Password'.",
        "Prompt injection is a vulnerability where an attacker tries to trick an AI by overriding its instructions.",
        "Academic dishonesty includes copying code from others without citation or having an AI write your entire assignment."
    ]
    
    docs = [Document(page_content=text) for text in sample_texts]
    
    # Create and save
    vector_store = FAISS.from_documents(docs, embedder)
    
    # Ensure directory exists
    if not os.path.exists(FAISS_INDEX_PATH):
        os.makedirs(FAISS_INDEX_PATH)
        
    vector_store.save_local(FAISS_INDEX_PATH)
    return vector_store
