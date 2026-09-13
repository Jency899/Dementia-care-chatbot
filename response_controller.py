# response_controller.py

import re
import random

UNSAFE_PATTERNS = [
    r"\b(kill|harm|hurt|die|death|suicide|medication dosage)\b",
    r"(I don't know what|I cannot|as an AI|I am an AI|language model)",
    r"(http[s]?://|www\.)",
]

FALLBACK_RESPONSES = {
    "lonely": [
        "You are not alone — I am right here with you, and I truly care about how you feel.",
        "It means a lot that you shared that with me. I'm here beside you, always.",
        "Loneliness can feel overwhelming, but please know I am here and I am listening.",
        "You matter deeply, and I'm glad you reached out. Let's talk — I'm not going anywhere.",
    ],
    "confused": [
        "That's completely okay — let's slow down and take it one small step at a time together.",
        "It's alright to feel confused sometimes. I'm here to help you figure things out gently.",
        "Don't worry at all. Let's work through this together, slowly and carefully.",
        "Take your time — there's no rush. I'm right here to help you whenever you're ready.",
    ],
    "sad": [
        "I'm truly sorry you're feeling this way. Your feelings are completely valid and I'm here to listen.",
        "It's okay to feel sad. I'm here with you, and you don't have to go through this alone.",
        "Thank you for trusting me with how you feel. I care about you and I'm here for you.",
        "I hear you, and I'm so sorry you're hurting. Would you like to talk about what's on your mind?",
    ],
    "anxious": [
        "Take a slow, deep breath with me. You are safe, and I am right here beside you.",
        "I understand you're feeling worried. Let's take this moment by moment — you're not alone.",
        "It's okay to feel anxious. Let's breathe together and take things one step at a time.",
        "You are safe right now. I'm here with you, and we'll get through this together.",
    ],
    "happy": [
        "That's truly wonderful to hear! Your happiness means so much — please tell me more!",
        "It warms my heart to hear you're feeling good today! What's been making you smile?",
        "That's so lovely! I'm really glad you're feeling this way. Let's celebrate this moment!",
    ],
    "neutral": [
        "Hello! It's so lovely to hear from you. How are you feeling today?",
        "Hi there! I'm so glad you reached out. What's on your mind today?",
        "Good to see you! I'm here and ready to chat whenever you are.",
    ],
    "general": [
        "Thank you for sharing that with me. I'm here and I'm listening carefully.",
        "I hear you. Please know that I'm fully here for you — take all the time you need.",
        "I appreciate you talking to me. How can I best support you right now?",
        "I'm here with you. Would you like to tell me more about what you're experiencing?",
    ]
}


def is_invalid(text: str) -> bool:
    text = text.strip()
    if not text:
        return True
    if re.fullmatch(r'\[?\d{1,2}:\d{2}\]?', text):
        return True
    if len(text.split()) < 4:
        return True
    if re.fullmatch(r'[^a-zA-Z0-9]+', text):
        return True
    return False


def is_echo(response: str, user_input: str) -> bool:
    if not user_input:
        return False
    response_clean = response.lower().strip(" .")
    user_clean = user_input.lower().strip(" .")
    if user_clean in response_clean:
        return True
    user_words = set(user_clean.split())
    response_words = set(response_clean.split())
    if len(user_words) == 0:
        return False
    overlap = len(user_words & response_words) / len(user_words)
    if overlap > 0.7:
        return True
    return False


def get_fallback(emotion: str) -> str:
    responses = FALLBACK_RESPONSES.get(
        emotion,
        FALLBACK_RESPONSES["general"]
    )
    return random.choice(responses)


def clean_response(
    response: str,
    emotion: str = "general",
    user_input: str = ""
) -> str:
    if not response or not response.strip():
        return get_fallback(emotion)

    response = re.sub(
        r"^(Response:|Answer:|Bot:|Assistant:|System:)\s*",
        "", response, flags=re.IGNORECASE
    ).strip()

    for pattern in UNSAFE_PATTERNS:
        if re.search(pattern, response, re.IGNORECASE):
            return get_fallback(emotion)

    if user_input and is_echo(response, user_input):
        return get_fallback(emotion)

    if is_invalid(response):
        return get_fallback(emotion)

    sentences = re.split(r'(?<=[.!?])\s+', response.strip())
    sentences = [s.strip() for s in sentences if s.strip()]

    seen = set()
    unique = []
    for s in sentences:
        if s.lower() not in seen:
            seen.add(s.lower())
            unique.append(s)

    result = " ".join(unique[:2])

    if is_invalid(result) or (user_input and is_echo(result, user_input)):
        return get_fallback(emotion)

    return result