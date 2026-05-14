from app.rag.vector_store import init_vector_store

# Initialize it once
_vector_store = None

def get_retriever():
    global _vector_store
    if _vector_store is None:
        _vector_store = init_vector_store()
    return _vector_store.as_retriever(search_kwargs={"k": 2})

def retrieve_context(query: str) -> str:
    """
    Retrieves context relevant to the query from the vector store.
    """
    try:
        retriever = get_retriever()
        docs = retriever.invoke(query)
        context = "\n".join([doc.page_content for doc in docs])
        return context
    except Exception as e:
        print(f"Error retrieving context: {e}")
        return ""
