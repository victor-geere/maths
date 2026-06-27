---
title: Integration by Substitution
tag: calculus
summary: Reversing the chain rule to simplify integrals by changing the variable of integration.
links:
  - fundamental-theorem-calculus
  - chain-rule
  - integration-by-parts
---

# Integration by Substitution

**Integration by substitution** (also called $u$-substitution) is the most widely used integration technique. It is the direct reversal of the chain rule: just as the chain rule differentiates a composite function $f(g(x))$ by multiplying $f'(g(x))$ by $g'(x)$, substitution recognises a composite structure inside an integral and replaces $g(x)$ with a single variable $u$, converting a complicated integral into a simpler one. The key is spotting that the integrand contains a function $g(x)$ and its derivative $g'(x)$ as a factor.

## Formula

If $u = g(x)$, then $du = g'(x)\,dx$, and:

$$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$$

## Method

1. Choose a substitution $u = g(x)$ — usually the "inner" function of a composite.
2. Compute $du = g'(x)\,dx$ and rewrite $dx = du/g'(x)$.
3. Express the entire integrand in terms of $u$.
4. Integrate with respect to $u$.
5. Back-substitute $u = g(x)$ to return to $x$.

## Examples

**$\int 2x\cos(x^2)\,dx$:** let $u = x^2$, $du = 2x\,dx$:

$$\int \cos u\,du = \sin u + C = \sin(x^2) + C$$

**$\int \frac{e^{\sqrt{x}}}{\sqrt{x}}\,dx$:** let $u = \sqrt{x}$, $du = \frac{1}{2\sqrt{x}}\,dx$:

$$2\int e^u\,du = 2e^u + C = 2e^{\sqrt{x}} + C$$

**$\int \tan x\,dx$:** let $u = \cos x$, $du = -\sin x\,dx$:

$$\int \frac{\sin x}{\cos x}\,dx = -\int \frac{du}{u} = -\ln|u| + C = -\ln|\cos x| + C$$

## Definite Integrals

Change the limits of integration along with the variable:

$$\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$

**Example:** $\int_0^1 2x e^{x^2}\,dx$. Let $u=x^2$: limits $0\to 0$, $1\to 1$:

$$\int_0^1 e^u\,du = \bigl[e^u\bigr]_0^1 = e - 1$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $u$-substitution | another name for integration by substitution |
| $u = g(x)$ | the substitution — replacing a composite expression by a single variable |
| $du = g'(x)\,dx$ | the differential of $u$ |
| $g'(x)$ | derivative of the substituted function |
| Chain rule | $\frac{d}{dx}[f(g(x))] = f'(g(x))\,g'(x)$ |
| Back-substitute | replacing $u$ with $g(x)$ at the end to express the answer in $x$ |
| $\ln|u|$ | natural log of the absolute value of $u$ |
| Composite function | a function of the form $f(g(x))$ |
| $C$ | constant of integration |
| Limits of integration | the values $a$ and $b$ in $\int_a^b$; must be converted when the variable changes |
