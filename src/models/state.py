import operator
from typing import TypedDict, Annotated
from pydantic import BaseModel

from langchain_core.messages import (
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
)


# LangGraph State Schemas

class TravelState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_results: str
    hotel_results: str
    itinerary: str
    llm_calls: int




# FastAPI State Schemas

class TravelRequest(BaseModel):
    message: str
    thread_id: str | None = None


