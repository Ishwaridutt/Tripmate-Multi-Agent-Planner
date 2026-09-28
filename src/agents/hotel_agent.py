from langchain_core.messages import (
    AIMessage
)
from tools.tavily_tool import tavily_search
from models.state import TravelState



# Hotel Agent


def hotel_agent(state: TravelState):
    query = f"Best hotels for {state['user_query']}"
    hotel_results = tavily_search(query)

    print('\nHotel agent result: ', hotel_results)
    print('\nTotal LLM Calls: ', state.get("llm_calls"))

    return {
        "hotel_results": hotel_results,
        "messages": [
            AIMessage(content="Hotel information fetched.")
        ],
        "llm_calls": state.get("llm_calls", 0) + 1
    }



