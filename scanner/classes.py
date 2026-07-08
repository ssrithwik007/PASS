from dataclasses import dataclass

@dataclass
class Finding:
    file: str
    line: int
    secret_type: str
    severity: str
    secret: str