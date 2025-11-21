import os
import datetime


class Assistant:
    """A small extendable assistant.

    - `use_openai=False` uses a simple rule-based responder.
    - `use_openai=True` will attempt to use the `openai` package and
      requires `OPENAI_API_KEY` in the environment.
    """

    def __init__(self, use_openai: bool = False):
        self.use_openai = bool(use_openai)

        if self.use_openai:
            try:
                import openai
            except Exception as e:
                raise RuntimeError("OpenAI package is not installed") from e

            key = os.getenv("OPENAI_API_KEY")
            if not key:
                raise RuntimeError("OPENAI_API_KEY environment variable is not set")

            self.openai = openai
            self.openai.api_key = key

    def respond(self, text: str) -> str:
        """Return a short response for the given text.

        This is intentionally simple so you can extend it later.
        """
        text = (text or "").strip()
        if not text:
            return "Please say something so I can help."

        # exit/quit immediate responses
        if text.lower().strip() in ("exit", "quit"):
            return "Goodbye!"

        # If configured, forward to OpenAI (best-effort)
        if self.use_openai:
            try:
                resp = self.openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": text}],
                    max_tokens=150,
                )
                return resp.choices[0].message.content.strip()
            except Exception as e:
                return f"OpenAI request failed: {e}"

        # Simple rule-based replies
        low = text.lower()

        if any(g in low for g in ("hello", "hi", "hey")):
            return "Hello! How can I help you today?"

        if "time" in low:
            return datetime.datetime.now().strftime("Current time: %Y-%m-%d %H:%M:%S")

        if "your name" in low or "who are you" in low:
            return "I'm an independent AI assistant you can extend."

        if low.endswith("?"):
            return "That's an interesting question — can you provide more context?"

        # Default echo-like reply
        return f"I heard you: {text}"
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
