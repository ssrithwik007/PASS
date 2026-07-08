from pathlib import Path
import pathspec

def load_ignore_spec(root: Path = Path(".")):
    ignore_file = root / ".secretignore"

    if not ignore_file.exists():
        return pathspec.PathSpec.from_lines("gitwildmatch", [])

    return pathspec.PathSpec.from_lines(
        "gitwildmatch",
        ignore_file.read_text().splitlines()
    )