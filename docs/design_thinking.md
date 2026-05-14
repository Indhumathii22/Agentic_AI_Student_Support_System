# Design Thinking Approach
## Agentic AI Student Support System

---

# 1. Empathize

Online education platforms handle thousands of student queries daily related to:
- course guidance
- assignment help
- grading support
- technical issues

Students often face:
- delayed responses
- confusion during learning
- lack of personalized support
- frustration with technical problems

Support teams struggle with:
- repetitive queries
- operational overload
- increasing response time
- scalability challenges

Additionally, educational AI systems must ensure:
- academic integrity
- ethical AI usage
- student privacy protection

### Key Insight

Students do not simply need answers.  
They need:
- guided learning
- fast support
- conceptual understanding
- ethical academic assistance

---

# 2. Define

# Problem Statement

Online learning platforms struggle to provide scalable, personalized, and ethical support for large numbers of student queries.

Traditional support systems lead to:
- slow response times
- inconsistent support quality
- poor learning experience
- operational strain

At the same time, AI systems must prevent:
- direct assignment cheating
- unsafe AI behavior
- misuse of educational AI

# How Might We

> How might we build an intelligent multi-agent academic support system for online learners so that students receive fast, personalized, ethical, and scalable assistance while reducing support workload?

---

# 3. Ideate

Multiple solution approaches were considered:

## Traditional Chatbot
Rejected because:
- static responses
- poor personalization
- limited scalability

## Single AI Assistant
Rejected because:
- overloaded responsibilities
- weak specialization
- difficult workflow management

## Multi-Agent AI System
Selected because:
- specialized agents improve response quality
- orchestrator enables intelligent routing
- modular architecture improves scalability
- easier maintenance and monitoring

### Final Solution

We designed an:
# Agentic AI Student Support System

using:
- CrewAI orchestration
- specialized AI agents
- RAG-based retrieval
- lightweight guardrails
- monitoring system

The system intelligently routes student queries to dedicated agents based on intent.

---

# 4. Prototype

# System Architecture

Student Query
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
CrewAI Orchestrator
    ↓
Intent Classification
    ↓
Task Routing
 ┌────────┬─────────┬──────────┬──────────┐
 ↓        ↓         ↓          ↓
Course  Assignment  Technical Escalation
Agent     Agent       Agent      Agent
      ↓
Guardrails
      ↓
Response Generation
      ↓
Monitoring Logs

---

# Agent Design

## Orchestrator Agent
- classifies intent
- routes queries
- coordinates agents

## Course Guidance Agent
- explains concepts
- provides learning guidance

## Assignment Support Agent
- provides hints and explanations
- prevents direct assignment solving

## Technical Support Agent
- handles troubleshooting
- resolves platform issues

## Escalation Agent
- handles unresolved issues
- simulates human escalation

---

# Guardrails Design

To ensure ethical AI usage, lightweight guardrails were implemented.

## Input Guardrails
Detect:
- academic dishonesty
- prompt injection
- harmful prompts

## Output Guardrails
Prevent:
- direct assignment answers
- plagiarism-ready responses
- unsafe outputs

If cheating attempts are detected, the system switches to:
# Guided Learning Mode

Instead of giving direct answers, the AI:
- explains concepts
- provides hints
- encourages learning

---

# Monitoring Design

The system tracks:
- misuse attempts
- escalation frequency
- response latency
- agent activity

This improves:
- transparency
- maintainability
- future scalability

---

# 5. Test

The system was tested using multiple scenarios.

## Scenario 1
### Query:
“Suggest a roadmap to learn Python.”

### Expected:
Course Guidance Agent responds.

---

## Scenario 2
### Query:
“Solve my graded assignment completely.”

### Expected:
Guardrail triggers and guided learning response is generated.

---

## Scenario 3
### Query:
“I cannot access my course certificate.”

### Expected:
Technical Support Agent responds.

---

## Scenario 4
### Query:
“I am frustrated with repeated platform issues.”

### Expected:
Escalation Agent activates.

---

# Conclusion

Using the Design Thinking approach helped design a student-centered AI support system that balances:
- scalability
- personalization
- ethical AI behavior
- educational integrity

The final solution combines:
- multi-agent orchestration
- retrieval-augmented generation
- lightweight guardrails
- monitoring systems

to create a scalable and responsible AI-powered student support platform.