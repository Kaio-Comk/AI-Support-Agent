"""
Human-in-the-Loop (HITL) manager. If a human operator replies in the chat,
the bot automatically silences itself for a configurable cooldown window.
"""
import time

class HITLSilenceTracker:
    def __init__(self, cooldown_hours: float = 24.0):
        self.cooldown_seconds = cooldown_hours * 3600.0
        self.muted_until: dict[str | int, float] = {}

    def record_human_intervention(self, chat_id: str | int) -> None:
        """Mark that a human agent sent a message in this chat."""
        self.muted_until[chat_id] = time.time() + self.cooldown_seconds

    def is_muted(self, chat_id: str | int) -> bool:
        """Check if AI should remain silent."""
        exp = self.muted_until.get(chat_id)
        if not exp:
            return False
        if time.time() < exp:
            return True
        del self.muted_until[chat_id]
        return False
