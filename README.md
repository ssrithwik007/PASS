# PASS - Protect API Keys & Secrets Scanner

PASS (Protect API Keys & Secrets Scanner) is a lightweight security tool that scans local projects and Git repositories for accidentally exposed secrets such as API keys, passwords, access tokens, private keys, and other sensitive credentials.

Designed to integrate into a developer's workflow, PASS can scan an entire project or only the files staged for a Git commit, helping prevent secrets from being committed to source control.

---

## Features

* Scan an entire project recursively
* Scan only staged Git files before committing
* Detect a wide range of exposed secrets, including:

  * AWS Access Keys
  * OpenAI API Keys
  * GitHub Personal Access Tokens
  * GitLab Tokens
  * Google API Keys
  * Slack Tokens
  * Stripe Secret Keys
  * Twilio API Keys
  * SendGrid API Keys
  * Mailgun API Keys
  * Discord Bot Tokens
  * JWT Tokens
  * Database Connection URLs
  * Private Keys
  * Generic API Keys, Passwords, Secrets, and Access Tokens
* Supports customizable `.secretignore` files
* Colorized terminal output using Rich
* Categorizes findings by severity
* Masks detected secrets in reports
* Returns proper exit codes for automation and Git hooks

---

## Project Structure

```text
PASS/
│
├── pass.py
├── install_hook.py
├── requirements.txt
├── README.md
├── .secretignore
│
├── scanner/
│   ├── file_scanner.py
│   ├── git_detector.py
│   ├── report.py
│   ├── secret_detector.py
│   └── classes.py
│
├── rules/
│   └── patterns.py
│
├── utils/
│   └── ignore.py
│
└── demo/
    ├── vulnerable_project/
    └── clean_project/
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/ssrithwik007/PASS.git
```

```bash
cd PASS
```

---

## 2. Create a virtual environment (Recommended)

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Scan the current directory

```bash
python PASS/pass.py
```

### Scan a specific project

```bash
python PASS/pass.py <path-to-project>
```

Example:

```bash
python PASS/pass.py D:\Projects\MyBackend
```

or

```bash
python PASS/pass.py demo/vulnerable_project
```

### Scan staged Git files

```bash
python PASS/pass.py <path-to-git-repository> --staged
```

Example:

```bash
python PASS/pass.py D:\Projects\MyBackend --staged
```

This scans only the files currently staged in the specified Git repository.

# Using PASS as a Git Pre-Commit Hook

PASS is designed to be installed **once** and used to protect any number of Git repositories.

### Example Directory Structure

```text
D:\
│
├── Tools\
│   └── PASS\
│
├── Projects\
│   ├── Backend\
│   ├── Frontend\
│   └── Portfolio\
```

PASS can install a Git pre-commit hook into any repository without being copied into that repository.

## Step 1: Clone PASS

```bash
git clone https://github.com/ssrithwik007/PASS.git
cd PASS
```

## Step 2: Create a virtual environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Install the hook into your project

Run:

```bash
python install_hook.py <path-to-git-repository>
```

Example:

```bash
python install_hook.py D:\Projects\Backend
```

This installs a pre-commit hook into the specified Git repository.

## Step 5: Work normally

```bash
git add .
git commit -m "Add new feature"
```

Before Git creates the commit, PASS automatically scans all staged files.

* If no secrets are detected, the commit proceeds normally.
* If exposed credentials are found, PASS blocks the commit and displays a detailed report.

This helps prevent accidentally committing sensitive information such as API keys, passwords, tokens, private keys, and database credentials.

# Example Output

```text
────────────────────────────────────────────

PASS Security Scanner

Total Findings : 3

CRITICAL : 1
HIGH     : 2

────────────────────────────────────────────

OpenAI API Key

File   : config.py
Line   : 18
Secret : sk-abcd****************7890

────────────────────────────────────────────

GitHub Personal Access Token

File   : auth.py
Line   : 42
Secret : ghp_****************************x9F

────────────────────────────────────────────
```

---

# Exit Codes

PASS returns standard exit codes for automation.

| Exit Code | Meaning                      |
| --------- | ---------------------------- |
| 0         | No secrets detected          |
| 1         | One or more secrets detected |

This makes PASS suitable for Git hooks and CI/CD pipelines.

---

# Supported Secret Types

PASS currently detects many common credential formats, including:

* AWS Access Keys
* AWS Temporary Keys
* OpenAI API Keys
* GitHub Personal Access Tokens
* GitLab Tokens
* Google API Keys
* Slack Tokens
* Stripe Secret Keys
* Twilio API Keys
* SendGrid API Keys
* Mailgun API Keys
* Discord Bot Tokens
* JWT Tokens
* Database URLs
* Private Keys
* Generic API Keys
* Access Tokens
* Refresh Tokens
* Password Assignments
* Secret Variables

---

# Custom Ignore Rules

PASS supports a `.secretignore` file.

Example:

```text
.git
node_modules
dist
build
*.png
*.jpg
*.pdf
```

Files matching these patterns are skipped during scanning.

> **Note:** PASS scans `.env` files during manual project scans because they commonly contain sensitive credentials. During Git pre-commit scanning, `.env` files are only scanned if they have been staged for commit. This allows developers to safely keep local `.env` files for development while preventing accidental commits of sensitive information.


---

# Technologies Used

* Python
* Rich
* PathSpec
* Regular Expressions
* Git

---
