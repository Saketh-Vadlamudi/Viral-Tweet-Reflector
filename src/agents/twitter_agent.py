from typing import TypedDict
from langgraph.graph import END, StateGraph
from src.agents.nodes import generation_node, reflection_node


# Define state schema properly using TypedDict
class TweetState(TypedDict):
    original_tweet: str
    generated_tweet: str
    feedback: str


def build_graph():
    builder = StateGraph(TweetState)

    builder.add_node("generate", generation_node)
    builder.add_node("reflect", reflection_node)

    # Set the entry point
    builder.set_entry_point("generate")

    # Define the conditional edge for reflection
    def decide_to_end_or_regenerate(state: TweetState):
        if state.get("feedback") == "stop":
            return END
        else:
            return "generate" # Loop back to generate for refinement

    # Add edges
    builder.add_edge("generate", "reflect") # After generating, always reflect
    builder.add_conditional_edges("reflect", decide_to_end_or_regenerate) # After reflecting, decide to end or regenerate

    return builder.compile()