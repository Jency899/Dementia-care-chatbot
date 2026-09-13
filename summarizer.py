# summarizer.py

import os
import json
from datetime import datetime

SUMMARY_DIR = "data/summaries"

class DailySummarizer:
    """
    Generates and stores daily conversation summaries.
    """

    def __init__(self):
        os.makedirs(SUMMARY_DIR, exist_ok=True)

    def generate_summary(self, history: list) -> str:
        """
        Generates a plain text summary from conversation history.
        """
        if not history:
            return "No conversation recorded today."

        emotion_counts = {}
        key_moments = []

        for turn in history:
            emotion = turn.get("emotion", "general")
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

            # Pick notable turns
            if emotion in ["lonely", "sad", "confused", "anxious"]:
                key_moments.append(
                    f"- [{turn['timestamp']}] User felt {emotion}: "
                    f"\"{turn['user'][:60]}...\""
                    if len(turn['user']) > 60
                    else f"- [{turn['timestamp']}] User felt {emotion}: "
                    f"\"{turn['user']}\""
                )

        # Build summary text
        total_turns = len(history)
        dominant_emotion = (
            max(emotion_counts, key=emotion_counts.get)
            if emotion_counts else "general"
        )

        summary_lines = [
            f"📅 Daily Summary — {datetime.now().strftime('%Y-%m-%d')}",
            f"Total interactions: {total_turns}",
            f"Dominant emotional state: {dominant_emotion}",
            "",
            "Emotion breakdown:",
        ]

        for emotion, count in emotion_counts.items():
            summary_lines.append(f"  • {emotion}: {count} time(s)")

        if key_moments:
            summary_lines.append("")
            summary_lines.append("Key emotional moments:")
            summary_lines.extend(key_moments[:5])  # top 5 moments

        return "\n".join(summary_lines)

    def save_summary(self, history: list) -> str:
        """
        Saves daily summary to a JSON file.
        Returns the summary text.
        """
        summary_text = self.generate_summary(history)
        date_str = datetime.now().strftime("%Y-%m-%d")
        filepath = os.path.join(SUMMARY_DIR, f"summary_{date_str}.json")

        data = {
            "date": date_str,
            "summary": summary_text,
            "history": history
        }

        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

        return summary_text

    def load_latest_summary(self) -> str:
        """
        Loads the most recent saved summary.
        """
        files = sorted(os.listdir(SUMMARY_DIR), reverse=True)
        if not files:
            return "No previous summaries found."

        latest = os.path.join(SUMMARY_DIR, files[0])
        with open(latest, "r") as f:
            data = json.load(f)

        return data.get("summary", "No summary available.")