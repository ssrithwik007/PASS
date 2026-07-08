import re

RULES = [
    # ==========================
    # Cloud Providers
    # ==========================
    {
        "name": "AWS Access Key",
        "severity": "CRITICAL",
        "pattern": re.compile(r"AKIA[0-9A-Z]{16}")
    },
    {
        "name": "AWS Temporary Access Key",
        "severity": "CRITICAL",
        "pattern": re.compile(r"ASIA[0-9A-Z]{16}")
    },
    {
        "name": "Google API Key",
        "severity": "HIGH",
        "pattern": re.compile(r"AIza[0-9A-Za-z\-_]{35}")
    },

    # ==========================
    # OpenAI
    # ==========================
    {
        "name": "OpenAI API Key",
        "severity": "CRITICAL",
        "pattern": re.compile(r"sk-[A-Za-z0-9_-]{20,}")
    },

    # ==========================
    # GitHub
    # ==========================
    {
        "name": "GitHub Personal Access Token",
        "severity": "CRITICAL",
        "pattern": re.compile(r"gh[pousr]_[A-Za-z0-9]{36,255}")
    },

    # ==========================
    # GitLab
    # ==========================
    {
        "name": "GitLab Token",
        "severity": "HIGH",
        "pattern": re.compile(r"glpat-[A-Za-z0-9\-_]{20,}")
    },

    # ==========================
    # Slack
    # ==========================
    {
        "name": "Slack Token",
        "severity": "HIGH",
        "pattern": re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")
    },

    # ==========================
    # Stripe
    # ==========================
    {
        "name": "Stripe Secret Key",
        "severity": "CRITICAL",
        "pattern": re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}")
    },

    # ==========================
    # Twilio
    # ==========================
    {
        "name": "Twilio API Key",
        "severity": "HIGH",
        "pattern": re.compile(r"SK[a-fA-F0-9]{32}")
    },

    # ==========================
    # SendGrid
    # ==========================
    {
        "name": "SendGrid API Key",
        "severity": "HIGH",
        "pattern": re.compile(r"SG\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}")
    },

    # ==========================
    # Mailgun
    # ==========================
    {
        "name": "Mailgun API Key",
        "severity": "HIGH",
        "pattern": re.compile(r"key-[A-Fa-f0-9]{32}")
    },

    # ==========================
    # Discord
    # ==========================
    {
        "name": "Discord Bot Token",
        "severity": "HIGH",
        "pattern": re.compile(r"[MN][A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27}")
    },

    # ==========================
    # JWT
    # ==========================
    {
        "name": "JWT Token",
        "severity": "MEDIUM",
        "pattern": re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")
    },

    # ==========================
    # Private Keys
    # ==========================
    {
        "name": "Private Key",
        "severity": "CRITICAL",
        "pattern": re.compile(
            r"-----BEGIN (RSA|DSA|EC|OPENSSH|PGP|PRIVATE) KEY-----"
        )
    },

    # ==========================
    # Generic Bearer Token
    # ==========================
    {
        "name": "Bearer Token",
        "severity": "HIGH",
        "pattern": re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{20,}")
    },

    # ==========================
    # Generic API Key Assignment
    # ==========================
    {
        "name": "API Key",
        "severity": "MEDIUM",
        "pattern": re.compile(
            r"(?i)(api[_-]?key)\s*[:=]\s*['\"][A-Za-z0-9_\-./+=]{8,}['\"]"
        )
    },

    {
        "name": "Secret",
        "severity": "MEDIUM",
        "pattern": re.compile(
            r"(?i)(secret|secret_key|client_secret)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
        )
    },

    {
        "name": "Access Token",
        "severity": "MEDIUM",
        "pattern": re.compile(
            r"(?i)(access[_-]?token)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
        )
    },

    {
        "name": "Refresh Token",
        "severity": "MEDIUM",
        "pattern": re.compile(
            r"(?i)(refresh[_-]?token)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
        )
    },

    {
        "name": "Password",
        "severity": "LOW",
        "pattern": re.compile(
            r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"][^'\"]{6,}['\"]"
        )
    },

    {
        "name": "Database URL",
        "severity": "HIGH",
        "pattern": re.compile(
            r"(postgres|postgresql|mysql|mongodb|redis):\/\/[^\s'\"]+"
        )
    }
]