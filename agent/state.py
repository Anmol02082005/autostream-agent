"""
agent/state.py
State schema for the AutoStream LangGraph agent.
"""

from typing import Annotated, TypedDict, Optional, List
from langgraph.graph.message import add_messages


class LeadInfo(TypedDict, total=False):
    """Collected lead information, filled incrementally."""
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]


class AgentState(TypedDict):
    """
    Full conversation state persisted across every graph node.

    Fields:
        messages      : Full chat history (Human + AI turns), managed by LangGraph.
        intent        : Latest classified intent label.
        lead_info     : Incrementally collected lead fields.
        lead_captured : True once mock_lead_capture has been called successfully.
        turn_count    : Number of completed conversation turns.
    """
    messages: Annotated[list, add_messages]
    intent: str                        # "greeting" | "inquiry" | "high_intent" | "unknown"
    lead_info: LeadInfo
    lead_captured: bool
    turn_count: int
