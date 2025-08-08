import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tools.migrate_projects import ProjectMigrator


def test_project_migrator_class():
    assert hasattr(ProjectMigrator, '__init__')

