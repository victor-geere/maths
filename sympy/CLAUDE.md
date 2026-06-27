# CLAUDE.md — SymPy Equation Verification

This file guides Claude Code when asked to verify the mathematical claims in a Markdown proof note using the `sympy-verifier` MCP server.

> **Prerequisite:** the `maths` conda environment must exist and the MCP server must be registered in `.mcp.json`.
> See `README.md` for one-time setup instructions. The MCP tools listed below are only available once that environment is active.

## MCP tools available

| Tool | Use for |
|---|---|
| `verify_equation(lhs, rhs, symbols, assumptions)` | Symbolic equality check: `simplify(lhs - rhs) == 0` |
| `check_zero(expr, symbols, assumptions)` | Whether an expression vanishes identically |
| `simplify_expression(expr, symbols, assumptions)` | Canonical form + LaTeX of an expression |
| `evaluate_at(expr, substitutions, symbols, assumptions, precision)` | Numerical spot-check at specific values |
| `verify_latex_equation(lhs_latex, rhs_latex)` | Parse raw LaTeX and check equality (no manual translation needed) |
| `verify_with_sage(code, timeout)` | Exact number-theory checks beyond SymPy (cyclotomic, L-values, zeta zeros) |

---

## Verification workflow

### Step 1 — Extract claims

Read the Markdown file. Identify every `$$...$$` block and inline `$...$` expression that states an **equality, identity, or "iff"** claim. Skip:
- Definitions using `:=` or "we define" — not verifiable claims.
- Claims tagged **heuristic** or **exploratory** in the note — SymPy cannot verify these.
- Claims that require analytic continuation or limit arguments (e.g. "$r \to 1^-$") — flag as SKIP.

### Step 2 — Classify each claim

| Type | Example | Tool |
|---|---|---|
| Closed-form identity | $K_r(0) = \frac{2r}{1-r-r^2}$ | `verify_equation` or `verify_latex_equation` |
| Expression vanishes | "the error term is zero" | `check_zero` |
| Numerical spot-check | "equals $P(4)$ to 10 digits" | `evaluate_at`, compare manually |
| Exact number theory | factorisation, class group order | `verify_with_sage` |

### Step 3 — Translate to SymPy notation

For `verify_equation` / `check_zero` / `simplify_expression`, inputs must be valid Python parseable by `sympify()`.

| LaTeX | SymPy notation |
|---|---|
| `\frac{a}{b}` | `a/b` |
| `a^{n}` | `a**n` |
| `\sqrt{a}` | `sqrt(a)` |
| `\Re(z)` | `re(z)` |
| `e^{f(x)}` | `exp(f(x))` |
| `\cos\theta` | `cos(theta)` |
| `\sum_{n=1}^{N} f(n)` | `Sum(f(n), (n, 1, N))` |
| `\varphi` (golden ratio) | `(1 + sqrt(5))/2` |
| `F_n` (Fibonacci) | `fibonacci(n)` |
| `\zeta(s)` | `zeta(s)` |
| `\Gamma(s)` | `gamma(s)` |
| `\mathrm{Li}_s(z)` | `polylog(s, z)` |

If you are uncertain about a translation, use `verify_latex_equation` and pass the raw LaTeX strings directly.

### Step 4 — Declare symbols and assumptions

Always pass the symbols that appear in the expression. Use assumptions where the proof note specifies a domain constraint:

```
symbols="r n"         assumptions="positive"       # r > 0, n > 0
symbols="r"           assumptions="positive,real"  # 0 < r < 1 (real positive)
symbols="s"           assumptions="complex"
symbols="theta"       assumptions="real"
symbols="n"           assumptions="integer,nonnegative"
```

### Step 5 — Call tools and record results

For each claim, call the appropriate tool and record:

| Label | Meaning |
|---|---|
| **PASS** | `equal=True` or `is_zero=True` |
| **FAIL** | `equal=False`; record `simplified_diff` to show the discrepancy |
| **ERROR** | Tool returned `error` (parse failure, timeout, antlr4 missing) |
| **SKIP** | Definition, heuristic claim, or requires analysis beyond SymPy |

### Step 6 — Report

Return a Markdown table:

```markdown
| # | Claim | Location | Result | Notes |
|---|---|---|---|---|
| 1 | $K_r(0) = 2r/(1-r-r^2)$ | §2 Thm F4 | PASS | — |
| 2 | closed form F2 | §2 Thm F2 | PASS | verified via verify_latex_equation |
| 3 | $\|\Psi_2\|^2 = P(4)$ | §6 | PASS | evaluate_at r=2; matches to 10 digits |
```

Finish with a summary line: `N claims checked: K PASS, M FAIL, J ERROR, L SKIP.`
Flag every FAIL and ERROR row for human review.

---

## Common pitfalls

- **SymPy cannot close infinite sums** — `Sum(fibonacci(n)*r**n, (n,1,oo))` will not simplify to the rational closed form. Instead verify the closed form equals a truncated partial sum at a specific $r$ via `evaluate_at`, or verify the rational form satisfies the recurrence directly.
- **Trigonometric identities** — add `assumptions="real"` to all angular symbols so `simplify` uses real-valued trig identities.
- **Complex expressions** — `re(z)` and `im(z)` only simplify correctly if `z` is declared with explicit real/imaginary parts or assumptions. Prefer `verify_latex_equation` for complex-valued kernel expressions.
- **The `equal=False` case is not a proof of error** — SymPy may fail to simplify a true identity (it returns `simplified_diff` non-zero but non-constant). In that case, escalate to `verify_with_sage` or flag as SKIP with a note.
- **`antlr4` errors** — the `verify_latex_equation` tool requires `antlr4-python3-runtime==4.11.1` (exact version). If you see an antlr4 import error, run `conda run -n maths pip install antlr4-python3-runtime==4.11.1` and restart the MCP server.
