# The Fibonacci Kernel — A Phase‑1 Worked Case

*Phase‑1 deliverable (see [README](../README.md)). Linear recurrences are the
easiest objects in the catalogue: the spectrum is the sequence itself, the kernel
has a rational closed form, and positive definiteness is unconditional. Every
statement below is a theorem with a complete proof or a cited generating‑function
identity. Nothing here is conditional on anything.*

---

## 0. Summary

Apply the general recipe ([spectral-triple.html](../victor/spectral-triple.html) §3) to the
Fibonacci numbers $a_n=F_n$ ($F_0=0,F_1=F_2=1,\dots$) with geometric damping
$w_n=r^n$. Because $F_n\sim\varphi^n/\sqrt5$ with $\varphi=\tfrac{1+\sqrt5}{2}$,
the damped sequence is summable exactly for $0<r<1/\varphi\approx0.618$. The
**Fibonacci kernel** is

$$K_r(\theta)=2\sum_{n\ge1}F_n r^n\cos(n\theta).$$

| | statement | mechanism |
|---|---|---|
| **F1** Domain | $K_r\in C(\mathbb T)$ and is positive definite $\iff 0<r<1/\varphi$ | radius of convergence $=1/\varphi$ + Bochner |
| **F2** Closed form | $K_r(\theta)=2\,\Re\!\dfrac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}$ | generating function $\sum F_nz^n=\dfrac{z}{1-z-z^2}$ |
| **F3** Spectrum | the convolution operator has eigenvalues $\lambda_n=F_{|n|}r^{|n|}$ on $e^{in\theta}$, decaying like $(\varphi r)^{n}$ | Bochner / Fourier diagonalisation |
| **F4** Mass | $K_r(0)=\dfrac{2r}{1-r-r^2}$, mean $\tfrac1{2\pi}\!\int K_r=\lambda_0=F_0=0$ | generating function at $z=r$ |

---

## 1. Setup and the recipe

Work on the circle $\mathbb T=[-\pi,\pi)$ with $\langle f,g\rangle=\frac1{2\pi}\int_{\mathbb T}f\overline g$.
Following the recipe:

- **Damping.** $w_n=r^n$, $r>0$.
- **Symmetrisation.** $\lambda_0=F_0=0$ and $\lambda_n=\lambda_{-n}=F_nr^n$ for $n\ge1$.
- **Kernel.** $K_r(\theta)=\sum_{n\in\mathbb Z}\lambda_ne^{in\theta}=2\sum_{n\ge1}F_nr^n\cos(n\theta)$.

---

## 2. Domain and positive definiteness

> **Theorem F1 (domain).** $\sum_{n\ge1}F_nr^n<\infty$ **iff** $0<r<1/\varphi$. In
> that range $K_r$ is a continuous, even, real function on $\mathbb T$ and is
> positive definite.

*Proof.* By Binet, $F_n=(\varphi^n-\psi^n)/\sqrt5$ with $\psi=\tfrac{1-\sqrt5}{2}$,
$|\psi|<1$, so $F_n\sim\varphi^n/\sqrt5$ and $\limsup F_n^{1/n}=\varphi$. Hence the
power series $\sum F_nr^n$ has radius of convergence $1/\varphi$ and converges iff
$r<1/\varphi$. For such $r$ the coefficients $\lambda_n=F_{|n|}r^{|n|}\ge0$ are
absolutely summable, so $K_r$ is a uniformly convergent series of continuous even
terms, hence continuous and even. By **Bochner's theorem on the circle**, a
continuous even function whose Fourier coefficients are all $\ge0$ is positive
definite; here $\lambda_n\ge0$. $\;\blacksquare$

> **Corollary (operator).** Convolution $T_rf=K_r*f$ is a bounded, self‑adjoint,
> positive semidefinite operator on $L^2(\mathbb T)$, compact (its eigenvalues
> $\lambda_n\to0$), and trace class ($\sum_n\lambda_n<\infty$).

---

## 3. Closed form

> **Theorem F2 (rational closed form).** For $0<r<1/\varphi$,
> $$K_r(\theta)=2\,\Re\!\left[\frac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}\right].$$

*Proof.* With $z=re^{i\theta}$, $|z|=r<1/\varphi$ lies inside the disc of
convergence of the Fibonacci generating function
$\sum_{n\ge0}F_nz^n=\frac{z}{1-z-z^2}$. Then
$$K_r(\theta)=2\,\Re\sum_{n\ge1}F_nz^n=2\,\Re\frac{z}{1-z-z^2},$$
since $F_0=0$. Substitute $z=re^{i\theta}$. $\;\blacksquare$

---

## 4. Spectrum and mass

> **Theorem F3 (spectrum).** The eigenpairs of $T_r$ are $(\lambda_n,e^{in\theta})$
> with $\lambda_n=F_{|n|}r^{|n|}$. The nonzero eigenvalues are
> $\{F_nr^n:n\ge1\}$, each of multiplicity $2$, decaying like
> $\lambda_n\sim(\varphi r)^n/\sqrt5\to0$.

*Proof.* Convolution by an $L^1$ kernel is diagonalised by the Fourier basis
$e^{in\theta}$ with eigenvalue the $n$‑th Fourier coefficient $\lambda_n$
(Theorem F1). Asymptotics from Binet. $\;\blacksquare$

> **Theorem F4 (total mass).** $K_r(0)=\dfrac{2r}{1-r-r^2}$ and
> $\dfrac1{2\pi}\int_{\mathbb T}K_r=\lambda_0=0$.

*Proof.* $K_r(0)=2\sum_{n\ge1}F_nr^n=2\cdot\frac{r}{1-r-r^2}$ (generating
function at $z=r$, real). The mean equals the zeroth Fourier coefficient
$\lambda_0=F_0=0$. $\;\blacksquare$

---

## 5. Generalisations (same machine)

- **Lucas / general order‑2 recurrence.** Any $a_{n}=ca_{n-1}+da_{n-2}$ has a
  rational generating function $\frac{P(z)}{1-cz-dz^2}$; the same substitution
  $z=re^{i\theta}$ gives a rational closed‑form kernel, with damping threshold
  $r<1/|\lambda_{\max}|$ for the dominant root.
- **Order‑$k$ linear recurrences.** Rational generating function of degree $k$;
  kernel is $2\,\Re[P(z)/Q(z)]$, positive definite below the reciprocal of the
  dominant root's modulus.
- **Transfer‑operator view (open).** The Fibonacci/Lucas pair is a candidate
  smallest example of "transfer between objects": the identity
  $L_n=F_{n-1}+F_{n+1}$ is a linear map on coefficient sequences and hence a
  bounded multiplier between the two kernels. Formalising this multiplier and its
  explicit‑formula analogue is left to Phase 1/4.

---

## 6. Numerical verification (to fill in)

Target checks for a small script (extends [prime-zeros.py](../victor/prime-zeros.py)):

| quantity | formula | check |
|---|---|---|
| $K_r(0)$ | $2r/(1-r-r^2)$ | vs. truncated $2\sum_{n\le N}F_nr^n$ |
| min of $K_r$ | — | should be $\ge0$ on a fine $\theta$‑grid (PD) |
| eigenvalues | $F_nr^n$ | vs. FFT of sampled kernel |
| $\|K_r\|_2^2$ | $2\sum_{n\ge1}F_n^2r^{2n}=\dfrac{r^2(1-r^2)}{(1+r^2)(1-3r^2+r^4)}\cdot\!\big[\text{check}\big]$ | vs. $\sum_n\lambda_n^2$ (Parseval) |

*(Verify the $\sum F_n^2x^n$ closed form numerically before relying on it.)*

---

## 7. Scope and honest limits

- **Proven.** F1–F4 are unconditional. The Fibonacci kernel is a genuine
  positive definite kernel with rational closed form for every $0<r<1/\varphi$.
- **Not claimed.** This case has no bearing on $\zeta$, primes, or RH; it is the
  template that fixes notation and the proof pattern (recipe → Bochner →
  generating function → spectrum) reused for harder objects.
- **Open.** The Fibonacci↔Lucas transfer multiplier and a Fibonacci "explicit
  formula" (a trace identity for $T_r$) are unproven here.
- **Standard results used.** Binet's formula; Cauchy–Hadamard radius of
  convergence; Bochner's theorem on $\mathbb T$; the generating function
  $\sum F_nz^n=z/(1-z-z^2)$.
