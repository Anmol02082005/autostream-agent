"""
main.py
CLI entry point for the AutoStream Social-to-Lead agent.
Run with: python main.py
"""

import sys
from agent.graph import AGENT_GRAPH


def print_banner():
    print("\n" + "=" * 60)
    print("   🎬  AutoStream – Social-to-Lead AI Agent")
    print("=" * 60)
    print("Type your message and press Enter.")
    print("Type 'quit' or 'exit' to end the session.\n")


def initialize_state():
    return {
        "user_input": "",
        "intent": "unknown",
        "lead_info": {},
        "response": ""
    }


def run_agent():
    print_banner()
    state = initialize_state()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! 👋")
            sys.exit(0)

        if not user_input:
            continue

        if user_input.lower() in {"quit", "exit", "bye"}:
            print("\nBot: Thanks for chatting! 👋\n")
            break

        # ✅ Set user input
        state["user_input"] = user_input

        # ✅ Run graph
        state = AGENT_GRAPH.invoke(state)

        # ✅ Print response
        print(f"\nBot: {state['response']}\n")


if __name__ == "__main__":
    run_agent()