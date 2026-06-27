---
title: Limits
tag: calculus
summary: Formalising the idea of a function approaching a value.
links:
  - derivative-definition
  - continuity
  - convergence
---

## Key Formula

$$\lim_{x \to a} f(x) = L \iff \forall\varepsilon>0\;\exists\delta>0:\; 0 < |x-a| < \delta \;\Rightarrow\; |f(x)-L| < \varepsilon$$

## Notes

The **$\varepsilon$–$\delta$ definition** (Weierstrass): $L$ is the limit of $f$ at $a$ if, for every tolerance $\varepsilon$, we can confine $f$ within $\varepsilon$ of $L$ by keeping $x$ within some $\delta$ of $a$.

### One-sided limits

$$\lim_{x\to a^-} f(x) \quad \text{and} \quad \lim_{x\to a^+} f(x)$$

The two-sided limit exists iff both one-sided limits exist **and** are equal.

### Limit laws

If $\lim_{x\to a} f(x) = L$ and $\lim_{x\to a} g(x) = M$:

$$\lim_{x\to a}[f(x)+g(x)] = L+M, \qquad \lim_{x\to a}[f(x)g(x)] = LM$$

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \frac{L}{M} \quad (M \neq 0)$$

### L'Hôpital's rule

For indeterminate forms $\frac{0}{0}$ or $\frac{\infty}{\infty}$:

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

provided the right-hand limit exists. Apply the [[derivative-definition|derivative]] to both numerator and denominator separately.

### Continuity

$f$ is [[continuity|continuous]] at $a$ iff $\displaystyle\lim_{x\to a}f(x) = f(a)$.
