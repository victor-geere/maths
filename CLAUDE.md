# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository structure

Folder-specific guidance (how to run code, detailed structure, per-track status tables) lives in
each folder's own `CLAUDE.md`; this file covers only the repo-wide policy every note obeys.

```
victor/    # Python numerics + two research tracks — see victor/CLAUDE.md
leo/       # (empty — scratch space, .gitkeep only)
plan/      # master task list / open-work board — see plan/CLAUDE.md
library/   # reference library, one folder per subject area (30 subject folders under content/)
sympy/     # SymPy MCP verification server — see sympy/CLAUDE.md
```

## Rigour convention

Every result must be tagged — maintain these distinctions strictly:

- **proven** — complete proof present in the note, or a classical result with citation
- **conditional** — depends on RH or another named hypothesis; state it explicitly
- **RH-equivalent** — proven *equivalent* to RH (e.g. Weil positivity, Hermite–Biehler positivity, Connes' global trace formula). These mark the **frontier**; an RH-equivalent restatement is not itself a step toward a proof, and may never be presented as one.
- **heuristic/exploratory** — conjecture or numerical evidence only

## Math rendering

Project notes use standard LaTeX math (rendered by GitHub's KaTeX). Avoid `\operatorname{}`— use `\mathrm{}` instead (GitHub's renderer disallows `\operatorname`).
