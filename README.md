# 🤖 AI Support Agent (aisupport)

### Deterministic + Local LLM Customer Support Framework with Zero-VRAM Idle & HITL Silence

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://python.org)
[![Architecture](https://img.shields.io/badge/Architecture-Hybrid%20Deterministic%20%2B%20LLM-purple.svg)](https://github.com/Kaio-Comk/AI-Support-Agent)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Local%20Ollama-success.svg)](https://ollama.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Production customer support engine for Telegram, WhatsApp, and Web Chat.**  
*Combines sub-millisecond deterministic fast-paths with local LLMs (Ollama), automated VRAM unloading on idle, and Human-in-the-Loop (HITL) silence windows.*

---

## 🏗️ Architecture

```mermaid
flowchart TD
    Msg["💬 Inbound Customer Message"] --> Debounce["⏱️ Debounce Buffer (Wait for typing pause)"]
    Debounce --> HITL{"Human Operator active in chat?"}
    
    HITL -->|Yes| Silent["🤐 Stay Silent (24h Cooldown Window)"]
    HITL -->|No| FastPath{"Matches Fast-Path Regex? ('ok', 'obrigado')"}
    
    FastPath -->|Yes| Instant["⚡ Instant Reply (<1ms, 0 VRAM, 0 GPU)"]
    FastPath -->|No| VRAM["🧠 Wake local Ollama (Llama 3 / Qwen)"]
    
    VRAM --> LLM["📝 Generate Contextual Response"]
    LLM --> Sanitize["🧼 Style Sanitizer (Strip AI robotic tone)"]
    Sanitize --> Out["🚀 Send to Customer"]
    
    VRAM -.->|"Idle > 60s"| Unload["💤 Unload Model from GPU VRAM"]
```

---

## 📦 Installation

```bash
pip install git+https://github.com/Kaio-Comk/AI-Support-Agent.git
```

---

## 🚀 Quickstart

```python
from aisupport import FastPathMatcher, HITLSilenceTracker, DebounceBuffer, StyleSanitizer

# 1. Fast-path check
matcher = FastPathMatcher()
if canned := matcher.match("valeu!"):
    print(f"Replied without LLM: {canned}")

# 2. Human-in-the-Loop tracking
hitl = HITLSilenceTracker(cooldown_hours=24.0)
if human_sent_message:
    hitl.record_human_intervention(chat_id)
```

---

## 🛡️ License

MIT License. Extracted and decoupled from the NetHub customer support automation engine.
