from langgraph.graph import(
    StateGraph,
    START,
    END
)
import graph
from graph.state import CustomerState

from graph.nodes import(
    intent_node,
    agent_node
)

def create_customer_graph():
    graph = StateGraph(
        CustomerState
    )
    # add node
    graph.add_node("intent",intent_node)
    graph.add_node("agent",agent_node)
    # add edge
    graph.add_edge(START,"intent")
    graph.add_edge("intent","agent")
    graph.add_edge("agent",END)
    return graph.compile()
    