from crewai import Crew, Task
from app.agents.course_agent import create_course_agent
from app.agents.assignment_agent import create_assignment_agent
from app.agents.tech_agent import create_tech_agent
from app.agents.escalation_agent import create_escalation_agent
from app.rag.retriever import retrieve_context
import re

def classify_intent(query: str) -> str:
    """
    Simple intent classification. 
    In a full production environment, this could be another LLM call.
    For MVP, we use keyword heuristics.
    """
    query_lower = query.lower()
    
    if any(word in query_lower for word in ["assignment", "homework", "quiz", "test", "exam", "grade"]):
        return "assignment"
    elif any(word in query_lower for word in ["login", "password", "video", "load", "error", "bug", "platform"]):
        return "tech"
    elif any(word in query_lower for word in ["manager", "human", "angry", "terrible", "sucks", "frustrated"]):
        return "escalation"
    else:
        return "course"

def process_query(query: str, risk_level: str) -> tuple[str, str]:
    """
    Processes the query through the CrewAI agents.
    Returns: (Response text, Agent Name)
    """
    # 1. Retrieve Context
    context = retrieve_context(query)
    
    # 2. Classify Intent
    intent = classify_intent(query)
    
    # 3. Select Agent and Setup Task
    agent_name = ""
    selected_agent = None
    task_description = f"Answer the student's query: '{query}'.\n"
    
    if context:
        task_description += f"Use the following course context if relevant: {context}\n"

    if risk_level == "HIGH":
        # Force assignment agent if academic dishonesty was detected
        intent = "assignment"
        task_description += "WARNING: Academic dishonesty attempt detected. DO NOT provide direct answers. Provide high-level conceptual hints only."

    if intent == "assignment":
        selected_agent = create_assignment_agent()
        agent_name = "Assignment Agent"
    elif intent == "tech":
        selected_agent = create_tech_agent()
        agent_name = "Tech Agent"
    elif intent == "escalation":
        selected_agent = create_escalation_agent()
        agent_name = "Escalation Agent"
    else:
        selected_agent = create_course_agent()
        agent_name = "Course Agent"

    task = Task(
        description=task_description,
        expected_output="A helpful, professional response to the student's query adhering to the agent's role.",
        agent=selected_agent
    )

    crew = Crew(
        agents=[selected_agent],
        tasks=[task],
        verbose=True
    )

    # 4. Execute
    result = crew.kickoff()
    
    return str(result), agent_name
