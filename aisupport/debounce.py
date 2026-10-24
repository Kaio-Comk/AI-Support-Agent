"""
Debounce buffer that aggregates fragmented multiline customer messages into a single prompt.
"""
import time

class DebounceBuffer:
    def __init__(self, debounce_seconds: float = 4.0):
        self.debounce_seconds = debounce_seconds
        self.buffers: dict[str | int, list[str]] = {}
        self.last_seen: dict[str | int, float] = {}

    def append(self, chat_id: str | int, text: str) -> None:
        self.buffers.setdefault(chat_id, []).append(text.strip())
        self.last_seen[chat_id] = time.time()

    def should_flush(self, chat_id: str | int) -> bool:
        if chat_id not in self.last_seen:
            return False
        return (time.time() - self.last_seen[chat_id]) >= self.debounce_seconds

    def flush(self, chat_id: str | int) -> str | None:
        msgs = self.buffers.pop(chat_id, None)
        self.last_seen.pop(chat_id, None)
        if not msgs:
            return None
        return "\n".join(msgs)
