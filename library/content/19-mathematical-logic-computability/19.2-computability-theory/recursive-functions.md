---
title: Recursive Functions
tag: logic
summary: The recursive functions are built from zero, successor, and projection by composition, primitive recursion, and minimisation; they form the same class as Turing-computable functions, giving an algebraic characterisation of computability.
links:
  - church-turing
  - turing-machines
  - halting-problem
---

# Recursive Functions

The **recursive functions** (Kleene, 1936) provide an algebraic characterisation of computability, building the computable functions from a small set of base functions using three closure operations. The **primitive recursive functions** are closed under composition and primitive recursion, covering nearly all functions computed in practice (factorial, Fibonacci, primality). Adding **minimisation** (unbounded search) gives the **general recursive functions** (also called $\mu$-recursive functions), which coincide exactly with the Turing-computable functions. The Ackermann function is computable but not primitive recursive, showing that primitive recursion alone is insufficient for full computability.

## Primitive Recursive Functions

**Base functions**:
- Zero: $Z(x) = 0$
- Successor: $S(x) = x + 1$
- Projections: $P_i^n(x_1,\ldots,x_n) = x_i$

**Closure operations**:
- **Composition**: $h(\vec{x}) = f(g_1(\vec{x}),\ldots,g_m(\vec{x}))$
- **Primitive recursion**: $h(\vec{x}, 0) = f(\vec{x})$; $h(\vec{x}, y+1) = g(\vec{x}, y, h(\vec{x},y))$

## General Recursive Functions ($\mu$-recursive)

Add **minimisation**: $h(\vec{x}) = \mu y[f(\vec{x},y) = 0]$ = least $y$ with $f(\vec{x},y) = 0$ (undefined if none exists).

**Theorem**: The general recursive functions = the Turing-computable functions.

## Ackermann Function

$$A(0,n) = n+1,\ A(m+1,0) = A(m,1),\ A(m+1,n+1) = A(m, A(m+1,n))$$

$A$ is computable but grows faster than any primitive recursive function, so it is not primitive recursive.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Primitive recursive function | built from $Z, S, P_i^n$ by composition and primitive recursion |
| Composition $h = f \circ (g_1,\ldots,g_m)$ | $h(\vec{x}) = f(g_1(\vec{x}),\ldots,g_m(\vec{x}))$ |
| Primitive recursion | $h(\vec{x},0) = f(\vec{x})$; $h(\vec{x},y+1) = g(\vec{x},y,h(\vec{x},y))$ |
| Minimisation $\mu y$ | least $y$ such that $f(\vec{x},y) = 0$ |
| $\mu$-recursive function | primitive recursive + minimisation = general recursive |
| Ackermann function $A(m,n)$ | computable but not primitive recursive |
| Partial function | may be undefined on some inputs |
| Total function | defined on all inputs |
