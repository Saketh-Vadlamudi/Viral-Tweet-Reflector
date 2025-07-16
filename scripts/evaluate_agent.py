import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.twitter_agent import build_graph
from langchain_core.messages import HumanMessage # Still useful if you want to explicitly pass messages to your chains
import json

test_inputs = [
    "Make this tweet better: @LangChainAI's tool calling is underrated.",
    "Write a viral tweet about LangGraph's new composable agent flow.",
    "Improve: GPT-4 is good, but slow. Groq is fast but small. Thoughts?",
]

graph = build_graph()

results = []

for i, prompt in enumerate(test_inputs):
    # Prepare the initial state dictionary correctly, matching TweetState
    initial_state_for_graph = {
        "original_tweet": prompt, # The prompt string goes into 'original_tweet'
        "generated_tweet": "",    # Initialize empty
        "feedback": ""            # Initialize empty
    }

    # Invoke the graph with the correctly structured initial state
    result = graph.invoke(initial_state_for_graph)

    # Ensure you're accessing the final generated tweet from the result dictionary
    results.append({
        "input": prompt,
        "output": result["generated_tweet"], # Access generated_tweet from the final state dict
    })
    print(f"\n✅ [{i+1}] Input:\n{prompt}\n\n💡 Output:\n{result['generated_tweet']}")

with open("eval_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\n📁 Results saved to eval_results.json")