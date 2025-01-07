# app.py

import streamlit as st
import os
from dotenv import load_dotenv
from front_end_agent import front_end_agent

def main():
    # 1) Load .env variables (e.g., GEMINI_API_KEY)
    load_dotenv()

    st.title("👋 Agentia Hello World")

    st.markdown("""
    - Special-cases "assalamu alaikum" → "Wa alaikum as salam" + emojis
    - For any other greeting ("Hi", "你好"), replies in that language with a warm tone
    - Otherwise, fallback in English:
      "I only handle greetings right now. 🤖 Please try a greeting next time."
    """)

    # We track the last response, but won't label it "Last Response" in the UI
    if "last_response" not in st.session_state:
        st.session_state["last_response"] = ""

    # User input box
    user_text = st.text_input("Type your greeting here:")

    # Button to send the message
    if st.button("Send"):
        response = front_end_agent(user_text)
        st.session_state["last_response"] = response

    # Display ONLY the final answer, with no extra label
    # Removing any heading like "### Last Response:"
    st.write("### Answer:")
    st.write(st.session_state["last_response"])


if __name__ == "__main__":
    main()
