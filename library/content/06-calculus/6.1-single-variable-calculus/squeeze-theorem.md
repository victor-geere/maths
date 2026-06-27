---
title: Squeeze Theorem
tag: calculus
summary: If a function is sandwiched between two functions that share the same limit, it must share that limit too.
links:
  - limits
  - continuity
  - lhopital
---

# Squeeze Theorem

The **Squeeze Theorem** (also called the Sandwich Theorem or Pinching Theorem) provides a way to evaluate limits that are difficult to compute directly, by trapping the function of interest between two simpler functions whose limits are known and equal. If $f(x)$ is always between $g(x)$ and $h(x)$ near a point, and $g$ and $h$ both approach the same value $L$, then $f$ is forced — or "squeezed" — to approach $L$ as well. It is the standard tool for proving $\lim_{x\to 0}\frac{\sin x}{x} = 1$ rigorously.

## Statement

If $g(x) \leq f(x) \leq h(x)$ for all $x$ near $a$ (but not necessarily at $a$ itself), and:

$$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$$

then:

$$\lim_{x \to a} f(x) = L$$

The theorem holds equally for one-sided limits and limits as $x \to \pm\infty$.

## Classic Example: $\lim_{x \to 0} \frac{\sin x}{x} = 1$

Using the geometric inequality $\sin x \leq x \leq \tan x$ for $0 < x < \pi/2$:

Divide through by $\sin x > 0$:

$$1 \leq \frac{x}{\sin x} \leq \frac{1}{\cos x}$$

Take reciprocals (reversing inequalities):

$$\cos x \leq \frac{\sin x}{x} \leq 1$$

Since $\lim_{x\to 0}\cos x = 1$ and $\lim_{x\to 0} 1 = 1$, the Squeeze Theorem gives $\lim_{x\to 0}\frac{\sin x}{x} = 1$.

## Example: Oscillating Function

$$\lim_{x \to 0}\, x^2 \sin\!\left(\frac{1}{x}\right)$$

Since $-1 \leq \sin(1/x) \leq 1$ for all $x \neq 0$:

$$-x^2 \leq x^2\sin\!\left(\frac{1}{x}\right) \leq x^2$$

Both bounds tend to $0$ as $x \to 0$, so the limit is $0$.

## Example: Sequence Form

If $0 \leq a_n \leq b_n$ for all $n$ and $b_n \to 0$, then $a_n \to 0$. This version applies to sequences as well as functions.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\lim_{x \to a} f(x) = L$ | $f(x)$ approaches $L$ as $x$ approaches $a$ |
| $g(x) \leq f(x) \leq h(x)$ | $f$ is sandwiched between $g$ and $h$ |
| Squeeze / Sandwich / Pinching Theorem | names for the same result |
| One-sided limit | limit from the left ($x \to a^-$) or right ($x \to a^+$) only |
| $x \to \pm\infty$ | $x$ grows without bound positively or negatively |
| $\sin x$ | sine function |
| $\tan x$ | tangent function |
| Geometric inequality | an inequality justified by comparing areas or lengths in a geometric figure |
| $a_n$ | the $n$-th term of a sequence |
| Oscillating function | a function that alternates in sign without settling; e.g. $\sin(1/x)$ near 0 |
