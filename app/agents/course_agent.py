import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("WARNING: API KEY not found. LLM will fail.")
    return LLM(model="gemini/gemini-2.5-flash", api_key=api_key)

def create_course_agent() -> Agent:
    return Agent(
        role='Course Guidance Counselor',
        goal='Explain course concepts clearly and provide learning guidance.',
        backstory=(
            "You are an experienced and patient teaching assistant. "
            "You excel at breaking down complex concepts into easy-to-understand explanations. "
            "You use analogies and step-by-step reasoning to help students learn."
        ),
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
