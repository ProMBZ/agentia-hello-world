# greeting_agent.py

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

def greeting_agent(user_text: str) -> str:
    """
    Uses Google's Gemini 2.0 (ChatGoogleGenerativeAI) to handle greetings in any language.
    
    Special rules:
    1. If user says 'assalamu alaikum' (or variants), respond 'Wa alaikum as salam' + emojis.
    2. If recognized as a greeting (e.g. "Hi", "Hello", "你好"), respond in the same language with a
       friendly, warm tone (not just echoing).
    3. If not recognized as a greeting, fallback in English:
       "I only handle greetings right now. 🤖 Please try a greeting next time."
    """

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",   # or your actual Gemini 2.0 model
        temperature=0.7,
        max_tokens=512,
        api_key=os.getenv("GEMINI_API_KEY"),  # loaded from .env or environment
    )

    system_prompt = """You are a specialized Greeting Agent that can handle greetings in any language.

Rules:
1. If the user says "assalamu alaikum" (or variants), respond: "Wa alaikum as salam" plus emojis.
2. If it's any other greeting, respond in the same language with a friendly message + emojis.
   For example, if user says "Hi", you might say "Hi there! 👋 How can I help?"
   Do NOT simply echo the user's greeting verbatim.
3. If not recognized as a greeting, respond:
   "I only handle greetings right now. 🤖 Please try a greeting next time."
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_text),
    ]

    response = llm(messages)
    return response.content.strip()
