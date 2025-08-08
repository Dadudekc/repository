"""Shared workspace utilities for project management."""

from pathlib import Path
from typing import List
import json


def get_project_directories(base_path: Path = Path('.')) -> List[Path]:
    """Return list of project directories using clone_summary.json."""
    config_path = base_path / 'clone_summary.json'
    if not config_path.exists():
        return []
    with config_path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    dirs: List[Path] = []
    for repo in data.get('repositories', []):
        name = repo.get('name')
        if not name:
            continue
        path = base_path / name
        if path.exists() and path.is_dir():
            dirs.append(path)
    return dirs


def detect_project_type(repo_path: Path) -> str:
    """Detect the type of project based on files present."""
    if not repo_path.exists():
        return "Unknown"

    files = list(repo_path.rglob("*"))
    file_names = [f.name.lower() for f in files if f.is_file()]

    if any(name in file_names for name in ['requirements.txt', 'setup.py', 'pyproject.toml', '__init__.py']):
        return "Python"
    if any(name in file_names for name in ['package.json', 'package-lock.json', 'yarn.lock']):
        return "Node.js"
    if any(name in file_names for name in ['composer.json', 'index.php', '.php']):
        return "PHP"
    if any(name in file_names for name in ['pom.xml', 'build.gradle', '.java']):
        return "Java"
    if any(name in file_names for name in ['index.html', 'index.htm', '.html', '.css', '.js']):
        return "Web"
    if any(name in file_names for name in ['.md', 'readme', 'docs']):
        return "Documentation"
    return "Unknown"
