#!/usr/bin/env python3
"""
🚀 Unified Workspace Setup Script

Quick setup for your unified development environment.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_banner():
    """Print the setup banner."""
    print("="*60)
    print("🚀 UNIFIED WORKSPACE SETUP")
    print("="*60)
    print("One Environment. All Your Projects. Zero Setup Fights.")
    print("="*60)

def check_prerequisites():
    """Check if required software is installed."""
    print("🔍 Checking prerequisites...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Check pip
    try:
        import pip
        print("✅ pip is available")
    except ImportError:
        print("❌ pip is not available")
        return False
    
    # Check git
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git is available")
        else:
            print("⚠️  Git not found (optional but recommended)")
    except FileNotFoundError:
        print("⚠️  Git not found (optional but recommended)")
    
    return True

def create_virtual_environment():
    """Create a Python virtual environment."""
    print("\n🐍 Creating virtual environment...")
    
    workspace_root = Path(__file__).parent
    venv_path = workspace_root / 'venv'
    
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    try:
        subprocess.run([sys.executable, '-m', 'venv', str(venv_path)], check=True)
        print("✅ Virtual environment created")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def install_dependencies():
    """Install Python dependencies."""
    print("\n📦 Installing dependencies...")
    
    workspace_root = Path(__file__).parent
    requirements_path = workspace_root / 'environment' / 'requirements.txt'
    venv_path = workspace_root / 'venv'
    
    if not requirements_path.exists():
        print("❌ requirements.txt not found")
        return False
    
    # Determine pip command based on OS
    if os.name == 'nt':  # Windows
        pip_cmd = str(venv_path / 'Scripts' / 'pip.exe')
    else:  # Unix/Linux/Mac
        pip_cmd = str(venv_path / 'bin' / 'pip')
    
    try:
        # Upgrade pip first
        subprocess.run([pip_cmd, 'install', '--upgrade', 'pip'], check=True)
        
        # Install requirements
        subprocess.run([pip_cmd, 'install', '-r', str(requirements_path)], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def setup_environment_file():
    """Set up the environment configuration file."""
    print("\n⚙️  Setting up environment configuration...")
    
    workspace_root = Path(__file__).parent
    env_template = workspace_root / 'environment' / 'env.example'
    env_file = workspace_root / '.env'
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if env_template.exists():
        shutil.copy2(env_template, env_file)
        print("✅ Created .env file from template")
        print("⚠️  IMPORTANT: Edit .env file with your API keys and settings")
        return True
    else:
        print("❌ Environment template not found")
        return False

def create_shared_utilities():
    """Create basic shared utility modules."""
    print("\n🛠️  Creating shared utilities...")
    
    workspace_root = Path(__file__).parent
    shared_utils = workspace_root / 'shared' / 'utils'
    shared_utils.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py
    init_file = shared_utils / '__init__.py'
    if not init_file.exists():
        init_file.write_text('"""Shared utilities for the unified workspace."""\n')
    
    # Create basic utility modules
    utilities = {
        'config.py': '''"""Configuration utilities for the unified workspace."""
import os
from pathlib import Path
from typing import Dict, Any

def get_workspace_root() -> Path:
    """Get the workspace root directory."""
    return Path(__file__).parent.parent.parent

def load_env_vars() -> Dict[str, str]:
    """Load environment variables from .env file."""
    env_file = get_workspace_root() / '.env'
    env_vars = {}
    
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key] = value
    
    return env_vars

def get_setting(key: str, default: Any = None) -> Any:
    """Get a setting from environment variables."""
    env_vars = load_env_vars()
    return env_vars.get(key, default)
''',
        'logger.py': '''"""Logging utilities for the unified workspace."""
import logging
import sys
from pathlib import Path
from typing import Optional

def setup_logger(name: str, level: str = 'INFO', log_file: Optional[str] = None) -> logging.Logger:
    """Set up a logger for the workspace."""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
''',
        'api_client.py': '''"""API client utilities for the unified workspace."""
import requests
import aiohttp
import asyncio
from typing import Dict, Any, Optional
from .config import get_setting

class APIClient:
    """Base API client for the workspace."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key or get_setting('API_KEY')
        self.session = requests.Session()
        
        if self.api_key:
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a GET request."""
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, **kwargs)
    
    def post(self, endpoint: str, data: Dict[str, Any], **kwargs) -> requests.Response:
        """Make a POST request."""
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=data, **kwargs)

class AsyncAPIClient:
    """Async API client for the workspace."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key or get_setting('API_KEY')
        self.headers = {}
        
        if self.api_key:
            self.headers['Authorization'] = f'Bearer {self.api_key}'
    
    async def get(self, endpoint: str, **kwargs) -> aiohttp.ClientResponse:
        """Make an async GET request."""
        url = f"{self.base_url}{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers, **kwargs) as response:
                return response
    
    async def post(self, endpoint: str, data: Dict[str, Any], **kwargs) -> aiohttp.ClientResponse:
        """Make an async POST request."""
        url = f"{self.base_url}{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=self.headers, **kwargs) as response:
                return response
'''
    }
    
    for filename, content in utilities.items():
        file_path = shared_utils / filename
        if not file_path.exists():
            file_path.write_text(content)
            print(f"✅ Created {filename}")
    
    return True

def print_next_steps():
    """Print next steps for the user."""
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    print("\n📋 Next Steps:")
    print("1. Edit .env file with your API keys and settings")
    print("2. Activate the virtual environment:")
    print("   Windows: venv\\Scripts\\activate")
    print("   Mac/Linux: source venv/bin/activate")
    print("3. Start developing!")
    print("\n🚀 Quick Start Commands:")
    print("   cd unified-workspace")
    print("   # Activate environment")
    print("   python -c 'from shared.utils.config import get_workspace_root; print(get_workspace_root())'")
    print("\n📁 Your projects will be organized in:")
    print("   projects/trading/     - Trading and financial projects")
    print("   projects/ai-ml/       - AI and machine learning projects")
    print("   projects/web-apps/    - Web applications")
    print("   projects/tools/       - Utility and tool projects")
    print("   projects/personal/    - Personal projects")
    print("\n🔧 To migrate your existing projects:")
    print("   python tools/migrate_projects.py --dry-run")
    print("   python tools/migrate_projects.py")
    print("="*60)

def main():
    """Main setup function."""
    print_banner()
    
    if not check_prerequisites():
        print("❌ Prerequisites not met. Please install required software.")
        return False
    
    if not create_virtual_environment():
        print("❌ Failed to create virtual environment.")
        return False
    
    if not install_dependencies():
        print("❌ Failed to install dependencies.")
        return False
    
    if not setup_environment_file():
        print("❌ Failed to set up environment file.")
        return False
    
    if not create_shared_utilities():
        print("❌ Failed to create shared utilities.")
        return False
    
    print_next_steps()
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
