# greeting_agent.py

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

def greeting_agent(user_text: str) -> str:
    """
    Uses Google's Gemini 2.0 to handle greetings in any language.

    Special logic:
    1) If user says 'assalamu alaikum', respond with 'Wa alaikum as salam' + emojis.
    2) If recognized as a greeting (e.g. "Hi", "Hello", "你好"), respond in the same language
       with a friendly tone + emojis (not just echo).
    3) Otherwise, fallback in English:
       "I only handle greetings right now. 🤖 Please try a greeting next time."
    """

    # Create the Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",    # or the correct Gemini 2.0 variant
        temperature=0.7,
        max_tokens=512,
        api_key=os.getenv("GEMINI_API_KEY")  # from .env
    )

    system_prompt = """You are a specialized Greeting Agent that can handle greetings in any language.

Rules:
1. If user says "assalamu alaikum" (or variants), respond "Wa alaikum as salam" + emojis.
2. Otherwise, if recognized as a greeting, respond in that same language with a warm, friendly tone (add emojis).
3. If not recognized as a greeting, fallback in English: "I only handle greetings right now. 🤖 Please try a greeting next time."
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_text),
    ]

    response = llm(messages)
    return response.content.strip()
