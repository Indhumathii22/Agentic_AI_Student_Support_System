# Tech Stack Justification

## Python
The de-facto language for AI/ML and backend prototyping. Ensures access to all required libraries.

## FastAPI
Chosen for the backend because it's asynchronous, extremely fast, and automatically generates API documentation (Swagger/OpenAPI). It perfectly handles JSON-based RESTful communication.

## Streamlit
Provides the fastest way to build a functional, visually appealing frontend for data and AI applications without needing complex React/Vue setups. Fits the "lightweight MVP" requirement perfectly.

## CrewAI
A powerful framework for orchestrating role-playing autonomous AI agents. It simplifies the process of assigning tasks to specific "personas" (Course Agent, Tech Agent, etc.).

## Google Gemini API
Serves as the core LLM for both the agents and the guardrail classification, providing high-quality reasoning and generation.

## LangChain & FAISS
LangChain provides the abstractions for document loading and splitting. FAISS (Facebook AI Similarity Search) is an efficient, local, in-memory vector store perfect for MVP RAG implementations without the overhead of a dedicated database.

## python-dotenv
For secure management of the Gemini API key.
