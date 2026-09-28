from langchain_core.messages import (
    AIMessage
)
from tools.flight_tool import search_flights
from models.state import TravelState


# =========================
# Flight Agent
# =========================

def flight_agent(state: TravelState):
    query = state["user_query"]
    flight_data = search_flights(query)

    print('\nFlight agent result: ', flight_data)
    print('\nTotal LLM Calls: ', state.get("llm_calls"))

    return {
        "flight_results": flight_data,
        "messages": [
            AIMessage(content="Flight results fetched.")
        ],
        "llm_calls": state.get("llm_calls", 0) + 1
    }


