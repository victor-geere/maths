Verify all mathematical claims in the file `$ARGUMENTS` using the `sympy-verifier` MCP server. Follow the workflow defined in `sympy/CLAUDE.md` exactly.

## Steps

1. **Read the file** at `$ARGUMENTS` in full.

2. **Extract every math claim** — scan all `$$...$$` blocks and inline `$...$` expressions. For each one, decide:
   - **VERIFY** — an explicit equality, identity, or "iff" statement that SymPy can check
   - **SKIP** — a definition (`:=`, "we define", "let"), a heuristic/exploratory claim, or one requiring analytic continuation

3. **Verify each VERIFY claim** by calling the appropriate MCP tool:
   - Use `sympy-verifier__verify_equation` for symbolic equalities — translate both sides to SymPy notation first (see the LaTeX→SymPy mapping table in `sympy/CLAUDE.md`)
   - Use `sympy-verifier__verify_latex_equation` when the LaTeX is complex and manual translation is risky — pass raw LaTeX strings directly
   - Use `sympy-verifier__check_zero` for "the expression vanishes" claims
   - Use `sympy-verifier__evaluate_at` for numerical spot-checks (§6/§7 tables) — pass substitutions as a JSON string, e.g. `'{"r": 0.5}'`
   - Use `sympy-verifier__verify_with_sage` for exact number-theory checks beyond SymPy's reach
   - Always declare `symbols` and `assumptions` (e.g. `symbols="r n"`, `assumptions="positive"`)

4. **Record each result** as one of:
   - `PASS` — `equal=true` or `is_zero=true`
   - `FAIL` — `equal=false`; include the `simplified_diff` in the Notes column
   - `ERROR` — tool returned an error; include the error message
   - `SKIP` — definition, heuristic, or beyond SymPy

5. **Output a verification report** in this exact format:

```
## Verification Report: <filename>

| # | Claim | Location | Result | Notes |
|---|---|---|---|---|
| 1 | <short description of the claim> | <§N / Thm label> | PASS/FAIL/ERROR/SKIP | <simplified_diff or error or reason for skip> |
...

**Summary:** N claims checked — K PASS, M FAIL, J ERROR, L SKIP.
```

Flag every FAIL and ERROR row with ⚠️ for human review.

> **Note:** If `equal=false` but the `simplified_diff` is not a constant (SymPy failed to close a true identity), mark as ERROR with note "SymPy could not simplify — try verify_with_sage or manual proof" rather than FAIL.
