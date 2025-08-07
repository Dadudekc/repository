# Trading Platform Monorepo

This directory consolidates all trading-related projects into a single monorepo. Projects are organized by role to simplify development and future integration.

## Structure
- `core/` – base trading engine components derived from the original *trading-robot-plug* and *tr-plug-library* projects.
- `plugins/` – strategy and feature plugins such as *free-ride-investor*, *smart-stock-pro*, and *ultimate-options-trading-robot*.
- `analytics/` – advanced analytics modules including *ultimate-trading-intelligence*.
- `web-ui/` – user interface elements like *trading-robot-plug-web*.
- `lead-generation/` – auxiliary tooling such as *trading-leads-bot*.

Each subproject retains its original `CODE_ARCHITECTURE_STANDARDS.md` and `TASK_LIST.md` for reference. Future work will unify these documents and establish shared tooling, testing, and deployment workflows.

## Onboarding Resources

Structured passdown files for new contributors live in the `onboarding/` directory. These JSON, YAML, and XML documents outline each module and provide reconnaissance tasks to accelerate agent onboarding.
