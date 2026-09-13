# prompt_builder.py

EMOTION_TONE_MAP = {
    "lonely": "warmly and gently, making them feel heard and not alone",
    "confused": "calmly, patiently and reassuringly in very simple words",
    "sad": "with kindness and empathy, offering comfort",
    "anxious": "in a calm and grounding way to ease their concerns",
    "happy": "warmly and positively",
    "neutral": "in a friendly and welcoming way",
    "general": "helpfully and empathetically",
}

def build_prompt(user_input: str, emotion: str, memory_context: str) -> str:
    tone = EMOTION_TONE_MAP.get(emotion, EMOTION_TONE_MAP["general"])

    prompt = (
        f"You are a caring assistant for elderly people with dementia. "
        f"Respond {tone}. "
        f"Give a short, comforting reply in 1-2 sentences only. "
        f"Do not repeat the user's words. "
        f"Patient says: \"{user_input}\". "
        f"Your reply:"
    )
    return prompt