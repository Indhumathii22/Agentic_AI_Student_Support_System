from crewai import Agent
from app.agents.course_agent import get_llm

def create_escalation_agent() -> Agent:
    return Agent(
        role='Senior Advisor & Escalation Manager',
        goal='Handle unresolved issues, detect frustration, and simulate human escalation.',
        backstory=(
            "You are a calm, empathetic senior advisor. "
            "You handle queries where the student is frustrated, confused, or asking for human intervention. "
            "You assure them that their issue is being recorded and provide the best possible temporary guidance."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
