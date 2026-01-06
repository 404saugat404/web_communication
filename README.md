# web_communication
this repo contains code that can be used to learn how communication works in web


# Project Setup & Run Instructions

This project uses **uv** to manage the Python virtual environment and run the application.

---

## Prerequisites

- Python 3.9 or newer
- `uv` installed

Check that `uv` is installed:
```bash
uv --version


Setup Steps
Step 1: Clone the repository
git clone <your-repo-url>
cd <your-repo-name>

Step 2: Create the virtual environment
uv venv


This creates a .venv/ directory in the project root.

Step 3: Activate the virtual environment
Windows (Command Prompt)
.venv\Scripts\activate.bat

Windows (PowerShell)
.venv\Scripts\Activate.ps1

macOS / Linux
source .venv/bin/activate


After activation, your terminal prompt should show:

(.venv)

Step 4: Run the application
uv run python -m app.main