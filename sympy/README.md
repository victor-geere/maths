# Maths Framework

This repository contains exploratory mathematical work on spectral analysis, including quaternion-cosine energy functionals, dyadic decompositions, and sheaf-theoretic interpretations.

## Environment Setup

This project uses a combination of **Conda** (for SageMath and core scientific packages) and **pip** (for additional dependencies).

### Recommended Setup (Conda)

This is the most reliable way to set up the full environment, especially if you need **SageMath**.

```bash
# 0. One-time: initialise conda for your shell (zsh on macOS)
/opt/homebrew/Caskroom/miniforge/base/bin/conda init zsh
# Then open a new terminal so the shell picks up the changes.

# 1. Create the Conda environment
conda env create -f environment.yml

# 2. Activate the environment
conda activate maths

# 3. Install additional pip dependencies (antlr4 + mcp[cli])
pip install -r requirements.txt
```

> **Troubleshooting `CondaError: Run 'conda init' before 'conda activate'`**
> This means conda is not initialised for your current shell. Run step 0 above,
> open a new terminal, then retry. If you need to run commands in the same
> session without re-opening, use the full path:
> ```bash
> /opt/homebrew/Caskroom/miniforge/base/bin/conda run -n maths python ...
> ```

---

## MCP Server — `sympy-verifier`

The `mcp_server.py` in this directory is a [FastMCP](https://github.com/jlowin/fastmcp) server that exposes SymPy-backed equation verification tools to Claude Code. It is registered in `.mcp.json` at the repository root and **starts automatically** when Claude Code opens this project.

### Tools

| Tool | Purpose |
|---|---|
| `verify_equation` | Symbolic equality check via `simplify(lhs - rhs) == 0` |
| `check_zero` | Whether an expression is identically zero |
| `simplify_expression` | Canonical SymPy form + LaTeX of an expression |
| `evaluate_at` | Substitute values and evaluate numerically |
| `verify_latex_equation` | Parse raw LaTeX and verify equality (no translation needed) |
| `verify_with_sage` | Exact number-theory checks using SageMath 10.5 |

### Manual start (for testing outside Claude Code)

```bash
conda run --no-capture-output -n maths python sympy/mcp_server.py
```

The server reads JSON-RPC on stdin and writes responses on stdout. Use `Ctrl-C` to stop it. To test with the MCP CLI:

```bash
conda run -n maths mcp dev sympy/mcp_server.py
```

### How Claude uses it

See [`CLAUDE.md`](CLAUDE.md) for the full verification workflow. The short version: Claude reads a Markdown proof note, extracts all equation claims, translates them to SymPy notation, calls the MCP tools, and returns a pass/fail table.

---

## `/sympy` Skill

A project-level Claude Code slash command defined at [`.claude/commands/sympy.md`](../.claude/commands/sympy.md).

### Usage

In Claude Code, type:

```
/sympy project/fibonacci-kernel.md
```

or with the `@` file picker:

```
/sympy @project/fibonacci-kernel.md
```

Claude will read the file, extract all LaTeX equation claims, call the `sympy-verifier` MCP tools for each one, and return a verification report table:

```
## Verification Report: project/fibonacci-kernel.md

| # | Claim                      | Location  | Result | Notes |
|---|----------------------------|-----------|--------|-------|
| 1 | Closed form F2             | §2 Thm F2 | PASS   | —     |
| 2 | K_r(0) = 2r/(1-r-r²)      | §2 Thm F4 | PASS   | —     |
| 3 | Total mass via Parseval    | §4        | PASS   | —     |

**Summary:** 3 claims checked — 3 PASS, 0 FAIL, 0 ERROR, 2 SKIP.
```

### Prerequisites

The `maths` conda environment must be created and the MCP server registered before using the skill:

```bash
# One-time setup (from repo root)
/opt/homebrew/Caskroom/miniforge/base/bin/conda env create -f sympy/environment.yml
/opt/homebrew/Caskroom/miniforge/base/bin/conda run -n maths pip install -r sympy/requirements.txt
```

After setup, the server starts automatically when Claude Code opens this project (registered in `.mcp.json`).