# emotion_detector.py

EMOTION_KEYWORDS = {
    "lonely": ["lonely", "alone", "no one", "nobody", "isolated", "miss"],
    "confused": ["confused", "forget", "forgot", "lost", "don't remember",
                 "can't remember", "what was", "where am"],
    "sad": ["sad", "cry", "crying", "unhappy", "depressed", "upset", "tears"],
    "anxious": ["worried", "scared", "afraid", "nervous", "anxiety", "panic"],
    "happy": ["happy", "good", "great", "wonderful", "nice", "joy", "better"],
}

def detect_emotion(text: str) -> str:
    """
    Detects emotion from user input using keyword matching.
    Returns one of: lonely, confused, sad, anxious, happy, neutral
    """
    text_lower = text.lower()

    for emotion, keywords in EMOTION_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return emotion

    # Check for greetings
    greetings = ["hello", "hi", "hey", "good morning", "good evening",
                 "good afternoon"]
    for g in greetings:
        if g in text_lower:
            return "neutral"

    return "general"