from langgraph.graph import StateGraph, START, END
from clients.sql_lite_db_client import checkpointer

from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.itinerary_agent import itinerary_agent
from agents.summary_agent import summary_agent
from models.state import TravelState


# Build Graph
graph = StateGraph(TravelState)
graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent", itinerary_agent)
graph.add_node("summary_agent", summary_agent)

# define path
graph.add_edge(START, "flight_agent")
graph.add_edge("flight_agent", "hotel_agent")
graph.add_edge("hotel_agent", "itinerary_agent")
graph.add_edge("itinerary_agent", "summary_agent")
graph.add_edge("summary_agent", END)

travel_graph = graph.compile(
    checkpointer=checkpointer
)
