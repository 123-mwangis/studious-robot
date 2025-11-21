# Studious Robot — Minimal AI Assistant

This repository contains a minimal, extendable AI assistant implemented in Python.

Quick start

1. Run locally (rule-based, no external API required):

```bash
python Main.py
```

2. Enable OpenAI integration (optional):

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="..."
export USE_OPENAI=true
python Main.py
```

Files

- `Main.py`: CLI runner for the assistant.
- `ai/engine.py`: Assistant implementation (rule-based + optional OpenAI).
- `requirements.txt`: Optional dependencies.

Next steps

- Improve conversational logic or add an LLM backend.
- Add persistent context memory.
- Add web or API front-end.
# studious-robot
Ai software that turns text to anime
