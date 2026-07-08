from pathlib import Path
from rules.patterns import RULES
from .classes import Finding

def scan_file(path: Path) -> list[Finding]:
    findings = []

    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, start=1):
            for rule in RULES:
                for match in rule["pattern"].finditer(line):
                    findings.append(
                        Finding(
                        file=str(path),
                        line=line_num,
                        secret_type=rule["name"],
                        severity=rule["severity"],
                        secret=match.group(0),
                    ))

    return findings

