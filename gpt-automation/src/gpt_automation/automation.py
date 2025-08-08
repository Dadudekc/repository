"""Core automation features for GPT Automation."""
from __future__ import annotations

import os
from typing import Optional

try:  # pragma: no cover - simple import guard
    from openai import OpenAI
except Exception:  # pragma: no cover - openai may not be installed for tests
    OpenAI = None  # type: ignore


class AutomationEngine:
    """Simple wrapper around the OpenAI Chat Completions API."""

    def __init__(self, client: Optional[object] = None, model: str = "gpt-3.5-turbo") -> None:
        self.model = model
        if client is not None:
            self.client = client
            return
        if OpenAI is None:  # pragma: no cover - avoids import requirement during tests
            raise ImportError("openai package is required when no client is provided")
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")
        self.client = OpenAI(api_key=api_key)

    def run_prompt(self, prompt: str) -> str:
        """Send a prompt to the configured model and return the response text."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
