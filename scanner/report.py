from collections import Counter
from rich.console import Console
from rich.panel import Panel
from .classes import Finding

console = Console()

SEVERITY_COLORS = {
    "CRITICAL": "bold red",
    "HIGH": "red",
    "MEDIUM": "yellow",
    "LOW": "cyan",
}

def mask_secret(secret: str) -> str:
    if len(secret) <= 8:
        return "*" * len(secret)

    return f"{secret[:4]}{'*' * (len(secret) - 8)}{secret[-4:]}"

def print_summary(findings: list[Finding]) -> None:
    if not findings:
        console.print("\n[bold green]✓ No secrets detected![/bold green]\n")
        return

    counts = Counter(f.severity for f in findings)

    console.rule("[bold blue]PASS Security Scanner[/bold blue]")

    console.print(f"[bold]Total Findings:[/bold] {len(findings)}")

    for severity in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
        if severity in counts:
            color = SEVERITY_COLORS[severity]
            console.print(f"[{color}]{severity:<8}[/{color}] : {counts[severity]}")

    console.rule()

def print_report(findings: list[Finding]) -> None:
    print_summary(findings)

    if not findings:
        return

    severity_order = {
        "CRITICAL": 0,
        "HIGH": 1,
        "MEDIUM": 2,
        "LOW": 3,
    }

    findings.sort(key=lambda f: severity_order.get(f.severity, 99))

    for finding in findings:
        color = SEVERITY_COLORS.get(finding.severity, "white")

        body = (
            f"[bold]{finding.secret_type}[/bold]\n\n"
            f"[cyan]File:[/cyan] {finding.file}\n"
            f"[cyan]Line:[/cyan] {finding.line}\n"
            f"[cyan]Secret:[/cyan] {mask_secret(finding.secret)}"
        )

        console.print(
            Panel(
                body,
                title=f"[{color}]{finding.severity}[/{color}]",
                border_style=color,
                expand=False,
            )
        )