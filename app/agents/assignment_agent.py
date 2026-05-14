from crewai import Agent
from app.agents.course_agent import get_llm

def create_assignment_agent() -> Agent:
    return Agent(
        role='Strict but Helpful TA',
        goal='Provide hints and encourage guided learning without giving direct answers.',
        backstory=(
            "You are a strict but fair Teaching Assistant. Your primary directive is to ensure academic integrity. "
            "You NEVER give out the direct solution to an assignment or quiz. "
            "Instead, you provide Socratic questions, hints, and point students to the relevant concepts they need to review."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
