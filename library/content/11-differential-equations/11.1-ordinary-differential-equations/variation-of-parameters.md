---
title: Variation of Parameters
tag: ode
summary: A general method for finding a particular solution to any linear ODE by allowing the constants in the homogeneous solution to become functions of x.
links:
  - constant-coeff-odes
  - undetermined-coefficients
  - linear-first-order
---

# Variation of Parameters

**Variation of parameters** is a general method for finding a particular solution to a non-homogeneous linear ODE, working for any forcing function $f(x)$ — not just those in the undetermined coefficients table. The idea is elegant: take the homogeneous solution $y_h = C_1 y_1 + C_2 y_2$ and replace the constants $C_1, C_2$ with unknown functions $u_1(x), u_2(x)$ to be determined. Substituting $y_p = u_1 y_1 + u_2 y_2$ into the ODE and imposing a convenient side condition leads to a $2 \times 2$ system solved via the **Wronskian**. The method extends to higher-order equations and requires only that the homogeneous solution is known.

## Setup (2nd Order)

Given $y'' + p(x)y' + q(x)y = f(x)$ with homogeneous solutions $y_1, y_2$.

Seek $y_p = u_1(x)y_1 + u_2(x)y_2$ where $u_1, u_2$ satisfy the system:

$$u_1'y_1 + u_2'y_2 = 0$$
$$u_1'y_1' + u_2'y_2' = f(x)$$

## Wronskian

$$W = W(y_1, y_2) = \begin{vmatrix}y_1 & y_2 \\ y_1' & y_2'\end{vmatrix} = y_1 y_2' - y_2 y_1'$$

## Solution by Cramer's Rule

$$u_1' = -\frac{y_2 f}{W}, \qquad u_2' = \frac{y_1 f}{W}$$

Integrate:

$$u_1 = -\int\frac{y_2 f}{W}\,dx, \qquad u_2 = \int\frac{y_1 f}{W}\,dx$$

## Example

$y'' + y = \sec x$. Homogeneous: $y_1 = \cos x$, $y_2 = \sin x$, $W = 1$.

$$u_1' = -\sin x\sec x = -\tan x \implies u_1 = \ln|\cos x|$$

$$u_2' = \cos x\sec x = 1 \implies u_2 = x$$

$$y_p = \cos x\ln|\cos x| + x\sin x$$

## Advantages over Undetermined Coefficients

- Works for **any** continuous $f(x)$, including $\ln x$, $1/x$, $e^{x^2}$
- Works for **variable-coefficient** equations (if $y_1, y_2$ are known)

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $y_p = u_1 y_1 + u_2 y_2$ | particular solution via variation of parameters |
| $u_1(x), u_2(x)$ | the "varied parameters" (functions replacing constants) |
| $W(y_1, y_2)$ | Wronskian: $y_1 y_2' - y_2 y_1'$ |
| Wronskian | determinant measuring linear independence of solutions; $W \neq 0$ |
| $y_1, y_2$ | linearly independent solutions to the homogeneous equation |
| Cramer's rule | solving the $2\times2$ system for $u_1'$ and $u_2'$ |
| $f(x)$ | forcing function on the right-hand side |
| $p(x), q(x)$ | possibly variable coefficients in the ODE |
| $\sec x$ | secant function: $1/\cos x$ |
| Abel's identity | $W(x) = W(x_0)\exp\!\left(-\int_{x_0}^x p(t)\,dt\right)$ |
