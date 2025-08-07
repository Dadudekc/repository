#!/usr/bin/env python3
"""Generate CODE_ARCHITECTURE_STANDARDS.md for all repositories.

This script walks through all top-level directories in the workspace and
creates a CODE_ARCHITECTURE_STANDARDS.md file with common guidelines for
project structure, code quality, testing, security, and documentation.
"""

from datetime import datetime
from pathlib import Path

CONTENT_TEMPLATE = """# Coding & Architecture Standards

## Project Structure
- Use modular design with clear separation of concerns.
- Keep configuration, source, tests, and documentation in dedicated folders.
- Minimize duplication through reusable components and libraries.
- Prefer class-based, object-oriented design for complex components.

## Code Quality
- Follow language-specific style guides (PEP 8 for Python, etc.).
- Enforce linters and formatters in the development workflow.
- Keep functions small and focused.
- Design classes and modules to follow the Single Responsibility Principle (SRP).

## Testing
- Maintain unit tests for critical functionality.
- Include integration tests for major workflows.
- Provide example data or fixtures to simplify test setup.

## Security
- Validate all external input and sanitize outputs.
- Store secrets outside the codebase and load them securely at runtime.
- Regularly review dependencies for vulnerabilities.

## Documentation
- Document public functions, modules, and complex logic.
- Keep README and usage examples up to date.
- Include setup instructions and contribution guidelines.

---
**Last Updated**: {date}
"""


def main() -> None:
    base_path = Path('.')
    repositories = [d for d in base_path.iterdir()
                    if d.is_dir() and not d.name.startswith('.') and d.name != '.git']

    date = datetime.now().strftime('%Y-%m-%d')
    for repo in repositories:
        path = repo / 'CODE_ARCHITECTURE_STANDARDS.md'
        path.write_text(CONTENT_TEMPLATE.format(date=date), encoding='utf-8')
        print(f"Created CODE_ARCHITECTURE_STANDARDS.md for {repo.name}")


if __name__ == '__main__':
    main()
