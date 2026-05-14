# Agentic AI Student Support System

An Agentic AI-powered Student Support System designed for online education platforms. This system leverages CrewAI for multi-agent orchestration, providing a clean architecture for handling student queries, ensuring academic integrity through guardrails, and presenting a user-friendly frontend.

## Project Overview

The Agentic AI Student Support System acts as a virtual teaching assistant. It can:
- Provide course guidance and learning paths.
- Offer hints and assistance on assignments (while strictly avoiding giving direct solutions).
- Troubleshoot platform technical issues.
- Escalate unresolved queries intelligently.

## Architecture

The system follows a modular architecture:
1.  **Frontend (Streamlit):** A minimalistic UI for students to submit queries and view AI responses, complete with risk indicators.
2.  **Backend (FastAPI):** Exposes a `/query` endpoint that coordinates the orchestration.
3.  **Orchestrator (CrewAI):** Classifies query intents and dynamically routes them to specialized agents (Course, Assignment, Tech, Escalation).
4.  **Guardrails:** Pre-and-post processing layers to detect prompt injection, academic dishonesty, and inappropriate content.
5.  **RAG Layer:** Uses LangChain, FAISS, and Gemini embeddings to retrieve relevant contextual data for the agents.
6.  **Monitoring:** Local JSON logging for auditing and performance tracking.

## Tech Stack

- **Language:** Python
- **Orchestration:** CrewAI
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **LLM / Embeddings:** Google Gemini API
- **RAG:** LangChain + FAISS
- **Other:** python-dotenv, Pydantic, JSON Logging

## Setup Instructions

### 1. Clone the Repository
\`\`\`bash
git clone <repository_url>
cd agentic-ai-student-support
\`\`\`

### 2. Set Up Virtual Environment
\`\`\`bash
python -m venv venv
# Windows:
venv\\Scripts\\activate
# Mac/Linux:
source venv/bin/activate
\`\`\`

### 3. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Environment Variables
Create a \`.env\` file in the root directory and add your Google Gemini API key:
\`\`\`env
GEMINI_API_KEY=your_gemini_api_key_here
\`\`\`

### 5. Running the Application

**Start the FastAPI Backend:**
\`\`\`bash
uvicorn app.api.main:app --reload --port 8000
\`\`\`

**Start the Streamlit Frontend:**
Open a new terminal, activate the virtual environment, and run:
\`\`\`bash
streamlit run frontend/streamlit_app.py
\`\`\`

## API Usage

The backend exposes a single main endpoint.

**POST `/query`**

**Payload:**
\`\`\`json
{
  "query": "Can you give me the solution to assignment 3?"
}
\`\`\`

**Response:**
\`\`\`json
{
  "response_text": "I cannot provide the direct solution to your assignment, but I can guide you through the concepts...",
  "selected_agent": "Assignment Agent",
  "guardrail_status": "Blocked Direct Answer",
  "risk_level": "HIGH"
}
\`\`\`

## Future Improvements

- Replace local JSON logging with an ELK stack or Prometheus/Grafana.
- Upgrade FAISS to a managed vector database (e.g., Pinecone, Weaviate) for scale.
- Implement proper user authentication.
- Connect to an actual LMS (Learning Management System) database instead of local documents.
