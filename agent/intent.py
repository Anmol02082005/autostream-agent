# agent package
def detect_intent(text):
    text = text.lower()

    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(x in text for x in ["price", "plan", "cost"]):
        return "query"

    elif any(x in text for x in ["buy", "subscribe", "start", "try", "i want"]):
        return "high_intent"

    return "other"