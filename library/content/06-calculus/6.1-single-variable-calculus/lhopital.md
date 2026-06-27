---
title: L'Hôpital's Rule
tag: calculus
summary: Evaluating indeterminate limits of the form 0/0 or ∞/∞ by differentiating numerator and denominator separately.
links:
  - limits
  - derivative-definition
  - squeeze-theorem
---

# L'Hôpital's Rule

When a limit produces an **indeterminate form** such as $0/0$ or $\infty/\infty$, standard limit laws break down — the value cannot be determined from the forms alone. **L'Hôpital's Rule** resolves this by replacing the ratio of functions with the ratio of their derivatives, which often has a determinate limit. First published by the Marquis de l'Hôpital in 1696 (based on work by Johann Bernoulli), it is one of the most practically useful tools in calculus and applies in a surprisingly wide range of situations once indeterminate forms are put into the right shape.

## Statement

If $\lim_{x \to a} f(x) = 0$ and $\lim_{x \to a} g(x) = 0$ (or both tend to $\pm\infty$), and $g'(x) \neq 0$ near $a$, then:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

provided the right-hand limit exists (or is $\pm\infty$). The rule also applies as $x \to \pm\infty$.

## Indeterminate Forms

L'Hôpital's Rule applies directly to $\tfrac{0}{0}$ and $\tfrac{\infty}{\infty}$. Other forms require algebraic manipulation first:

| Form | Rewrite as |
|---|---|
| $0 \cdot \infty$ | $\frac{0}{1/\infty}$ or $\frac{\infty}{1/0}$ |
| $\infty - \infty$ | combine into a single fraction |
| $0^0,\; 1^\infty,\; \infty^0$ | take logarithm: $e^{\lim f\ln g}$ |

## Examples

**$\tfrac{0}{0}$ form:**
$$\lim_{x\to 0}\frac{\sin x}{x} = \lim_{x\to 0}\frac{\cos x}{1} = 1$$

**$\tfrac{\infty}{\infty}$ form:**
$$\lim_{x\to\infty}\frac{x^2}{e^x} = \lim_{x\to\infty}\frac{2x}{e^x} = \lim_{x\to\infty}\frac{2}{e^x} = 0$$

(Applied twice — rule can be iterated.)

**$1^\infty$ form:**
$$\lim_{x\to 0}(1+x)^{1/x}:\quad \ln L = \lim_{x\to 0}\frac{\ln(1+x)}{x} = \lim_{x\to 0}\frac{1/(1+x)}{1} = 1 \implies L = e$$

## Caution

L'Hôpital's Rule requires the indeterminate form to hold — applying it when $\lim g(x) \neq 0$ gives wrong answers. Always verify the form before applying.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\lim_{x \to a}$ | the limit as $x$ approaches $a$ |
| $f'(x)$ | the derivative of $f$ with respect to $x$ |
| Indeterminate form | a limiting expression whose value cannot be decided from the forms alone (e.g. $0/0$, $\infty/\infty$) |
| $0/0$ | indeterminate ratio where both numerator and denominator tend to zero |
| $\infty/\infty$ | indeterminate ratio where both tend to infinity |
| $1^\infty$ | indeterminate power where base $\to 1$ and exponent $\to \infty$ |
| $0^0$ | indeterminate power where both base and exponent tend to zero |
| $e$ | Euler's number ($\approx 2.71828$); base of the natural logarithm |
| $\ln$ | natural logarithm |
| Iterate | apply the rule a second (or more) time when the result is still indeterminate |
