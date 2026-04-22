"""
agent/rag.py
RAG (Retrieval-Augmented Generation) pipeline for AutoStream knowledge base.
Uses simple keyword + semantic matching against local JSON knowledge base.
"""

import json
import os
from pathlib import Path


KB_PATH = Path(__file__).parent.parent / "knowledge_base" / "autostream_kb.json"


def load_knowledge_base() -> dict:
    """Load the AutoStream knowledge base from JSON."""
    with open(KB_PATH, "r") as f:
        return json.load(f)


def build_kb_context(kb: dict) -> str:
    """
    Flatten the knowledge base into a single readable context string
    that can be injected into the LLM system prompt.
    """
    lines = []

    # Company info
    co = kb["company"]
    lines.append(f"## Company: {co['name']}")
    lines.append(f"{co['description']}\n")

    # Pricing
    lines.append("## Pricing Plans")
    for key, plan in kb["pricing"].items():
        lines.append(f"\n### {plan['name']} – ${plan['price_monthly']}/month")
        for feat in plan["features"]:
            lines.append(f"  - {feat}")

    # Policies
    lines.append("\n## Policies")
    for policy_name, policy_text in kb["policies"].items():
        lines.append(f"- **{policy_name.replace('_', ' ').title()}**: {policy_text}")

    # FAQs
    lines.append("\n## FAQs")
    for faq in kb["faqs"]:
        lines.append(f"Q: {faq['q']}")
        lines.append(f"A: {faq['a']}\n")

    return "\n".join(lines)


def get_rag_context() -> str:
    """Public function: load KB and return formatted context string."""
    kb = load_knowledge_base()
    return build_kb_context(kb)
