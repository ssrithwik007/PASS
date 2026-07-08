from pathlib import Path
from .secret_detector import scan_file
from .classes import Finding
from utils.ignore import load_ignore_spec

TEXT_EXTENSIONS = { ".py", ".js", ".ts", ".jsx", ".tsx", ".env", ".json", ".yaml", ".yml", ".toml", ".ini", ".txt", }

IGNORED_DIRS = { ".git", "node_modules", "__pycache__", "venv", ".venv", "dist", "build", }

def is_binary(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            return b"\0" in f.read(1024)
    except OSError:
        return True
    
def scan_files(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []

    spec = load_ignore_spec(Path("."))

    for file in files:
        if not file.is_file():
            continue

        if spec.match_file(file.as_posix()):
            continue

        if file.suffix not in TEXT_EXTENSIONS and not file.name.startswith(".env"):
            continue

        if is_binary(file):
            continue

        try:
            findings.extend(scan_file(file))
        except (PermissionError, FileNotFoundError):
            continue

    return findings

def scan_directory(dir_path: Path) -> list[Finding]:
    files = [f for f in dir_path.rglob("*") if f.is_file()]
    return scan_files(files)