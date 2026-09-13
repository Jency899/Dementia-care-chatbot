# model_handler.py

import random
import re

RESPONSE_BANK = {
    "lonely": [
        "You are not alone — I am right here with you, and I truly care about how you feel.",
        "It means a lot that you shared that with me. I'm here beside you, always.",
        "Loneliness can feel overwhelming, but please know I am here and I am listening.",
        "You matter deeply, and I'm glad you reached out. Let's talk — I'm not going anywhere.",
        "I'm so glad you told me. You are loved and you are not forgotten.",
    ],
    "confused": [
        "That's completely okay — let's slow down and take it one small step at a time together.",
        "It's alright to feel confused sometimes. I'm here to help you figure things out gently.",
        "Don't worry at all. Let's work through this together, slowly and carefully.",
        "Take your time — there's no rush. I'm right here to help you whenever you're ready.",
        "It's okay to forget things sometimes. I'll always be here to help you remember.",
    ],
    "sad": [
        "I'm truly sorry you're feeling sad today. Your feelings are completely valid and I'm here to listen.",
        "It's okay to feel sad. I'm here with you, and you don't have to go through this alone.",
        "Thank you for trusting me with how you feel. I care deeply about you.",
        "I hear you, and I'm so sorry you're hurting. Would you like to talk about what's on your mind?",
        "Feeling sad is okay. I'm right here beside you — you don't have to carry this alone.",
        "I'm so sorry you're going through this. I'm here and I'm listening with all my heart.",
    ],
    "anxious": [
        "Take a slow, deep breath with me. You are safe, and I am right here beside you.",
        "I understand you're feeling worried. Let's take this moment by moment — you're not alone.",
        "It's okay to feel anxious. Let's breathe together and take things one step at a time.",
        "You are safe right now. I'm here with you, and we'll get through this together.",
        "Everything is going to be okay. I'm right here — just focus on this moment with me.",
    ],
    "happy": [
        "That's truly wonderful to hear! Your happiness means so much — please tell me more!",
        "It warms my heart to hear you're feeling good today! What's been making you smile?",
        "That's so lovely! I'm really glad you're feeling this way. Let's celebrate this moment!",
        "Your joy is contagious! I'm so happy to hear that. Tell me what's making you feel this way!",
    ],
    "neutral": [
        "Hello! It's so lovely to hear from you. How are you feeling today?",
        "Hi there! I'm so glad you reached out. What's on your mind today?",
        "Good to see you! I'm here and ready to chat whenever you are.",
        "Welcome! I'm here for you. How has your day been so far?",
    ],
    "general": [
        "Thank you for sharing that with me. I'm here and I'm listening carefully.",
        "I hear you. Please know that I'm fully here for you — take all the time you need.",
        "I appreciate you talking to me. How can I best support you right now?",
        "I'm here with you. Would you like to tell me more about what you're experiencing?",
        "That's important, and I'm glad you shared it. I'm here to help however I can.",
    ]
}

# Context-aware responses for specific topics
CONTEXT_RESPONSES = {
    "family": [
        "It's so natural to miss your family. They love you very much.",
        "Family means everything. Would you like to tell me more about them?",
        "Missing loved ones is hard. I'm here to keep you company until you can see them.",
    ],
    "son": [
        "I understand you miss your son. That love between you is so special.",
        "Your son is lucky to have someone who cares so much. I'm here with you right now.",
        "Missing your son shows how much you love him. Would you like to talk about him?",
    ],
    "daughter": [
        "I can hear how much you love your daughter. That bond is truly beautiful.",
        "Missing your daughter is completely natural. I'm here to keep you company.",
        "Your daughter is so loved by you. Tell me more about her if you'd like.",
    ],
    "pain": [
        "I'm sorry you're in pain. Please let a caregiver know so they can help you.",
        "Your comfort matters deeply. Please tell a nurse or caregiver about your pain right away.",
    ],
    "food": [
        "It's important to eat well! Would you like me to remind a caregiver about your meal?",
        "Good nutrition keeps us strong. Let's make sure you're taken care of!",
    ],
    "memory": [
        "It's okay to forget sometimes — it happens to all of us. I'm here to help.",
        "Don't worry about forgetting. I'm here and we can figure things out together.",
    ],
    "home": [
        "Feeling at home is so important. Tell me what you miss most — I'd love to hear.",
        "Home holds such precious memories. Would you like to share some with me?",
    ],
    "medicine": [
        "It's very important to take your medicine. Please let your caregiver know if you need help.",
        "Your health comes first. Please speak to your nurse or caregiver about your medication.",
    ],
}

class ModelHandler:
    def __init__(self):
        print("Response system initialized ✅")
        self.model_loaded = True
        self.last_responses = []  # avoid repeating same response

    def _get_context_response(self, user_input: str) -> str:
        """Check for specific context keywords and return targeted response."""
        user_lower = user_input.lower()
        for keyword, responses in CONTEXT_RESPONSES.items():
            if keyword in user_lower:
                return random.choice(responses)
        return None

    def _get_emotion_response(self, emotion: str) -> str:
        """Get a non-repeating emotion-based response."""
        responses = RESPONSE_BANK.get(emotion, RESPONSE_BANK["general"])

        # Filter out recently used responses
        available = [r for r in responses if r not in self.last_responses]
        if not available:
            available = responses
            self.last_responses = []

        response = random.choice(available)

        # Track last 3 responses to avoid repetition
        self.last_responses.append(response)
        if len(self.last_responses) > 3:
            self.last_responses.pop(0)

        return response

    def generate(self, prompt: str, emotion: str = "general") -> str:
        """
        Smart response generation:
        1. Check for specific context (family, pain, food etc.)
        2. Fall back to emotion-based response
        """
        # Extract user input from prompt
        user_input = ""
        if "Patient says:" in prompt:
            user_input = prompt.split("Patient says:")[-1].strip(' ".')

        # Try context-aware response first
        context_response = self._get_context_response(user_input)
        if context_response:
            return context_response

        # Fall back to emotion-based response
        return self._get_emotion_response(emotion)