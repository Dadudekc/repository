# Trading Platform

Modular framework for building and deploying trading tools.

## Directory Structure
- `core-engine/` – shared trading bot engines
- `plugins/` – strategy plugins
- `analytics/` – performance metrics
- `lead-generation/` – outreach tools
- `web-ui/` – interface components

## Environment Setup
1. Create a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r environment/requirements.txt
   ```
3. Copy `environment/env.example` to `.env` and add your API keys.

## Status
Project skeleton with initial environment scaffolding.

## Progress
- Added `pytest` to requirements and created a basic import test for `pandas`, `numpy`, and `yfinance`.
- Initial tests pass once dependencies are installed.
- Future consolidation: migrate strategy modules from `tbow-tactics` and machine learning utilities from `machine-learning-model-maker` into `core-engine`.
