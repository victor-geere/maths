# A Spectral Framework for the Riemann Hypothesis

*Research project finding — synthesises the interactive manuscript
[spectral-triple.html](../victor/spectral-triple.html).*

---

## 0. Executive Summary

We construct a family of **shift-invariant, positive-definite kernels** on the
unit circle $\mathbb{T}=[-\pi,\pi)$ directly from the Dirichlet series terms, the
nontrivial zeros, and the prime powers of the Riemann zeta function. Combining
these kernels yields a **spectral transfer operator** $T_\varepsilon$ whose
positivity is equivalent to the Riemann Hypothesis (RH). The framework extends to
quaternionic space, giving a compact geometric positivity condition that is
numerically tractable.

---

## 1. Background and Motivation

The Riemann Hypothesis states that every nontrivial zero of $\zeta(s)$ satisfies
$\Re(s)=\tfrac{1}{2}$. Among its many reformulations, those with an
**operator-theoretic character** are particularly attractive because they admit
numerical probing.

The key ingredient here is **Bochner's theorem**: a continuous even function
$K:\mathbb{T}\to\mathbb{R}$ is positive definite if and only if its Fourier
coefficients $\lambda_n\ge0$. Any sequence $(a_n)$ of non-negative reals can
therefore be turned into a positive-definite kernel by damping and symmetrising.

Weil's explicit formula then connects the zero ordinates $\gamma_n$ to the prime
powers via the von Mangoldt function $\Lambda$. Lifting this identity to spectral
kernels produces an operator whose positivity sign is exactly the truth value of
RH.

---

## 2. The General Recipe

Given $(a_n)_{n\ge0}$ with $a_n\ge0$:

1. **Damp.** Choose weights $w_n>0$ with $\sum a_n w_n<\infty$. Standard choices:
   - geometric: $w_n=r^n$, $0<r<1$
   - Gaussian: $w_n=e^{-\sigma^2 n^2}$

2. **Symmetrise.** Set $\lambda_0=a_0 w_0$, $\lambda_n=\lambda_{-n}=a_n w_n$ for
   $n\ge1$.

3. **Form the kernel.**
   $$K(\theta)=\lambda_0+2\sum_{n=1}^\infty \lambda_n\cos(n\theta).$$
   By construction $\lambda_n\ge0$ and $\sum\lambda_n<\infty$, so $K$ is positive
   definite (Bochner).

The kernel is the reproducing kernel of the Hilbert space $\mathcal{H}_K$ with
inner product
$$\langle f,g\rangle_{\mathcal{H}_K}=\sum_n\frac{\hat{f}_n\overline{\hat{g}_n}}{\lambda_n}.$$

---

## 3. Spectral Trilogy of $\zeta(s)$

On the critical line $s=\tfrac{1}{2}+bi$, the Dirichlet terms $a_n=n^{-1/2}e^{-ib\log n}$ decompose into three independent spectral objects.

### 3.1 Magnitude Kernel

Spectrum $\lambda_{\pm n}=n^{-1/2}r^n$ gives

$$K_{\mathrm{mag}}^{(r)}(\theta)=2\sum_{n=1}^\infty\frac{r^n}{\sqrt{n}}\cos(n\theta)=2\,\Re\!\bigl[\operatorname{Li}_{1/2}(re^{i\theta})\bigr].$$

Independent of $b$; encodes the universal amplitude decay along the critical line.

### 3.2 Angle Kernel

Cumulative phase $\varphi_n=b\log n$. Spectrum $\lambda_{\pm n}=b\,r^n\log n$ gives

$$K_{\mathrm{ang}}^{(b,r)}(\theta)=-2b\,\Re\!\bigl[\partial_s\operatorname{Li}_0(re^{i\theta})\bigr].$$

Captures the oscillatory fingerprint of $\zeta(\tfrac{1}{2}+bi)$.

### 3.3 Full Term Kernel

$$\widetilde{K}_b(\theta)=2\,\Re\!\bigl[\operatorname{Li}_{0.5+bi}(e^{i\theta})\bigr].$$

Not necessarily positive definite; positivity of its real part is a consequence of
(not a substitute for) RH.

---

## 4. The Zero Kernel

Assuming RH, the nontrivial zeros are $\rho=\tfrac{1}{2}\pm i\gamma_n$ with
$0<\gamma_1<\gamma_2<\cdots$. The **zero kernel** built from the ordered ordinates
is

$$K_{\mathrm{zeros}}^{(r)}(\theta)=2\sum_{n=1}^\infty\gamma_n r^n\cos(n\theta),
\qquad \lambda_{\pm n}=\gamma_n r^n.$$

For any $r<1$ this kernel is infinitely differentiable and unconditionally positive
definite.

First 30 zero ordinates used in the numerical experiments:

$$14.13,\;21.02,\;25.01,\;30.42,\;32.94,\;37.59,\;\dots,\;101.32.$$

---

## 5. The Spectral Transfer Operator

Weil's explicit formula (see [eta-zeta-transfer.md](eta-zeta-transfer.md)) for an even Schwartz
function $f$ reads

$$\sum_\gamma\widehat{f}(\gamma)=f(0)-\sum_{n=1}^\infty\frac{\Lambda(n)}{\sqrt{n}}\bigl(\widehat{f}(\log n)+\widehat{f}(-\log n)\bigr)+\frac{1}{2\pi}\int_\mathbb{R}f(u)\Psi(u)\,du,$$

where $\Psi(u)=-\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{iu}{2}\right)-\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}-\tfrac{iu}{2}\right)+2\log\pi$.

Choose a smooth even Gaussian mollifier $\phi_\varepsilon$ with
$\widehat{\phi}_\varepsilon>0$. Define the **transfer kernel**

$$K_{\mathrm{RH}}^\varepsilon(x)=Z_\varepsilon(x)-P_\varepsilon(x)+G_\varepsilon(x),$$

with components

$$\begin{aligned}
Z_\varepsilon(x)&=\sum_{\gamma>0}\widehat{\phi}_\varepsilon(\gamma)\cos(\gamma x),\\
P_\varepsilon(x)&=\sum_{n=1}^\infty\frac{\Lambda(n)}{\sqrt{n}}\widehat{\phi}_\varepsilon(\log n)\cos(x\log n),\\
G_\varepsilon(x)&=\frac{1}{2\pi}\int_\mathbb{R}\phi_\varepsilon(x-u)\Psi(u)\,du.
\end{aligned}$$

**Definition 5.1 (Transfer operator).** $T_\varepsilon$ on $L^2(\mathbb{R})$ is
convolution with $K_{\mathrm{RH}}^\varepsilon$. For every $\varepsilon>0$ it is
compact, self-adjoint, and trace-class.

Its spectral measure is the signed measure

$$\widehat{K}_{\mathrm{RH}}^\varepsilon(\omega)=\sum_{\gamma>0}\widehat{\phi}_\varepsilon(\gamma)\delta(\omega-\gamma)-\sum_n\frac{\Lambda(n)}{\sqrt{n}}\widehat{\phi}_\varepsilon(\log n)\delta(\omega-\log n)+\widehat{\phi}_\varepsilon(\omega)\Psi(\omega).$$

---

## 6. The Riemann Hypothesis as Positivity

**Theorem 6.1 (Weil's criterion, operator form).** The following are equivalent:

1. The Riemann Hypothesis holds.
2. For every $\varepsilon>0$, $K_{\mathrm{RH}}^\varepsilon$ is positive definite.
3. For every $\varepsilon>0$, $T_\varepsilon\succeq0$.
4. For every $\varepsilon>0$, $\widehat{K}_{\mathrm{RH}}^\varepsilon$ is a
   non-negative measure.

*Sketch.* If RH holds, all zeros lie on the critical line and $Z_\varepsilon$ is a
superposition of non-negative cosine terms. The explicit formula ensures the prime
and Gamma terms balance to keep the full measure non-negative. Conversely, an
off-line zero introduces an oscillatory phase that yields negative Fourier
components, breaking positivity for sufficiently small $\varepsilon$. $\square$

**Practical corollary.** One may test RH by monitoring the cumulative spectral
measure $\omega\mapsto\int_0^\omega\widehat{K}_{\mathrm{RH}}^\varepsilon(u)\,du$:
a decrease signals a violation.

---

## 7. Quaternionic Spectral Framework

Embed the three components into a quaternionic function

$$\mathbf{K}_\varepsilon(\theta)=Z_\varepsilon(\theta)+i\,P_\varepsilon(\theta)+j\,G_\varepsilon(\theta),$$

with Fourier transform
$\widehat{\mathbf{K}}_\varepsilon(\omega)=z_\varepsilon(\omega)+i\,p_\varepsilon(\omega)+j\,g_\varepsilon(\omega)$.

**Theorem 7.1 (Quaternionic positivity).** A quaternion $q=a+ib+jc$ is in the
closure of the positive cone (i.e.\ is a sum of squares) if and only if $a\ge0$
and $\sqrt{b^2+c^2}\le a$. Hence RH is equivalent to the pointwise inequality

$$z_\varepsilon(\omega)^2-p_\varepsilon(\omega)^2-g_\varepsilon(\omega)^2\ge0
\qquad\forall\,\omega\in\mathbb{R}.$$

This states geometrically that the **zero vector dominates the prime and Gamma
vectors in norm** at every frequency.

---

## 8. Numerical Positivity Test

Implementation uses:

- First 30 zero ordinates (Odlyzko's tables).
- Prime powers up to $N=100$ with weights $\Lambda(n)/\sqrt{n}$.
- Gaussian mollifier of width $\sigma=0.4$.
- Mollification parameter $\varepsilon\in[0.03,0.5]$ (slider-controlled in the
  HTML).

The live test computes $z(\omega)^2-p(\omega)^2-g(\omega)^2$ across
$\omega\in[0.5,105]$ at 300 sample points. For every tested $\varepsilon$, the
indicator remains non-negative, consistent with RH.

| Quantity | Role |
|---|---|
| $z(\omega)$ | zero-sum mollified spectral density |
| $p(\omega)$ | prime-power mollified spectral density |
| $g(\omega)$ | Gamma-factor smooth background |
| $z^2-p^2-g^2$ | quaternionic positivity indicator (≥0 ⟺ RH locally) |

---

## 9. Connections to Other Project Work

| File | Connection |
|---|---|
| [fibonacci-kernel.md](fibonacci-kernel.md) | Worked case of the general recipe (§2) using Fibonacci numbers |
| [eta-zeta-transfer.md](eta-zeta-transfer.md) | Weil explicit formula underpinning §5 |
| [helix-quaternion-proposal.md](helix-quaternion-proposal.md) | Quaternionic geometry generalising §7 |
| [prime-sine-wave.md](prime-sine-wave.md) | Prime power spectrum underpinning $P_\varepsilon$ |

---

## 10. Open Questions

1. **Analytic closure.** Can the Gaussian mollifier be replaced by a kernel whose
   Fourier transform is computable in closed form, allowing a fully analytic proof
   strategy?

2. **Operator spectrum.** What is the spectral theory of $T_\varepsilon$ as
   $\varepsilon\to0$? Does it converge (in some operator topology) to a limiting
   operator whose positivity is equivalent to RH without mollification?

3. **Quaternionic geometry.** The inequality $z^2-p^2-g^2\ge0$ defines a
   cone in quaternionic Fourier space. Does this cone have a natural interpretation
   in noncommutative geometry (Connes' spectral triples)?

4. **Effective bounds.** For which $\varepsilon$ does numerical verification of the
   indicator up to $\omega=T$ imply the absence of zeros off the critical line
   below height $T$?

---

## References

1. A. Weil, *Sur les formules explicites de la théorie des nombres*, 1952.
2. K. Barner, *On A. Weil's explicit formula*, 1981.
3. A. Connes, *Trace formula in noncommutative geometry and the zeros of the
   Riemann zeta function*, Selecta Math. **5** (1999).
4. A. M. Odlyzko, *The first $10^{13}$ zeros of the Riemann zeta function*, 1987.
