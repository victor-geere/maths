"""SymPy MCP equation verification server.

Exposes six tools to Claude Code:
  verify_equation        — check lhs == rhs symbolically
  check_zero             — check expr == 0 symbolically
  simplify_expression    — simplify and return SymPy + LaTeX form
  evaluate_at            — substitute values and evaluate numerically
  verify_latex_equation  — parse raw LaTeX and verify equality
  verify_with_sage       — run arbitrary Sage code for exact number-theory checks

Start: conda run --no-capture-output -n maths python sympy/mcp_server.py
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from typing import Any

import sympy as sp
from sympy import latex, simplify, sympify
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sympy-verifier")


def _resolve_sage_bin() -> str | None:
    """Locate the Sage executable.

    The MCP server runs inside the pinned ``maths`` conda env, which does not
    contain Sage (Sage's heavy dependency tree lives in its own ``sage`` env).
    Resolution order:
      1. ``SAGE_BIN`` env var (absolute path), if set and executable.
      2. ``sage`` on PATH.
      3. A sibling conda env named ``sage`` next to the current env.
    Returns the path, or None if not found.
    """
    candidate = os.environ.get("SAGE_BIN")
    if candidate and os.access(candidate, os.X_OK):
        return candidate

    on_path = shutil.which("sage")
    if on_path:
        return on_path

    # Sibling conda env: .../envs/<current>/bin/python -> .../envs/sage/bin/sage
    envs_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.sys.executable)))
    sibling = os.path.join(envs_dir, "sage", "bin", "sage")
    if os.access(sibling, os.X_OK):
        return sibling

    return None


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _build_symbol_map(symbols: str, assumptions: str) -> dict[str, sp.Symbol]:
    """Return a {name: Symbol} dict from space-separated names and comma-separated assumptions."""
    if not symbols.strip():
        return {}
    assumption_kwargs: dict[str, bool] = {}
    for a in (tok.strip() for tok in assumptions.split(",") if tok.strip()):
        assumption_kwargs[a] = True
    return {
        name: sp.Symbol(name, **assumption_kwargs)
        for name in symbols.split()
        if name.strip()
    }


def _parse(expr_str: str, symbol_map: dict) -> sp.Expr:
    """Parse a SymPy-notation string into a SymPy expression."""
    local_ns: dict = {**sp.__dict__, **symbol_map}
    return sympify(expr_str, locals=local_ns)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@mcp.tool()
def verify_equation(
    lhs: str,
    rhs: str,
    symbols: str = "",
    assumptions: str = "",
) -> dict[str, Any]:
    """Verify that two SymPy-notation expressions are symbolically equal.

    Checks simplify(lhs - rhs) == 0. For complex LaTeX that is hard to
    translate manually, use verify_latex_equation instead.

    Args:
        lhs: Left-hand side in SymPy notation, e.g. "2*r/(1 - r - r**2)".
        rhs: Right-hand side in SymPy notation.
        symbols: Space-separated symbol names, e.g. "r theta n".
        assumptions: Comma-separated SymPy assumptions applied to all symbols,
            e.g. "positive,real". Common values: positive, negative, real,
            complex, integer, nonnegative.

    Returns:
        {"equal": bool, "simplified_diff": str, "latex_diff": str, "error": str|None}
    """
    try:
        sym = _build_symbol_map(symbols, assumptions)
        lhs_expr = _parse(lhs, sym)
        rhs_expr = _parse(rhs, sym)
        diff = simplify(lhs_expr - rhs_expr)
        equal = diff == 0
        return {
            "equal": equal,
            "simplified_diff": str(diff),
            "latex_diff": latex(diff),
            "error": None,
        }
    except Exception as exc:
        return {"equal": False, "simplified_diff": None, "latex_diff": None, "error": str(exc)}


@mcp.tool()
def check_zero(
    expr: str,
    symbols: str = "",
    assumptions: str = "",
) -> dict[str, Any]:
    """Check whether a SymPy expression simplifies to zero.

    Use for "the error term vanishes" or "the correction is identically zero" claims.

    Args:
        expr: Expression string in SymPy notation.
        symbols: Space-separated symbol names.
        assumptions: Comma-separated SymPy assumptions.

    Returns:
        {"is_zero": bool, "simplified": str, "latex": str, "error": str|None}
    """
    try:
        sym = _build_symbol_map(symbols, assumptions)
        parsed = _parse(expr, sym)
        simplified = simplify(parsed)
        return {
            "is_zero": simplified == 0,
            "simplified": str(simplified),
            "latex": latex(simplified),
            "error": None,
        }
    except Exception as exc:
        return {"is_zero": False, "simplified": None, "latex": None, "error": str(exc)}


@mcp.tool()
def simplify_expression(
    expr: str,
    symbols: str = "",
    assumptions: str = "",
) -> dict[str, Any]:
    """Simplify a SymPy expression and return its canonical form and LaTeX.

    Useful as a first pass before comparing two expressions, or to see what
    SymPy makes of a complicated formula.

    Args:
        expr: Expression string in SymPy notation.
        symbols: Space-separated symbol names.
        assumptions: Comma-separated SymPy assumptions.

    Returns:
        {"result": str, "latex": str, "error": str|None}
    """
    try:
        sym = _build_symbol_map(symbols, assumptions)
        parsed = _parse(expr, sym)
        result = simplify(parsed)
        return {"result": str(result), "latex": latex(result), "error": None}
    except Exception as exc:
        return {"result": None, "latex": None, "error": str(exc)}


@mcp.tool()
def evaluate_at(
    expr: str,
    substitutions: str,
    symbols: str = "",
    assumptions: str = "",
    precision: int = 15,
) -> dict[str, Any]:
    """Substitute values into a SymPy expression and evaluate numerically.

    Use for §6/§7 numerical spot-checks: substitute specific parameter values
    and compare the result against the table value in the proof note.

    Args:
        expr: Expression string in SymPy notation.
        substitutions: JSON object mapping symbol names to numeric values,
            e.g. '{"r": 0.5, "theta": 0, "n": 3}'.
        symbols: Space-separated names of symbols that are NOT substituted
            (i.e. remain symbolic after evaluation).
        assumptions: Comma-separated SymPy assumptions.
        precision: Significant figures for mpmath numerical evaluation (default 15).

    Returns:
        {"result": str, "numeric": float|None, "error": str|None}
    """
    try:
        sym = _build_symbol_map(symbols, assumptions)
        parsed = _parse(expr, sym)
        subs_raw: dict = json.loads(substitutions)
        subs_map = {sp.Symbol(k): v for k, v in subs_raw.items()}
        result = parsed.subs(subs_map)
        try:
            numeric = float(sp.N(result, precision))
        except Exception:
            numeric = None
        return {"result": str(result), "numeric": numeric, "error": None}
    except Exception as exc:
        return {"result": None, "numeric": None, "error": str(exc)}


@mcp.tool()
def verify_latex_equation(
    lhs_latex: str,
    rhs_latex: str,
) -> dict[str, Any]:
    """Parse two raw LaTeX expressions and verify they are symbolically equal.

    Preferred over verify_equation when the LaTeX is complex and manual
    translation to SymPy notation is error-prone. Uses
    sympy.parsing.latex.parse_latex (requires antlr4-python3-runtime~=4.11).

    Args:
        lhs_latex: Left-hand side in LaTeX, e.g. r"\\frac{2r}{1-r-r^{2}}".
        rhs_latex: Right-hand side in LaTeX.

    Returns:
        {"equal": bool, "simplified_diff": str, "latex_diff": str, "error": str|None}
    """
    try:
        from sympy.parsing.latex import parse_latex  # deferred: antlr4 startup cost
        lhs_expr = parse_latex(lhs_latex)
        rhs_expr = parse_latex(rhs_latex)
        diff = simplify(lhs_expr - rhs_expr)
        equal = diff == 0
        return {
            "equal": equal,
            "simplified_diff": str(diff),
            "latex_diff": latex(diff),
            "error": None,
        }
    except Exception as exc:
        return {"equal": False, "simplified_diff": None, "latex_diff": None, "error": str(exc)}


@mcp.tool()
def verify_with_sage(
    code: str,
    timeout: int = 30,
) -> dict[str, Any]:
    """Run arbitrary SageMath code and return its stdout.

    Use for exact number-theory computations beyond SymPy's reach:
    cyclotomic polynomials, exact Dirichlet L-values, zeta zeros, class groups,
    modular forms, exact Mellin transforms, etc.

    The code runs in a subprocess with SageMath 10.5 (conda env 'maths').
    Use print() to emit the values you want to inspect.

    Example:
        code = "R.<x> = ZZ[]; print(factor(x**5 - 1))"

    Args:
        code: SageMath code to execute.
        timeout: Maximum execution time in seconds (default 30).

    Returns:
        {"output": str, "error": str|None}
    """
    sage_bin = _resolve_sage_bin()
    if sage_bin is None:
        return {
            "output": None,
            "error": (
                "sage executable not found. Install it with "
                "`conda create -y -n sage -c conda-forge sage`, then either put it "
                "on PATH or set the SAGE_BIN env var to its absolute path "
                "(e.g. .../envs/sage/bin/sage)."
            ),
        }
    try:
        result = subprocess.run(
            [sage_bin, "-c", code],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if result.returncode != 0:
            error_msg = result.stderr.strip() or f"sage exited with code {result.returncode}"
            return {"output": result.stdout, "error": error_msg}
        return {"output": result.stdout, "error": None}
    except FileNotFoundError:
        return {
            "output": None,
            "error": f"sage executable not found at resolved path: {sage_bin}",
        }
    except subprocess.TimeoutExpired:
        return {"output": None, "error": f"sage execution timed out after {timeout}s"}
    except Exception as exc:
        return {"output": None, "error": str(exc)}


if __name__ == "__main__":
    mcp.run(transport="stdio")
