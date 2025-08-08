import sys
from pathlib import Path

# Ensure the src directory is on the Python path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from gpt_automation import AutomationEngine


class DummyCompletions:
    def create(self, model, messages):
        assert model == "gpt-3.5-turbo"
        assert messages[0]["content"] == "Hello"
        class Choice:
            message = type("msg", (), {"content": "Hi"})
        class Response:
            choices = [Choice()]
        return Response()


class DummyClient:
    chat = type("Chat", (), {"completions": DummyCompletions()})


def test_run_prompt_returns_response():
    engine = AutomationEngine(client=DummyClient())
    assert engine.run_prompt("Hello") == "Hi"
