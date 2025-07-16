from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=256
)

# Prompt for reflection
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Provide detailed critique and suggestions to improve virality, clarity, or style.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Prompt for tweet generation
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a tech Twitter influencer assistant. Generate the most viral and engaging tweet for the given request.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Chains
generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm
