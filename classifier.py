JAILBREAK_KEYWORDS = [
    "ignore", "bypass", "act as", "jailbreak", "override", "pretend", "dan"
]

TOXIC_KEYWORDS = [
    "kill", "hate", "die", "attack", "stupid", "useless", "destroy", "hurt"
]

PII_KEYWORDS = [
    "password", "credit card", "ssn", "bank", "secret", "confidential", "private"
]

def classify_prompt(prompt):
    prompt_lower = prompt.lower()
    confidence = 0.9

    if any(word in prompt_lower for word in JAILBREAK_KEYWORDS):
        return {"category": "jailbreak", "confidence": confidence}
    elif any(word in prompt_lower for word in TOXIC_KEYWORDS):
        return {"category": "toxic", "confidence": confidence}
    elif any(word in prompt_lower for word in PII_KEYWORDS):
        return {"category": "pii", "confidence": confidence}
    else:
        return {"category": "safe", "confidence": confidence}