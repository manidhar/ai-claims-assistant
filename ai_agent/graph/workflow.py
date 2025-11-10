from langgraph.graph import StateGraph, START, END
from graph.state_schema import ClaimState
from graph.nodes.parser import document_parser
from graph.nodes.vision_damage import vision_damage_assessment
from graph.nodes.policy_verifier import policy_verifier
from graph.nodes.claim_assessor import claim_assessment


def build_graph():
    graph = StateGraph(ClaimState)

    graph.add_node("parser", document_parser)
    graph.add_node("vision", vision_damage_assessment)
    graph.add_node("policy", policy_verifier)
    graph.add_node("assessor", claim_assessment)

    graph.add_edge(START, "parser")
    graph.add_edge("parser", "vision")
    graph.add_edge("vision", "policy")
    graph.add_edge("policy", "assessor")
    graph.add_edge("assessor", END)

    return graph