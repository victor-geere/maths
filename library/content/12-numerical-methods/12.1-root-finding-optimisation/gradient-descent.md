---
title: Gradient Descent
tag: numerical-methods
summary: An iterative optimisation algorithm that repeatedly moves in the direction of the negative gradient to minimise a differentiable objective function.
links:
  - newton-raphson
  - partial-derivatives
  - grad-div-curl
  - big-o-notation
---

# Gradient Descent

**Gradient descent** is the most widely used optimisation algorithm in science and machine learning. Given a differentiable function $f(\mathbf{x})$ to minimise, each iteration takes a step in the direction of the **negative gradient** $-\nabla f(\mathbf{x})$ — the direction of steepest descent. The step size is controlled by the **learning rate** $\alpha$. When $\alpha$ is chosen well, the iterates converge to a local minimum; when $f$ is convex, they converge to the global minimum. Gradient descent is the engine behind neural network training (via backpropagation), logistic regression, support vector machines, and virtually all large-scale optimisation in data science.

## Algorithm

**Input:** objective $f : \mathbb{R}^d \to \mathbb{R}$, starting point $\mathbf{x}_0$, learning rate $\alpha > 0$.

Repeat until convergence:

$$\mathbf{x}_{n+1} = \mathbf{x}_n - \alpha\, \nabla f(\mathbf{x}_n)$$

## Step Size (Learning Rate)

| $\alpha$ | Behaviour |
|---|---|
| Too large | Overshoots; may diverge or oscillate |
| Too small | Slow convergence |
| Optimal | $\alpha \leq 1/L$ where $L$ is the Lipschitz constant of $\nabla f$ |

For a quadratic $f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T A\mathbf{x}$: optimal $\alpha = 2/(\lambda_{\min} + \lambda_{\max})$.

## Convergence (Convex Case)

For $L$-smooth, $\mu$-strongly convex $f$:

$$f(\mathbf{x}_n) - f^* \leq \left(1 - \frac{\mu}{L}\right)^n (f(\mathbf{x}_0) - f^*)$$

**Linear convergence** with rate $1 - \mu/L$. The condition number $\kappa = L/\mu$ governs the speed.

## Variants

| Variant | Update rule |
|---|---|
| Stochastic GD (SGD) | Use gradient from a single sample |
| Mini-batch GD | Use gradient from a small batch |
| Momentum | $\mathbf{v}_{n+1} = \beta\mathbf{v}_n - \alpha\nabla f$; $\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_{n+1}$ |
| Adam | Adaptive per-parameter learning rates |
| Nesterov | Look-ahead gradient for faster convergence |

## 1D Example

Minimise $f(x) = x^2$, $\alpha = 0.5$, $x_0 = 4$:

$$x_1 = 4 - 0.5(2\cdot 4) = 0, \quad f^* = 0 \text{ reached in 1 step}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\nabla f(\mathbf{x})$ | gradient of $f$: vector of partial derivatives |
| $\alpha$ | learning rate (step size) |
| $\mathbf{x}_{n+1} = \mathbf{x}_n - \alpha\nabla f$ | gradient descent update rule |
| $f^*$ | the minimum value of $f$ |
| $L$-smooth | $\|\nabla f(\mathbf{x}) - \nabla f(\mathbf{y})\| \leq L\|\mathbf{x}-\mathbf{y}\|$ |
| $\mu$-strongly convex | $f(\mathbf{y}) \geq f(\mathbf{x}) + \nabla f(\mathbf{x})^T(\mathbf{y}-\mathbf{x}) + \frac{\mu}{2}\|\mathbf{y}-\mathbf{x}\|^2$ |
| Condition number $\kappa = L/\mu$ | ratio measuring how ill-conditioned the optimisation is |
| SGD | Stochastic Gradient Descent: uses one random sample per step |
| Mini-batch | small random subset of data used to estimate the gradient |
| Convergence | the iterates approach the minimiser as $n \to \infty$ |
| Local minimum | point where $\nabla f = \mathbf{0}$ and Hessian is positive semi-definite |
