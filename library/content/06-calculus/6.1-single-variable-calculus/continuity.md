---
title: Continuity
tag: analysis
summary: A function is continuous at a if lim_{x→a} f(x) = f(a).
links:
  - limits
  - derivative-definition
---

## Key Formula

$$f \text{ continuous at } a \iff \lim_{x \to a} f(x) = f(a)$$

## Notes

**Three conditions** must all hold for continuity at $a$:

1. $f(a)$ is defined
2. $\displaystyle\lim_{x \to a} f(x)$ exists
3. They are equal

### Types of discontinuity

| Type | Description | Example |
|---|---|---|
| Removable | Limit exists but ≠ $f(a)$ | $\frac{\sin x}{x}$ at $0$ (fixed by setting $f(0)=1$) |
| Jump | Left and right limits differ | $\text{sign}(x)$ at $0$ |
| Infinite | Limit is $\pm\infty$ | $\frac{1}{x}$ at $0$ |
| Oscillatory | Limit does not exist | $\sin(1/x)$ at $0$ |

### Key theorems

**Intermediate Value Theorem (IVT):** if $f$ is continuous on $[a,b]$ and $f(a) < c < f(b)$, then there exists $x_0 \in (a,b)$ with $f(x_0) = c$.

**Extreme Value Theorem (EVT):** a continuous function on a closed bounded interval $[a,b]$ attains its maximum and minimum.

### Uniform continuity

$f$ is **uniformly continuous** on $S$ if $\delta$ can be chosen independently of the point:

$$\forall\varepsilon>0\;\exists\delta>0:\; |x-y|<\delta \;\Rightarrow\; |f(x)-f(y)|<\varepsilon \quad\forall x,y\in S$$

Every continuous function on a compact set is uniformly continuous (Heine–Cantor).
