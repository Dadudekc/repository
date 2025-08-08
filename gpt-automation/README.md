# GPT Automation

Toolkit for building GPT-driven automation workflows.

## Environment Setup
Run the automated setup script:

```bash
python environment/setup.py
```

This creates a virtual environment, installs dependencies, and copies
`environment/env.example` to `.env` if it does not already exist.

## Usage
```python
from gpt_automation import AutomationEngine

engine = AutomationEngine()
print(engine.run_prompt("Hello"))
```

## Status
Basic environment automation and core features available.
