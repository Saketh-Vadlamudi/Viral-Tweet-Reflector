from dotenv import load_dotenv
load_dotenv()

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.twitter_agent import build_graph

print("🤖 Running Viral Tweet Agent...")

graph = build_graph()

input_data = {
    "original_tweet": "Make this tweet better: @LangChainAI's tool calling is underrated.",
    "generated_tweet": "",
    "feedback": ""
}

print("🚀 Invoking agent with input...")
result = graph.invoke(input_data, config={"recursion_limit": 10})

print("✅ Final Output:\n", result)

final_state = graph.invoke(input_data)

print("\n✅ Final Output:\n")
print(final_state["generated_tweet"])
