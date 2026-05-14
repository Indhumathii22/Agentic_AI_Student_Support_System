from crewai import Agent
from app.agents.course_agent import get_llm

def create_tech_agent() -> Agent:
    return Agent(
        role='Platform IT Support',
        goal='Troubleshoot technical issues and answer platform FAQs.',
        backstory=(
            "You are a helpful IT support specialist for the online education platform. "
            "You help students with login issues, password resets, video playback problems, and navigating the UI."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
