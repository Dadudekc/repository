#!/usr/bin/env python3
"""
🚀 Unified Workspace Migration Tool

This script helps migrate your existing projects into the unified workspace structure.
It organizes projects by category and sets up the proper directory structure.
"""

import os
import shutil
import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProjectMigrator:
    """Handles migration of projects into unified workspace structure."""
    
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.project_categories = self._define_categories()
        
    def _define_categories(self) -> Dict[str, List[str]]:
        """Define project categories and their associated projects."""
        return {
            'trading': [
                'ultimate_trading_intelligence',
                'UltimateOptionsTradingRobot',
                'TradingRobotPlug',
                'TradingRobotPlugWeb',
                'SmartStock-pro',
                'FreeRideInvestor',
                'trading-leads-bot',
                'tbow-tactics',
                'LSTMmodel_trainer'
            ],
            'ai-ml': [
                'AI_Debugger_Assistant',
                'self-evolving-ai',
                'machinelearningproject',
                'machinelearningmodelmaker',
                'Hive-Mind',
                'gpt_automation',
                'HCshinobi'
            ],
            'web-apps': [
                'bolt-project',
                'FocusForge',
                'DreamVault',
                'FreeWork',
                'DaDudeKC-Website',
                'DaDudekC',
                'DigitalDreamscape',
                'socialmediamanager',
                'MeTuber'
            ],
            'tools': [
                'projectscanner',
                'network-scanner',
                'IT_help_desk',
                'basicbot',
                'osrsbot',
                'osrsAIagent'
            ],
            'personal': [
                'my-resume',
                'my-personal-templates',
                'Resume-Showcase',
                'content',
                'prompt-library',
                'Side-projects',
                'practice'
            ],
            'games': [
                'NewSims4ModProject',
                'TROOP'
            ]
        }
    
    def create_directory_structure(self):
        """Create the unified workspace directory structure."""
        logger.info("Creating unified workspace directory structure...")
        
        # Create main directories
        directories = [
            'projects',
            'shared/utils',
            'shared/configs',
            'shared/docs',
            'shared/scripts',
            'environment',
            'tools/linting',
            'tools/testing',
            'tools/deployment',
            'docs',
            'logs',
            'data'
        ]
        
        for directory in directories:
            dir_path = self.target_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {dir_path}")
    
    def categorize_project(self, project_name: str) -> str:
        """Determine the category for a given project."""
        for category, projects in self.project_categories.items():
            if project_name in projects:
                return category
        
        # Default categorization based on project name patterns
        if any(keyword in project_name.lower() for keyword in ['trading', 'stock', 'finance', 'robinhood', 'alpaca']):
            return 'trading'
        elif any(keyword in project_name.lower() for keyword in ['ai', 'ml', 'machine', 'neural', 'debugger']):
            return 'ai-ml'
        elif any(keyword in project_name.lower() for keyword in ['web', 'app', 'site', 'platform', 'forge', 'vault']):
            return 'web-apps'
        elif any(keyword in project_name.lower() for keyword in ['tool', 'scanner', 'utility', 'bot']):
            return 'tools'
        elif any(keyword in project_name.lower() for keyword in ['resume', 'personal', 'template', 'content']):
            return 'personal'
        else:
            return 'tools'  # Default category
    
    def migrate_project(self, project_name: str, source_path: Path, category: str):
        """Migrate a single project to the unified workspace."""
        target_path = self.target_dir / 'projects' / category / project_name
        
        try:
            if source_path.exists():
                # Copy project to new location
                if target_path.exists():
                    logger.warning(f"Target directory already exists: {target_path}")
                    return False
                
                shutil.copytree(source_path, target_path)
                logger.info(f"Migrated {project_name} to {target_path}")
                
                # Create project-specific README if it doesn't exist
                readme_path = target_path / 'README.md'
                if not readme_path.exists():
                    self._create_project_readme(target_path, project_name, category)
                
                return True
            else:
                logger.warning(f"Source project not found: {source_path}")
                return False
                
        except Exception as e:
            logger.error(f"Error migrating {project_name}: {e}")
            return False
    
    def _create_project_readme(self, project_path: Path, project_name: str, category: str):
        """Create a basic README for migrated projects."""
        readme_content = f"""# {project_name}

This project has been migrated to the unified workspace.

## Category: {category}

## Quick Start

```bash
# Navigate to project
cd projects/{category}/{project_name}

# Install dependencies (if needed)
pip install -r requirements.txt

# Run the project
python main.py  # or appropriate entry point
```

## Environment

This project uses the unified workspace environment. See the main workspace README for setup instructions.

## Development

- **Workspace Root**: {self.target_dir}
- **Project Path**: projects/{category}/{project_name}
- **Shared Utils**: Available via `from shared.utils import ...`

## Notes

- This project was automatically migrated to the unified workspace
- Update this README with project-specific information
- Consider moving common utilities to `shared/utils/`
"""
        
        readme_path = project_path / 'README.md'
        with open(readme_path, 'w') as f:
            f.write(readme_content)
    
    def migrate_all_projects(self):
        """Migrate all projects from source to target directory."""
        logger.info(f"Starting migration from {self.source_dir} to {self.target_dir}")
        
        # Create directory structure
        self.create_directory_structure()
        
        # Get all projects from source directory
        source_projects = []
        if self.source_dir.exists():
            source_projects = [item.name for item in self.source_dir.iterdir() 
                             if item.is_dir() and not item.name.startswith('.')]
        
        migration_stats = {
            'total': len(source_projects),
            'migrated': 0,
            'failed': 0,
            'by_category': {}
        }
        
        for project_name in source_projects:
            source_path = self.source_dir / project_name
            category = self.categorize_project(project_name)
            
            logger.info(f"Processing {project_name} -> {category}")
            
            if self.migrate_project(project_name, source_path, category):
                migration_stats['migrated'] += 1
                migration_stats['by_category'][category] = migration_stats['by_category'].get(category, 0) + 1
            else:
                migration_stats['failed'] += 1
        
        # Save migration report
        self._save_migration_report(migration_stats)
        
        logger.info("Migration completed!")
        self._print_migration_summary(migration_stats)
    
    def _save_migration_report(self, stats: Dict):
        """Save migration statistics to a JSON file."""
        report_path = self.target_dir / 'migration_report.json'
        with open(report_path, 'w') as f:
            json.dump(stats, f, indent=2)
        logger.info(f"Migration report saved to: {report_path}")
    
    def _print_migration_summary(self, stats: Dict):
        """Print a summary of the migration results."""
        print("\n" + "="*50)
        print("🚀 MIGRATION SUMMARY")
        print("="*50)
        print(f"Total projects found: {stats['total']}")
        print(f"Successfully migrated: {stats['migrated']}")
        print(f"Failed migrations: {stats['failed']}")
        print("\nProjects by category:")
        for category, count in stats['by_category'].items():
            print(f"  {category}: {count} projects")
        print("="*50)
    
    def create_workspace_setup_script(self):
        """Create a setup script for the unified workspace."""
        setup_script = f"""#!/usr/bin/env python3
\"\"\"
🚀 Unified Workspace Setup Script

This script sets up the unified development environment.
\"\"\"

import os
import subprocess
import sys
from pathlib import Path

def setup_workspace():
    \"\"\"Set up the unified workspace environment.\"\"\"
    workspace_root = Path(__file__).parent.parent
    
    print("🚀 Setting up Unified Workspace...")
    
    # Create virtual environment
    venv_path = workspace_root / 'venv'
    if not venv_path.exists():
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', str(venv_path)])
    
    # Install dependencies
    requirements_path = workspace_root / 'environment' / 'requirements.txt'
    if requirements_path.exists():
        print("Installing dependencies...")
        pip_cmd = str(venv_path / 'Scripts' / 'pip.exe') if os.name == 'nt' else str(venv_path / 'bin' / 'pip')
        subprocess.run([pip_cmd, 'install', '-r', str(requirements_path)])
    
    # Copy environment template
    env_template = workspace_root / 'environment' / 'env.example'
    env_file = workspace_root / '.env'
    if env_template.exists() and not env_file.exists():
        print("Creating .env file from template...")
        shutil.copy2(env_template, env_file)
        print("⚠️  Please edit .env file with your API keys and settings")
    
    print("✅ Workspace setup complete!")
    print(f"📁 Workspace location: {workspace_root}")
    print("🔧 Next steps:")
    print("  1. Edit .env file with your API keys")
    print("  2. Activate virtual environment")
    print("  3. Start developing!")

if __name__ == '__main__':
    setup_workspace()
"""
        
        setup_path = self.target_dir / 'setup_workspace.py'
        with open(setup_path, 'w') as f:
            f.write(setup_script)
        
        # Make executable
        os.chmod(setup_path, 0o755)
        logger.info(f"Created workspace setup script: {setup_path}")

def main():
    """Main migration function."""
    parser = argparse.ArgumentParser(description='Migrate projects to unified workspace')
    parser.add_argument('--source', default='../Dadudekc', 
                       help='Source directory containing projects')
    parser.add_argument('--target', default='./unified-workspace',
                       help='Target directory for unified workspace')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be migrated without actually doing it')
    
    args = parser.parse_args()
    
    migrator = ProjectMigrator(args.source, args.target)
    
    if args.dry_run:
        logger.info("DRY RUN MODE - No files will be moved")
        # Show what would be migrated
        source_dir = Path(args.source)
        if source_dir.exists():
            projects = [item.name for item in source_dir.iterdir() 
                       if item.is_dir() and not item.name.startswith('.')]
            print("Projects that would be migrated:")
            for project in projects:
                category = migrator.categorize_project(project)
                print(f"  {project} -> projects/{category}/")
    else:
        migrator.migrate_all_projects()
        migrator.create_workspace_setup_script()

if __name__ == '__main__':
    main()
