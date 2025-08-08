#!/usr/bin/env python3
"""Bootstrap the development environment for GPT Automation."""
import os
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> None:
    env_dir = Path(__file__).resolve().parent
    project_root = env_dir.parent
    venv_dir = env_dir / "venv"

    if not venv_dir.exists():
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
    pip = venv_dir / ("Scripts" if os.name == "nt" else "bin") / "pip"
    subprocess.run([str(pip), "install", "-r", str(env_dir / "requirements.txt")], check=True)

    env_file = project_root / ".env"
    if not env_file.exists():
        shutil.copy(env_dir / "env.example", env_file)
        print("Created .env from env.example")

    print("Environment setup complete. Activate with `source environment/venv/bin/activate`.")


if __name__ == "__main__":  # pragma: no cover - script entry point
    main()
