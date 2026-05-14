import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_embedder():
    """
    Returns the configured Gemini embedding model.
    """
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        # Provide a fallback or warning for MVP purposes
        print("WARNING: API KEY not found in environment. Embeddings may fail.")
        
    return GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=api_key)
