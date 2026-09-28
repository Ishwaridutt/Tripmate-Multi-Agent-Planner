
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from models.state import TravelState
from clients.llm_client import llm_client


# =========================
# Itinerary Agent
# =========================

def itinerary_agent(state: TravelState):
    prompt = f"""
Create a complete travel itinerary.

User Query:
{state['user_query']}

Flight Results:
{state['flight_results']}

Hotel Results:
{state['hotel_results']}

Make the itinerary practical, budget-aware, and easy to follow.
"""

    print('\nItinerary agent prompt: ', prompt)

    response = llm_client.invoke([
        SystemMessage(content="You are an expert travel planner."),
        HumanMessage(content=prompt)
    ])

    print('\nItinerary agent result: ', response.content)
    print('\nTotal LLM Calls: ', state.get("llm_calls"))

    return {
        "itinerary": response.content,
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1
    }



