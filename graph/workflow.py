from langgraph.graph import (
    StateGraph,
    START,
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition,
)

from graph.state import CustomerState
from graph.nodes import agent_node
from graph.memory import memory
from tools import TOOLS



def build_graph():

    graph = StateGraph(
        CustomerState
    )


    # Agent
    graph.add_node(
        "agent",
        agent_node
    )


    # Tools
    graph.add_node(
        "tools",
        ToolNode(TOOLS)
    )


    graph.add_edge(
        START,
        "agent"
    )


    graph.add_conditional_edges(
        "agent",
        tools_condition
    )


    graph.add_edge(
        "tools",
        "agent"
    )


    return graph.compile(
        checkpointer=memory
    )