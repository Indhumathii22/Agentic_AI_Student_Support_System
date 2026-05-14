from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.guardrails.rules import guardrails, RISK_BLOCKED
from app.agents.orchestrator import process_query
from app.monitoring.logger import interaction_logger
import time

app = FastAPI(
    title="Agentic AI Student Support API",
    description="Backend API for the Student Support Multi-Agent System",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response_text: str
    selected_agent: str
    guardrail_status: str
    risk_level: str

@app.get("/")
def health_check():
    return {"status": "healthy"}

@app.post("/query", response_model=QueryResponse)
def handle_query(request: QueryRequest):
    start_time = time.time()
    query = request.query

    try:
        # 1. Input Guardrails
        risk_level, status_msg = guardrails.check_input(query)
        
        if risk_level == RISK_BLOCKED:
            response_text = "Your query has been blocked due to safety policies."
            selected_agent = "Guardrail System"
            guardrail_status = status_msg
            
        else:
            # 2. Process via Orchestrator/CrewAI
            raw_response, selected_agent = process_query(query, risk_level)
            
            # 3. Output Guardrails
            out_risk, out_status, filtered_response = guardrails.check_output(raw_response)
            
            response_text = filtered_response
            
            # Elevate risk level if output flagged it
            if out_risk in ["MEDIUM", "HIGH"] and risk_level == "SAFE":
                risk_level = out_risk
            
            guardrail_status = f"Input: {status_msg} | Output: {out_status}"

        # 4. Logging
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 1000
        interaction_logger.log_interaction(
            query=query,
            agent_name=selected_agent,
            response=response_text,
            risk_level=risk_level,
            guardrail_status=guardrail_status,
            response_time_ms=elapsed_ms
        )

        return QueryResponse(
            response_text=response_text,
            selected_agent=selected_agent,
            guardrail_status=guardrail_status,
            risk_level=risk_level
        )

    except Exception as e:
        print(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
