# graph_definition.py

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, node, START, END

from front_end_agent import front_end_agent
from greeting_agent import greeting_agent

class ConversationState(TypedDict):
    """
    Minimal single-response state:
      - user_message: the user's latest input
      - last_response: the agent's latest response
    """
    user_message: str
    last_response: str

# Create the StateGraph
graph_builder = StateGraph(ConversationState)

# Register each node (no runner, no build())
graph_builder.add_node("front_end_agent", node(front_end_agent))
graph_builder.add_node("greeting_agent", node(greeting_agent))

# Flow: START -> front_end_agent -> greeting_agent -> END
graph_builder.add_edge(START, "front_end_agent")
graph_builder.add_edge("front_end_agent", "greeting_agent")
graph_builder.add_edge("greeting_agent", END)

graph = graph_builder
