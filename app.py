# app.py

import streamlit as st
import os
from dotenv import load_dotenv
from front_end_agent import front_end_agent

def main():
    # 1) Load environment variables (GEMINI_API_KEY)
    load_dotenv()

    st.title("👋 Agentia Hello World")

    st.markdown("""
    **Flow**:
    1. User enters a message (e.g., 'Hi', 'assalamu alaikum', '你好').
    2. The front-end agent delegates to the greeting agent.
    3. The greeting agent uses Gemini 2.0 to respond in the same language or fallback in English.
    """)

    if "last_response" not in st.session_state:
        st.session_state["last_response"] = ""

    user_text = st.text_input("Type your greeting here:")
    if st.button("Send"):
        # The front-end agent calls the greeting agent
        answer = front_end_agent(user_text)
        st.session_state["last_response"] = answer

    # Show only the final answer
    st.write("### Answer:")
    st.write(st.session_state["last_response"])

if __name__ == "__main__":
    main()
