"""
Cleans robotic LLM styling, removing AI self-introductions, vocative loops, and markdown artifacts.
"""
import re

class StyleSanitizer:
    @staticmethod
    def clean(text: str) -> str:
        s = text.strip()
        s = re.sub(r"^(sou (o|um) assistente virtual[^.\n]*[.\n])", "", s, flags=re.IGNORECASE)
        s = re.sub(r"^#+\s*", "", s, flags=re.MULTILINE)
        return s.strip()
