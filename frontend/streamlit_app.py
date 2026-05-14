import streamlit as st
import requests
import json
import os

# Configure page
st.set_page_config(
    page_title="Agentic AI Support",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for a clean UI
st.markdown("""
<style>
    .risk-safe { color: #155724; background-color: #d4edda; padding: 5px; border-radius: 3px; }
    .risk-medium { color: #856404; background-color: #fff3cd; padding: 5px; border-radius: 3px; }
    .risk-high { color: #721c24; background-color: #f8d7da; padding: 5px; border-radius: 3px; }
    .risk-blocked { color: white; background-color: #dc3545; padding: 5px; border-radius: 3px; font-weight: bold; }
    .agent-badge { background-color: #004085; color: white; padding: 4px 8px; border-radius: 10px; font-size: 0.8em; }
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Support Assistant")
st.write("Ask me anything about the course, assignments, or platform issues!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "metadata" in message:
            md = message["metadata"]
            
            # Formatting risk level
            risk_class = f"risk-{md['risk_level'].lower()}"
            
            st.markdown(f"""
            <hr style="margin: 10px 0;">
            <div style="display: flex; gap: 10px; align-items: center; font-size: 0.9em;">
                <span class="agent-badge">🤖 {md['selected_agent']}</span>
                <span class="{risk_class}">Risk: {md['risk_level']}</span>
            </div>
            <div style="font-size: 0.8em; color: gray; margin-top: 5px;">
                Guardrail: {md['guardrail_status']}
            </div>
            """, unsafe_allow_html=True)

# Accept user input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        try:
            # Call FastAPI Backend
            API_URL = os.environ.get("API_URL", "http://localhost:8000/query")
            payload = {"query": prompt}
            
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            
            data = response.json()
            full_response = data["response_text"]
            
            # Display text
            message_placeholder.markdown(full_response)
            
            # Display metadata
            risk_class = f"risk-{data['risk_level'].lower()}"
            st.markdown(f"""
            <hr style="margin: 10px 0;">
            <div style="display: flex; gap: 10px; align-items: center; font-size: 0.9em;">
                <span class="agent-badge">🤖 {data['selected_agent']}</span>
                <span class="{risk_class}">Risk: {data['risk_level']}</span>
            </div>
            <div style="font-size: 0.8em; color: gray; margin-top: 5px;">
                Guardrail: {data['guardrail_status']}
            </div>
            """, unsafe_allow_html=True)
            
            # Add to history
            st.session_state.messages.append({
                "role": "assistant", 
                "content": full_response,
                "metadata": {
                    "selected_agent": data["selected_agent"],
                    "risk_level": data["risk_level"],
                    "guardrail_status": data["guardrail_status"]
                }
            })
            
        except Exception as e:
            message_placeholder.markdown(f"❌ Error communicating with backend: {e}")
            st.error("Make sure the FastAPI server is running on port 8000.")
