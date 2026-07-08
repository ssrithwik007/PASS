import argparse
from pathlib import Path

from scanner.file_scanner import scan_directory
from scanner.git_detector import scan_staged_files
from scanner.report import print_report


def main():
    parser = argparse.ArgumentParser(
        description="PASS: Protect API Keys & Secrets Scanner"
    )

    parser.add_argument(
        "target",
        type=str,
        nargs="?",
        default=".",
        help="The target directory to scan (defaults to current directory '.')"
    )

    parser.add_argument(
        "--staged",
        action="store_true",
        help="Scan only staged Git files."
    )

    args = parser.parse_args()

    target_path = Path(args.target).resolve()

    if not target_path.exists():
        parser.error(f"'{target_path}' does not exist.")

    if not target_path.is_dir():
        parser.error(f"'{target_path}' is not a directory.")

    if args.staged:
        findings = scan_staged_files(target_path)
    else:

        findings = scan_directory(target_path)

    print_report(findings)

    raise SystemExit(1 if findings else 0)


if __name__ == "__main__":
    main()