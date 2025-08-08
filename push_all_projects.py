#!/usr/bin/env python3
"""
Push All Projects Script

This script helps manage and push all individual projects to their respective repositories.
It provides functionality to:
1. Initialize git repositories for each project
2. Set up remote repositories
3. Push projects to their respective repositories
4. Manage project dependencies and setup
"""

import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

from workspace_utils import get_project_directories, detect_project_type

class ProjectManager:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.projects = []
        self.config_file = "project_config.json"
        
    def scan_projects(self):
        """Scan for all project directories"""
        projects = []
        for item in get_project_directories(self.base_path):
            name = item.name
            if any(skip in name.lower() for skip in ['backup', 'node_modules', 'venv', 'env']):
                continue
            projects.append({
                'name': name,
                'path': item,
                'type': detect_project_type(item),
                'has_git': (item / '.git').exists(),
                'has_task_list': (item / 'TASK_LIST.md').exists()
            })
        self.projects = projects
        return projects
    
    def create_project_config(self):
        """Create configuration for all projects"""
        config = {
            'last_updated': datetime.now().isoformat(),
            'total_projects': len(self.projects),
            'projects': {}
        }
        
        for project in self.projects:
            config['projects'][project['name']] = {
                'type': project['type'],
                'has_git': project['has_git'],
                'has_task_list': project['has_task_list'],
                'remote_url': None,
                'status': 'pending'
            }
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Created project configuration: {self.config_file}")
        return config
    
    def initialize_git_repository(self, project_path, project_name):
        """Initialize git repository for a project"""
        try:
            # Change to project directory
            os.chdir(project_path)
            
            # Initialize git if not already done
            if not (project_path / '.git').exists():
                subprocess.run(['git', 'init'], check=True)
                print(f"✅ Initialized git repository for {project_name}")
            
            # Add all files (force if needed)
            try:
                subprocess.run(['git', 'add', '.'], check=True)
            except subprocess.CalledProcessError:
                # Try with force flag if files are ignored
                subprocess.run(['git', 'add', '-f', '.'], check=True)
            
            # Check if there are changes to commit
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, check=True)
            
            if result.stdout.strip():
                # Commit changes
                subprocess.run(['git', 'commit', '-m', f'Initial commit for {project_name}'], check=True)
                print(f"✅ Committed changes for {project_name}")
            else:
                print(f"ℹ️  No changes to commit for {project_name}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error initializing git for {project_name}: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error for {project_name}: {e}")
            return False
    
    def setup_remote_repository(self, project_path, project_name):
        """Set up remote repository for a project"""
        try:
            os.chdir(project_path)
            
            # Check if remote already exists
            result = subprocess.run(['git', 'remote', '-v'], 
                                  capture_output=True, text=True, check=True)
            
            if not result.stdout.strip():
                # Create remote URL (you can customize this)
                remote_url = f"https://github.com/Dadudekc/{project_name}.git"
                
                # Add remote
                subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)
                print(f"✅ Added remote origin for {project_name}: {remote_url}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error setting up remote for {project_name}: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error for {project_name}: {e}")
            return False
    
    def push_project(self, project_path, project_name):
        """Push project to remote repository"""
        try:
            os.chdir(project_path)
            
            # Push to remote
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
            print(f"✅ Successfully pushed {project_name} to remote repository")
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error pushing {project_name}: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error pushing {project_name}: {e}")
            return False
    
    def create_setup_script(self, project_path, project_name, project_type):
        """Create setup script for the project"""
        setup_script = project_path / "setup.py"
        
        # Ensure project directory exists
        project_path.mkdir(exist_ok=True)
        
        if project_type == "Python":
            content = f'''#!/usr/bin/env python3
"""
Setup script for {project_name}
"""

import os
import subprocess
import sys
from pathlib import Path

def install_dependencies():
    """Install Python dependencies"""
    requirements_file = Path("requirements.txt")
    if requirements_file.exists():
        print("📦 Installing Python dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
    else:
        print("ℹ️  No requirements.txt found")

def setup_environment():
    """Set up environment variables"""
    env_file = Path(".env.example")
    if env_file.exists():
        print("🔧 Setting up environment variables...")
        if not Path(".env").exists():
            with open(".env", "w") as f:
                f.write("# Copy from .env.example and configure\n")
            print("✅ Created .env file from .env.example")
    else:
        print("ℹ️  No .env.example found")

def main():
    """Main setup function"""
    print(f"🚀 Setting up {project_name}...")
    
    # Install dependencies
    install_dependencies()
    
    # Setup environment
    setup_environment()
    
    print(f"✅ {project_name} setup complete!")
    print("📖 Check TASK_LIST.md for next steps")

if __name__ == "__main__":
    main()
'''
        elif project_type == "Node.js":
            content = f'''#!/usr/bin/env node
/**
 * Setup script for {project_name}
 */

const fs = require('fs');
const path = require('path');
const {{ execSync }} = require('child_process');

function installDependencies() {{
    console.log('📦 Installing Node.js dependencies...');
    try {{
        execSync('npm install', {{ stdio: 'inherit' }});
        console.log('✅ Dependencies installed successfully');
    }} catch (error) {{
        console.log('❌ Error installing dependencies:', error.message);
    }}
}}

function setupEnvironment() {{
    console.log('🔧 Setting up environment variables...');
    const envExample = path.join(__dirname, '.env.example');
    const envFile = path.join(__dirname, '.env');
    
    if (fs.existsSync(envExample) && !fs.existsSync(envFile)) {{
        fs.copyFileSync(envExample, envFile);
        console.log('✅ Created .env file from .env.example');
    }} else {{
        console.log('ℹ️  No .env.example found or .env already exists');
    }}
}}

function main() {{
    console.log(`🚀 Setting up ${{project_name}}...`);
    
    // Install dependencies
    installDependencies();
    
    // Setup environment
    setupEnvironment();
    
    console.log(`✅ ${{project_name}} setup complete!`);
    console.log('📖 Check TASK_LIST.md for next steps');
}}

main();
'''
        else:
            content = f'''#!/bin/bash
# Setup script for {project_name}

echo "🚀 Setting up {project_name}..."

# Check if setup script exists
if [ -f "setup.sh" ]; then
    echo "📦 Running custom setup script..."
    chmod +x setup.sh
    ./setup.sh
else
    echo "ℹ️  No custom setup script found"
fi

echo "✅ {project_name} setup complete!"
echo "📖 Check TASK_LIST.md for next steps"
'''

        with open(setup_script, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Make executable
        os.chmod(setup_script, 0o755)
        print(f"✅ Created setup script for {project_name}")
    
    def create_readme(self, project_path, project_name, project_type):
        """Create README.md for the project"""
        readme_file = project_path / "README.md"
        
        # Ensure project directory exists
        project_path.mkdir(exist_ok=True)
        
        if not readme_file.exists():
            content = f"""# {project_name.replace('-', ' ').title()}

## 🚀 Quick Start

### Prerequisites
- {self.get_prerequisites(project_type)}

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dadudekc/{project_name}.git
   cd {project_name}
   ```

2. **Run setup script**
   ```bash
   {self.get_setup_command(project_type)}
   ```

3. **Follow the task list**
   - Check `TASK_LIST.md` for detailed development tasks
   - Complete environment setup
   - Implement core features
   - Run tests

## 📋 Development

### Project Structure
```
{project_name}/
├── README.md          # This file
├── TASK_LIST.md       # Development tasks and goals
├── setup.py           # Setup script
└── ...                # Project files
```

### Development Workflow
1. Check `TASK_LIST.md` for current tasks
2. Set up development environment
3. Implement features
4. Run tests
5. Update documentation

## 🎯 Goals

This project is part of the Dadudekc repository collection. See `TASK_LIST.md` for:
- Beta readiness checklist
- Environment setup requirements
- Development standards
- Deployment guidelines

## 📞 Support

- Check `TASK_LIST.md` for detailed guidance
- Create issues for bugs or feature requests
- Follow the development standards outlined in the task list

---
**Last Updated**: {datetime.now().strftime("%Y-%m-%d")}
"""
            
            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Created README.md for {project_name}")
    
    def get_prerequisites(self, project_type):
        """Get prerequisites for project type"""
        if project_type == "Python":
            return "Python 3.8+, pip"
        elif project_type == "Node.js":
            return "Node.js 16+, npm"
        elif project_type == "PHP":
            return "PHP 8.0+, Composer"
        elif project_type == "Java":
            return "Java 11+, Maven/Gradle"
        else:
            return "See project documentation"
    
    def get_setup_command(self, project_type):
        """Get setup command for project type"""
        if project_type == "Python":
            return "python setup.py"
        elif project_type == "Node.js":
            return "node setup.js"
        else:
            return "./setup.sh"
    
    def process_all_projects(self):
        """Process all projects"""
        print("🔍 Scanning projects...")
        self.scan_projects()
        
        print(f"📊 Found {len(self.projects)} projects")
        
        # Create configuration
        self.create_project_config()
        
        # Process each project
        for project in self.projects:
            print(f"\n🔄 Processing {project['name']} ({project['type']})...")
            
            # Create setup script
            self.create_setup_script(project['path'], project['name'], project['type'])
            
            # Create README
            self.create_readme(project['path'], project['name'], project['type'])
            
            # Initialize git repository
            if not project['has_git']:
                self.initialize_git_repository(project['path'], project['name'])
            
            # Setup remote repository
            self.setup_remote_repository(project['path'], project['name'])
            
            # Push to remote (optional - uncomment if you want to push all)
            # self.push_project(project['path'], project['name'])
        
        print(f"\n🎉 Project processing complete!")
        print(f"📋 Processed {len(self.projects)} projects")
        print(f"📊 Configuration saved to {self.config_file}")
        print(f"🚀 Each project is now ready for individual development and deployment")

def main():
    """Main function"""
    manager = ProjectManager()
    manager.process_all_projects()

if __name__ == "__main__":
    main()
