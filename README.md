# Milton-BDD-Playwright-Python

Python + pytest + BDD + Playwright sample project.

## Setup

```powershell
cd "c:\Users\MILTON SARKAR\git\Milton-BDD-Playwright-Python"
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
```

## Run tests locally

```powershell
python -m pytest
```

## Run a tagged scenario

```powershell
python -m pytest -m smoke
```

## GitHub Actions

This project includes a GitHub Actions workflow at `.github/workflows/python-playwright.yml`.
The workflow installs dependencies, installs Playwright browsers, and runs `pytest -q` on `ubuntu-latest`.

## Branch and PR workflow

- Develop on the `Milton-Release-BDD` branch.
- Push your local changes to `Milton-Release-BDD` to trigger CI.
- Open a pull request from `Milton-Release-BDD` into `main`.
- The workflow will run for pushes to `Milton-Release-BDD` and PRs targeting `main` from that branch.

## Notes

- Keep `.venv/` out of source control. It is ignored by `.gitignore`.
- If you need a fresh environment, recreate it with `python -m venv .venv`.

## VS Code & PYTHONPATH

- This project adds a `.env` file at the workspace root with `PYTHONPATH=${workspaceFolder}` to help Pylance locate local packages.
- VS Code settings (`.vscode/settings.json`) point `python.envFile` to this file; ensure you select the project's virtual environment (Command Palette → `Python: Select Interpreter`) and reload the window if import diagnostics persist.
