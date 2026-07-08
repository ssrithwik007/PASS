from pathlib import Path
import argparse
import sys

parser = argparse.ArgumentParser(
    description="Install the PASS Git pre-commit hook."
)

parser.add_argument(
    "repository",
    help="Path to the Git repository to protect."
)

args = parser.parse_args()

repo = Path(args.repository).resolve()

git_dir = repo / ".git"

if not git_dir.exists():
    print(f"'{repo}' is not a Git repository.")
    raise SystemExit(1)

# Location of PASS
pass_root = Path(__file__).resolve().parent
pass_script = (Path(__file__).parent / "pass.py").resolve()

if not pass_script.exists():
    print("Unable to locate pass.py.")
    raise SystemExit(1)

hook_dst = git_dir / "hooks" / "pre-commit"

python_executable = Path(sys.executable).resolve()

hook_contents = f"""#!/bin/sh

echo
echo "=================================="
echo " Running PASS Secret Scanner"
echo "=================================="
echo

"{python_executable.as_posix()}" "{pass_script.as_posix()}" "{repo.as_posix()}" --staged

status=$?

if [ $status -ne 0 ]; then
    echo
    echo "❌ Commit blocked!"
    echo "Remove exposed secrets before committing."
    exit 1
fi

echo
echo "✅ PASS completed successfully."

exit 0
"""

hook_dst.write_text(hook_contents, encoding="utf-8", newline="\n")

print()
print("PASS pre-commit hook installed successfully!")
print(f"Repository : {repo}")
print(f"Hook       : {hook_dst}")
print()
print("PASS will now scan staged files before every commit.")