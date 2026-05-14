# System Design Document

## Architecture Overview

The system follows a standard Client-Server architecture with an intelligent processing pipeline.

1.  **Frontend (Client):** Streamlit app that accepts user input and displays the result.
2.  **Backend (API Server):** FastAPI handles incoming requests.
3.  **Processing Pipeline:**
    -   **Pre-Guardrails:** Validates the input query against prompt injection and inappropriate content. If flagged, execution stops here.
    -   **Orchestration & Intent Classification:** An orchestrator analyzes the query to determine its nature (academic, technical, escalation).
    -   **Agent Execution:** CrewAI spins up the designated agent.
    -   **RAG Augmentation:** The agent queries the FAISS vector store to retrieve relevant course context.
    -   **Post-Guardrails:** The generated response is checked for academic dishonesty (e.g., providing direct answers). If flagged, the response is re-written to be a "hint".
    -   **Logging:** The interaction is recorded in a JSON file.

## Agent Personas

-   **Orchestrator:** The router.
-   **Course Agent:** The tutor. Explains concepts.
-   **Assignment Agent:** The strict TA. Gives hints, no answers.
-   **Tech Agent:** The IT helpdesk.
-   **Escalation Agent:** The senior advisor for complex or angry queries.
