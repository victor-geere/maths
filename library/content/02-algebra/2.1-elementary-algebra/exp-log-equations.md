---
title: Exponential & Logarithmic Equations
tag: algebra
summary: Solving equations involving exponential and logarithmic functions.
links:
  - real-numbers
  - inequalities
---

## Key Identities

$$\ln(e^x) = x, \qquad e^{\ln x} = x \quad (x > 0)$$

$$\log_b(b^x) = x, \qquad b^{\log_b x} = x \quad (x > 0, b > 0, b \neq 1)$$

### Logarithm Laws

$$\log_b(xy) = \log_b x + \log_b y$$
$$\log_b\!\left(\tfrac{x}{y}\right) = \log_b x - \log_b y$$
$$\log_b(x^r) = r\log_b x$$

### Change of Base

$$\log_b x = \frac{\ln x}{\ln b}$$

## Solving Exponential Equations

**Strategy:** take logarithms of both sides.

**Example:** $3^{2x-1} = 27$

$$3^{2x-1} = 3^3 \implies 2x - 1 = 3 \implies x = 2$$

**Example:** $5^x = 17$

$$x = \frac{\ln 17}{\ln 5} \approx 1.76$$

## Solving Logarithmic Equations

**Strategy:** exponentiate both sides or combine logs first.

**Example:** $\log_2(x+3) = 4$

$$x + 3 = 2^4 = 16 \implies x = 13$$

**Example:** $\ln(x) + \ln(x-2) = \ln 8$

$$\ln(x(x-2)) = \ln 8 \implies x^2 - 2x - 8 = 0 \implies x = 4 \text{ (reject } x=-2\text{)}$$

## Notes

- Always check that logarithm arguments remain **positive** after solving.
- Natural log ($\ln$) and $\log_{10}$ are the two most commonly used bases.
