# memory_module.py

from datetime import datetime
from typing import Optional

class MemoryModule:
    """
    Short-term memory to maintain conversational continuity.
    Stores recent user emotions and key facts across turns.
    """

    def __init__(self, max_turns: int = 10):
        self.max_turns = max_turns
        self.history = []          # list of (user_msg, bot_response, emotion)
        self.last_emotion = "general"
        self.user_name: Optional[str] = None
        self.noted_facts = []      # e.g. ["user mentioned feeling lonely"]

    def update(self, user_msg: str, emotion: str, response: str = ""):
        """Add a new turn to memory."""
        self.last_emotion = emotion

        # Extract simple facts
        if "name is" in user_msg.lower():
            parts = user_msg.lower().split("name is")
            if len(parts) > 1:
                name = parts[1].strip().split()[0].capitalize()
                self.user_name = name
                self.noted_facts.append(f"User's name is {name}")

        self.history.append({
            "timestamp": datetime.now().strftime("%H:%M"),
            "user": user_msg,
            "response": response,
            "emotion": emotion
        })

        # Keep only last N turns
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context_summary(self) -> str:
        """Returns a brief context string for prompt building."""
        if not self.history:
            return ""

        parts = []
        if self.user_name:
            parts.append(f"User's name: {self.user_name}.")

        # Last 3 turns
        recent = self.history[-3:]
        for turn in recent:
            parts.append(
                f"[{turn['timestamp']}] User ({turn['emotion']}): "
                f"{turn['user'][:80]}"
            )

        return " | ".join(parts)

    def get_last_emotion(self) -> str:
        return self.last_emotion

    def get_full_history(self):
        return self.history

    def clear(self):
        self.history = []
        self.noted_facts = []
        self.last_emotion = "general"