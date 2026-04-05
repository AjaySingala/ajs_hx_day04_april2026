from langgraph.graph import StateGraph, END
from graph.state import AgentState

from nodes.knowledge import knowledge_node
from nodes.estimator import estimator_node
from nodes.architect import architect_node
from nodes.refiner import refiner_node


def build_graph():
    """Builds sequential agent workflow"""

    graph = StateGraph(AgentState)

    # TODO: Add nodes for:
    # knowledge, estimator, architect, refiner.
    ___

    # TODO: Set the knwoledge node as entry point.
    ___

    # TODO: Define the edges (flow) between the nodes.
    ___

    # TODO: Set the refiner node as the exit point.
    ___

    return graph.compile()
