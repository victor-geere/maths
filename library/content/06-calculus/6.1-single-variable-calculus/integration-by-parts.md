---
title: Integration by Parts
tag: calculus
summary: A technique for integrating products of functions, derived from the product rule for differentiation.
links:
  - fundamental-theorem-calculus
  - integration-by-substitution
  - derivative-definition
---

# Integration by Parts

**Integration by parts** is the integration counterpart of the product rule for differentiation. Just as the product rule tells us how to differentiate $u \cdot v$, integration by parts tells us how to integrate a product $u \cdot v'$ by trading it for $u \cdot v$ minus the integral of $u' \cdot v$. This is useful when one factor of the integrand becomes simpler upon differentiation while the other is easy to integrate. The method handles integrands like $x e^x$, $x\ln x$, $e^x\sin x$, and $\arctan x$ — products where substitution alone fails.

## Formula

$$\int u\, dv = uv - \int v\, du$$

where $u = u(x)$ and $dv = v'(x)\,dx$.

**Derivation:** from the product rule $\frac{d}{dx}(uv) = u\frac{dv}{dx} + v\frac{du}{dx}$, integrate both sides.

## Choosing $u$ and $dv$ — the LIATE Rule

Choose $u$ to be the factor that simplifies when differentiated; choose $dv$ to be the rest. A useful priority order:

**L**ogarithms → **I**nverse trig → **A**lgebraic (polynomials) → **T**rigonometric → **E**xponential

## Examples

**$\int x e^x\,dx$:** let $u = x$, $dv = e^x\,dx$:

$$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C = e^x(x-1) + C$$

**$\int \ln x\,dx$:** let $u = \ln x$, $dv = dx$:

$$\int \ln x\,dx = x\ln x - \int x \cdot \frac{1}{x}\,dx = x\ln x - x + C$$

**$\int e^x \sin x\,dx$:** apply twice, then solve algebraically:

$$I = -e^x\cos x + \int e^x\cos x\,dx = -e^x\cos x + e^x\sin x - I$$

$$2I = e^x(\sin x - \cos x) \implies I = \frac{e^x(\sin x - \cos x)}{2} + C$$

## Definite Integrals

$$\int_a^b u\, dv = \bigl[uv\bigr]_a^b - \int_a^b v\, du$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\int u\,dv = uv - \int v\,du$ | integration by parts formula |
| $u$ | the factor chosen to differentiate |
| $dv$ | the factor chosen to integrate |
| $du$ | differential of $u$: $du = u'(x)\,dx$ |
| $v$ | antiderivative of $dv$ |
| $C$ | constant of integration |
| LIATE | mnemonic for choosing $u$: Logarithm, Inverse trig, Algebraic, Trig, Exponential |
| Product rule | $\frac{d}{dx}(uv) = u'v + uv'$ |
| $e^x$ | exponential function |
| $\ln x$ | natural logarithm |
| $\bigl[f(x)\bigr]_a^b$ | $f(b) - f(a)$, the evaluation of $f$ at the endpoints |
