import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.twitter_agent import build_graph
from langgraph.pregel import GraphRecursionError

app = FastAPI()
graph = build_graph()

class TweetRequest(BaseModel):
    tweet: str

@app.post("/improve_tweet")
def improve_tweet(data: TweetRequest):
    state = {
        "original_tweet": data.tweet,
        "generated_tweet": data.tweet,
        "feedback": "",
        "iterations": 0
    }

    try:
        result = graph.invoke(state, config={"recursion_limit": 25})
        return {
            "original_tweet": data.tweet,
            "improved_tweet": result.get("generated_tweet", ""),
            "feedback": result.get("feedback", "")
        }
    except GraphRecursionError as gre:
        return {
            "error": "Recursion limit reached. Check stop conditions in your graph.",
            "details": str(gre)
        }
    except Exception as e:
        return {
            "error": "Unexpected error occurred.",
            "details": str(e)
        }

@app.get("/")
def health():
    return {"status": "ok"}
