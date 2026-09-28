from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)
from models.state import TravelState
from clients.llm_client import llm_client


# =========================
# Final Response Agent
# =========================

def summary_agent(state: TravelState):
    summary_prompt = f"""
Generate the final travel response for the user.

User Request:
{state['user_query']}

Flights:
{state['flight_results']}

Hotels:
{state['hotel_results']}

Itinerary:
{state['itinerary']}

Format the final answer beautifully using these sections:

1. Trip Summary
2. Flight Information
3. Hotel Suggestions
4. Day-by-Day Itinerary
5. Estimated Budget
6. Final Recommendations

Important:
- Be clear and practical.
- Mention that live flight API may not provide ticket prices if pricing is unavailable.
- Keep the response useful for real travel planning.
""" 

    print('Summary agent prompt: ', summary_prompt)

    response = llm_client.invoke([
        SystemMessage(content="You are a professional AI travel booking assistant."),
        HumanMessage(content=summary_prompt)
    ])

    print('Summary agent response: ', response)


    return {
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1
    }




