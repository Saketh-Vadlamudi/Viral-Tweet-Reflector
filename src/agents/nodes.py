import re # Add this import at the top of src/agents/nodes.py
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from src.utils.prompt_templates import generation_chain, reflection_chain

llm = ChatGroq(model="llama3-8b-8192")

def generation_node(state: dict) -> dict:
    from src.utils.prompt_templates import generation_chain
    # Your current generation_node logic (assuming it's still using original_tweet)
    response = generation_chain.invoke({"messages": [HumanMessage(content=state["original_tweet"])]})
    return {
        **state,
        "generated_tweet": response.content,
        "feedback": ""  # reset feedback
    }

def reflection_node(state: dict) -> dict:
    from src.utils.prompt_templates import reflection_chain

    tweet = state["generated_tweet"]
    reflection = reflection_chain.invoke({"messages": [HumanMessage(content=tweet)]}) # Ensure input is a HumanMessage
    print("🪞 Reflection:", reflection.content)

    content = reflection.content.lower()
    feedback = "continue" # Default to continue

    # Check for explicit "looks good" type phrases
    explicit_stop_phrases = [
        "looks good", "no further changes", "perfect", "final version",
        "good to go", "solid", "excellent", "great job"
    ]
    if any(phrase in content for phrase in explicit_stop_phrases):
        feedback = "stop"

    # Check for grades (e.g., "grade: a", "grade: b+", "grade: 8", "grade: 9")
    # Matches "grade:" followed by optional spaces, then A, A-, B+, or a digit 8/9
    grade_match = re.search(r"grade:\s*(a|a-|b\+|[89])", content)
    if grade_match:
        grade = grade_match.group(1)
        # You can refine this logic if you have specific grade cutoffs
        if grade in ["a", "a-", "b+", "8", "9"]:
            feedback = "stop"

    # Check for X/10 scores (e.g., "8/10", "8.5/10", "9/10")
    # Matches numbers followed by /10 or out of 10
    score_match = re.search(r"(\d+(\.\d+)?)\s*(?:/10|out of 10)", content)
    if score_match:
        score = float(score_match.group(1))
        if score >= 8.0: # If the score is 8 or higher, consider it a stop
            feedback = "stop"

    return {
        **state,
        "feedback": feedback
    }