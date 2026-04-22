from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal

from .intent import detect_intent
from .rag import get_rag_context
from tools.lead_capture import mock_lead_capture

# ── State ─────────────────────────────────────────
class AgentState(TypedDict):
    user_input: str
    intent: str
    lead_info: dict
    response: str


# ── Node 1: Intent Classification ────────────────
def classify_intent(state: AgentState) -> AgentState:
    user_input = state["user_input"]
    state["intent"] = detect_intent(user_input)
    return state


# ── Node 2: Respond ──────────────────────────────
def respond(state: AgentState) -> AgentState:
    intent = state.get("intent")

    if intent == "greeting":
        state["response"] = "👋 Hi! Ask me about pricing or plans."

    elif intent == "query":
        state["response"] = get_rag_context()

    elif intent == "high_intent":
        lead = state.get("lead_info", {})

        if not lead.get("name"):
            state["response"] = "👤 What's your name?"
        elif not lead.get("email"):
            state["response"] = "📧 What's your email?"
        elif not lead.get("platform"):
            state["response"] = "📱 Which platform do you create content on?"
        else:
            return capture_lead(state)

    else:
        state["response"] = "I can help with pricing or plans."

    return state


# ── Node 3: Capture Lead ─────────────────────────
def capture_lead(state: AgentState) -> AgentState:
    lead = state["lead_info"]

    result = mock_lead_capture(
        lead["name"], lead["email"], lead["platform"]
    )

    state["response"] = f"🎉 Lead captured successfully! ID: {result['lead_id']}"
    return state


# ── Graph Routing ────────────────────────────────
def route(state: AgentState) -> Literal["respond", "__end__"]:
    return "respond"


# ── Build Graph ──────────────────────────────────
def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("classify_intent", classify_intent)
    graph.add_node("respond", respond)

    graph.add_edge(START, "classify_intent")
    graph.add_edge("classify_intent", "respond")
    graph.add_edge("respond", END)

    return graph.compile()


AGENT_GRAPH = build_graph()