# Trading Platform Coding & Architecture Standards

## General Guidelines
- Write modular components; each module (core engine, plugins, analytics, web UI, lead generation) should be self-contained.
- Use clear, descriptive naming following `snake_case` for files and functions.
- Document public interfaces and complex logic using in-line comments and README files.
- Prefer dependency injection for extensibility and testing.
- Enforce code linting and formatting prior to commits.

## Core Engine
- Expose a stable API for strategy execution and data access.
- Handle configuration via environment variables or config files.

## Plugins
- Plugins must implement the prescribed interface defined by the core engine.
- Keep plugin dependencies isolated to avoid bloating the core system.

## Analytics
- Separate data collection, processing, and visualization layers.
- Provide reproducible analysis scripts and maintain versioned datasets where possible.

## Web UI
- Build lightweight front-ends that interact with the core engine through API endpoints.
- Ensure accessibility and responsive design across devices.

## Lead Generation
- Comply with applicable privacy laws and clearly document data sources.
- Abstract lead collection mechanisms to allow future integrations.
