import subprocess
from pathlib import Path
from .classes import Finding
from .file_scanner import scan_files

def get_staged_files(repo_path: Path) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_path), "diff", "--cached", "--name-only"],
            capture_output=True,
            text=True,
            check=True
        )
        
        files = [
            Path(repo_path / line)
            for line in result.stdout.splitlines()
            if line.strip()
        ]

        return [f for f in files if f.exists()]
    
    except subprocess.CalledProcessError as e:
        print("Current directory is not a Git repository.")
        return []
    except OSError:
        print("Git is either not installed or not added to your system's PATH.")
        return []

def scan_staged_files(repo_path: Path) -> list[Finding]:
    return scan_files(get_staged_files(repo_path))