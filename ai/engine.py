"""Simple, extendable AI assistant engine.

Provides a rule-based `Assistant` with optional OpenAI integration.
"""
from typing import Optional


class Assistant:
    def __init__(self, use_openai: bool = False):
        self.use_openai = use_openai
        self._openai = None
        if use_openai:
            try:
                import openai

                self._openai = openai
            except Exception as exc:  # pragma: no cover - environment dependent
                raise RuntimeError(
                    "openai package not installed or failed to import"
                ) from exc

    def _rule_response(self, text: str) -> str:
        t = (text or "").strip().lower()
        if not t:
            return "Please say something so I can help."

        greetings = ("hello", "hi", "hey")
        if any(g in t for g in greetings):
            return "Hello! How can I help you today?"

        if "help" in t:
            return (
                "I can chat, answer simple questions, and optionally use OpenAI when enabled."
            )

        if "your name" in t or "who are you" in t:
            return "I'm your local AI assistant."

        if t in ("exit", "quit"):
            return "Goodbye!"

        return "Sorry, I don't know how to help with that yet."

    def _openai_response(self, text: str) -> str:  # pragma: no cover - optional
        # Uses the OpenAI Completion API as a simple example. Requires
        # `OPENAI_API_KEY` env var and `openai` package installed.
        resp = self._openai.Completion.create(
            engine="text-davinci-003", prompt=text, max_tokens=150
        )
        return resp.choices[0].text.strip()

    def respond(self, text: Optional[str]) -> str:
        """Return a response string for the provided input text.

        If OpenAI integration is enabled, attempt to use it; otherwise fall
        back to rule-based responses.
        """
        if self.use_openai and self._openai is not None:
            try:
                return self._openai_response(text)
            except Exception:
                # Fall back to rule-based behavior on any error
                return self._rule_response(text)

        return self._rule_response(text)
