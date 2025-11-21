#!/usr/bin/env python3
from ai.engine import Assistant
import os

def main():
	use_openai = os.getenv("USE_OPENAI", "false").lower() in ("1", "true", "yes")
	try:
		assistant = Assistant(use_openai=use_openai)
	except RuntimeError as e:
		print("OpenAI integration requested but failed:", e)
		assistant = Assistant(use_openai=False)

	print("AI Assistant (type 'exit' or 'quit' to stop)")
	while True:
		try:
			text = input("> ")
		except (EOFError, KeyboardInterrupt):
			print()
			break

		resp = assistant.respond(text)
		print(resp)

		if text.strip().lower() in ("exit", "quit"):
			break


if __name__ == "__main__":
	main()

