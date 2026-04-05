from langgraph.graph import StateGraph, END
from graph.state import AgentState

from nodes.knowledge import knowledge_node
from nodes.estimator import estimator_node
from nodes.architect import architect_node
from nodes.refiner import refiner_node


def build_graph():
    """Builds sequential agent workflow"""

    graph = StateGraph(AgentState)

    # Add nodes
    graph.add_node("knowledge", knowledge_node)
    graph.add_node("estimator", estimator_node)
    graph.add_node("architect", architect_node)
    graph.add_node("refiner", refiner_node)

    # Define flow (sequential execution)
    graph.set_entry_point("knowledge")

    graph.add_edge("knowledge", "estimator")
    graph.add_edge("estimator", "architect")
    graph.add_edge("architect", "refiner")
    graph.add_edge("refiner", END)

    return graph.compile()
