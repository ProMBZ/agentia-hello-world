# front_end_agent.py

from greeting_agent import greeting_agent

def front_end_agent(user_text: str) -> str:
    """
    The Front-End Orchestration Agent:
    - Receives user_text
    - Delegates to the Greeting Agent
    - Returns the Greeting Agent's reply
    """
    return greeting_agent(user_text)
