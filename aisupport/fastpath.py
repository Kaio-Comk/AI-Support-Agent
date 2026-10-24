"""
Fast-path rule engine to answer confirmations, greetings, and thanks in <1ms without calling LLMs.
"""
import re

CONFIRMATION_PATTERNS = [
    r"^\s*(t[aá]\s*ok|ta\s*ok|t[aá]|ta|ok|blz|beleza|show|perfeito|entendi|combinado|certo)\s*[.!?]*\s*$",
    r"^\s*(valeu|obrigado|obg|agradecido|grato|muito obrigado)\s*[.!?]*\s*$",
    r"^\s*(bom dia|boa tarde|boa noite|ola|olá|oie|opa|e ai|e aí)\s*[.!?]*\s*$",
]

RESPONSES = {
    "confirmation": "Perfeito! Se precisar de mais alguma coisa, só chamar por aqui.",
    "thanks": "Por nada! Qualquer dúvida estamos à disposição.",
    "greeting": "Olá! Como posso ajudar você hoje?",
}

class FastPathMatcher:
    def match(self, text: str) -> str | None:
        t = text.strip().lower()
        if re.match(CONFIRMATION_PATTERNS[0], t):
            return RESPONSES["confirmation"]
        if re.match(CONFIRMATION_PATTERNS[1], t):
            return RESPONSES["thanks"]
        if re.match(CONFIRMATION_PATTERNS[2], t):
            return RESPONSES["greeting"]
        return None
