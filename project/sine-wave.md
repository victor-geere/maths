# The Natural Sine Wave — the Riemann Zeta Generalisation

*The $\zeta$-analogue of [prime-sine-wave.md](prime-sine-wave.md). Every statement
below is a theorem with a complete proof, or a citation to a standard one
(Riesz–Fischer, the Laurent expansion of $\zeta$, the classical sawtooth series).
Nothing is conditional on the Riemann Hypothesis, and nothing claims to bear on
it; see [§8 Scope](#8-scope-and-honest-limits).*

---

## 0. Summary

In $H=L^2[0,2]$, the harmonics $\{\sin(n\pi x)\}_{n\ge1}$ are orthonormal.
Weighting **every** frequency by $n^{-s}$ (rather than only the prime ones)
defines the *natural sine wave*

$$\Psi_s(x)=\sum_{n\ge1}\frac{\sin(n\pi x)}{n^{s}} .$$

This is the prime sine wave with $\mathbb P$ replaced by all of $\mathbb N$, and
the prime zeta $P$ replaced by the **Riemann zeta** $\zeta$. The framework is five
theorems, all unconditional:

| | statement | mechanism |
|---|---|---|
| **T1** Domain | the series converges in $H$ $\iff \sigma:=\Re s>\tfrac12$ | Riesz–Fischer + Cauchy criterion |
| **T2** Energy | $\lVert\Psi_s\rVert_H^2=\zeta(2\sigma)$, independent of $\Im s$ | Parseval |
| **T3** Kernel | $\langle\Psi_s,\Psi_{s'}\rangle_H=\zeta(s+\overline{s'})$ | orthonormality |
| **T4** Boundary | $\lVert\Psi_s\rVert_H^2=\frac{1}{2\sigma-1}+\gamma+o(1)$ as $\sigma\to\tfrac12^+$ (**simple pole**); on the line the energy diverges at the **harmonic** rate $\log N$ | simple pole of $\zeta$ at $1$ |
| **T5** Closed form | $\Psi_s(x)=\mathrm{Im}\,\mathrm{Li}_s(e^{i\pi x})$; in particular $\Psi_1(x)=\frac{\pi(1-x)}2$ on $(0,2)$ | polylogarithm / classical sawtooth |

The half-plane of definition is again exactly $\Re s>\tfrac12$, and the **critical
line $\Re s=\tfrac12$ is its natural boundary** — but now forced by the *pole* of
$\zeta$, not a logarithmic singularity. Two structural features distinguish this
note from the prime case: the kernel has a **closed form** (T5), and the
fundamental mode $\sin(\pi x)$ is **present** rather than absent (§4 corollary).

---

## 1. The space and its orthonormal harmonics

Let $H=L^2[0,2]$ over $\mathbb C$, with
$\langle f,g\rangle=\int_0^2 f(x)\overline{g(x)}\,dx$ and $\lVert f\rVert^2=\langle f,f\rangle$.
For $n\in\mathbb Z_{\ge1}$ put $\phi_n(x)=\sin(n\pi x)$.

> **Lemma 1 (orthonormality).** $\langle\phi_a,\phi_b\rangle=\delta_{ab}$ for all $a,b\in\mathbb Z_{\ge1}$.

This is exactly Lemma 1 of [prime-sine-wave.md](prime-sine-wave.md#1-the-space-and-its-orthonormal-harmonics)
(product-to-sum, then $\int_0^2\cos(k\pi x)\,dx=0$ for integer $k\ne0$); we reuse
it verbatim and do not repeat the proof. $\;\blacksquare$

> **Remark.** $\{\phi_n\}_{n\ge1}$ is a **complete** orthonormal system for the
> odd subspace $H_-=\{f\in H:\ f(2-x)=-f(x)\ \text{a.e.}\}$ (the sine half of the
> $[0,2]$ Fourier basis). Unlike the prime case — where the coefficients are
> supported on the sparse set $\mathbb P$ — here every coordinate is occupied, so
> $\Psi_s$ ranges over **all** of $H_-$ with $\ell^2$ decay. Completeness is what
> makes the closed form T5 a genuine function-identity.

The **Riemann zeta function** is $\zeta(z)=\sum_{n\ge1}n^{-z}$, absolutely
convergent for $\Re z>1$, with meromorphic continuation to $\mathbb C$ whose only
singularity is a simple pole at $z=1$. Throughout, $\sigma=\Re s$ and $\tau=\Im s$.

---

## 2. The natural sine wave and its domain of definition

> **Definition.** For $s\in\mathbb C$, the *natural sine wave* is the formal series
> $$\Psi_s(x)=\sum_{n\ge1}n^{-s}\,\phi_n(x)=\sum_{n\ge1}\frac{\sin(n\pi x)}{n^{s}}.$$
> We say $\Psi_s$ *exists in $H$* if its partial sums
> $\Psi_s^{(N)}=\sum_{n\le N}n^{-s}\phi_n$ converge in $H$.

> **Theorem 1 (domain).** $\Psi_s$ exists in $H$ **if and only if** $\sigma>\tfrac12$.
> When it exists, the convergence is unconditional.

*Proof.* The coefficients are $c_n=n^{-s}$, so $|c_n|^2=n^{-2\sigma}$ and
$$\sum_{n\ge1}|c_n|^2=\sum_{n\ge1}n^{-2\sigma}=\zeta(2\sigma),$$
finite $\iff 2\sigma>1\iff\sigma>\tfrac12$.

($\Leftarrow$) If $\sigma>\tfrac12$ then $(c_n)\in\ell^2$. By the **Riesz–Fischer
theorem** applied to the orthonormal system $\{\phi_n\}$ (Lemma 1), the series
$\sum_n c_n\phi_n$ converges in $H$, unconditionally, to an element of $H$.

($\Rightarrow$) If $\sigma\le\tfrac12$ then $\sum_n|c_n|^2=\infty$. For $N<M$,
orthonormality gives $\big\lVert\Psi_s^{(M)}-\Psi_s^{(N)}\big\rVert^2=\sum_{N<n\le M}|c_n|^2$,
whose tails do **not** tend to $0$. Hence $(\Psi_s^{(N)})$ is not Cauchy in $H$ and
does not converge. $\;\blacksquare$

The abscissa $\sigma=\tfrac12$ is identical to the prime case — for the same
$\ell^2$ reason — even though the relevant Dirichlet series ($\zeta$ vs. $P$)
differ.

---

## 3. Energy: the Riemann zeta function

> **Theorem 2 (Parseval / zeta energy).** For $\sigma>\tfrac12$,
> $$\boxed{\ \lVert\Psi_s\rVert_H^2=\sum_{n\ge1}n^{-2\sigma}=\zeta(2\sigma)\ }$$
> In particular the energy depends only on $\sigma=\Re s$, not on $\tau=\Im s$:
> the imaginary part only rotates the phases $n^{-i\tau}$, which have modulus $1$.

*Proof.* Immediate from the Parseval identity of Riesz–Fischer for the orthonormal
system $\{\phi_n\}$: $\lVert\sum_n c_n\phi_n\rVert^2=\sum_n|c_n|^2$, with
$|c_n|^2=|n^{-\sigma-i\tau}|^2=n^{-2\sigma}$. $\;\blacksquare$

---

## 4. The reproducing kernel is the Riemann zeta function

> **Theorem 3 (inner products).** For $\sigma,\sigma'>\tfrac12$,
> $$\langle\Psi_s,\Psi_{s'}\rangle_H=\sum_{n\ge1}n^{-s}\,\overline{n^{-s'}}
>   =\sum_{n\ge1}n^{-(s+\overline{s'})}=\zeta\!\big(s+\overline{s'}\big).$$
> The series on the right converges absolutely, since
> $\Re(s+\overline{s'})=\sigma+\sigma'>1$.

*Proof.* For $\ell^2$ coefficient sequences over an orthonormal system,
$\langle\sum_n a_n\phi_n,\sum_n b_n\phi_n\rangle=\sum_n a_n\overline{b_n}$
(continuity of the inner product plus Lemma 1). Take $a_n=n^{-s}$, $b_n=n^{-s'}$;
then $a_n\overline{b_n}=n^{-(s+\overline{s'})}$. Absolute convergence holds because
$\sigma+\sigma'>1$. $\;\blacksquare$

> **Corollary (Gram matrix).** The Gram matrix of any finite set
> $\{\Psi_{s_1},\dots,\Psi_{s_m}\}$ is $\big[\zeta(s_j+\overline{s_k})\big]_{j,k}$,
> a positive semidefinite matrix built entirely from values of $\zeta$ in the
> half-plane $\Re>1$. Setting $s'=s$ recovers Theorem 2.

> **Corollary (the fundamental mode is present).** For every $s$ with $\sigma>\tfrac12$,
> $$\langle\Psi_s,\ \sin(\pi x)\rangle_H=\sum_{n}n^{-s}\langle\phi_n,\phi_1\rangle=1^{-s}=1.$$
> This is the exact **reverse** of the prime case, where the same inner product is
> $0$ because $1\notin\mathbb P$. The natural sine wave always contains the
> fundamental $\sin(\pi x)$ with unit coefficient.

---

## 5. The critical line as the natural boundary

The energy $\zeta(2\sigma)$ is finite for $\sigma>\tfrac12$ and the map
$s\mapsto\Psi_s$ is a curve in $H$ defined exactly on the open half-plane
$\Re s>\tfrac12$. We quantify its behaviour as $s$ approaches the critical line.

> **Theorem 4 (boundary blow-up).**
> 1. As $\sigma\to\tfrac12^{+}$, with $\gamma=0.5772156649\ldots$ the Euler–Mascheroni constant,
> $$\lVert\Psi_s\rVert_H^2=\zeta(2\sigma)=\frac{1}{2\sigma-1}+\gamma+o(1)\ \longrightarrow\ +\infty.$$
> 2. On the critical line $s=\tfrac12+i\tau$ itself ($\Psi_s\notin H$ by Theorem 1),
> the truncated energy diverges at the **harmonic rate**:
> $$\big\lVert\Psi_{\frac12+i\tau}^{(N)}\big\rVert_H^2=\sum_{n\le N}\frac1n=\log N+\gamma+o(1).$$

*Proof.* (1) The Laurent expansion of $\zeta$ at its simple pole $z=1$ is
$$\zeta(z)=\frac{1}{z-1}+\gamma+O(z-1)\qquad(z\to1),$$
where the constant term is exactly $\gamma$ (the Stieltjes constant $\gamma_0$).
Put $z=2\sigma$, so $z-1=2\sigma-1\to0^+$; this gives the stated expansion, and the
pole forces $\zeta(2\sigma)\to+\infty$. (2) is the classical harmonic-sum estimate
$\sum_{n\le N}1/n=\log N+\gamma+o(1)$ (Euler–Maclaurin); the truncated energy is
$\sum_{n\le N}|n^{-1/2-i\tau}|^2=\sum_{n\le N}n^{-1}$, independent of $\tau$. $\;\blacksquare$

> **Why $\tfrac12$ and not some other line.** By Theorem 2 the energy
> $\sigma\mapsto\zeta(2\sigma)$ inherits the singularities of $\zeta$. The function
> $\zeta$ is meromorphic on all of $\mathbb C$ with a *single* singularity — the
> simple pole at $z=1$, i.e. at $2\sigma=1$. So the critical line $\sigma=\tfrac12$
> is the unique abscissa where the natural sine wave leaves $H$. Contrast the prime
> case, where $P$ has a *logarithmic* singularity at $1$ and a genuine natural
> boundary at $\Re z=0$: there the blow-up is the gentler $\log\frac1{2\sigma-1}$ and
> the line rate is Mertens' $\log\log N$. Here both are stronger — a pole and the
> harmonic $\log N$ — reflecting that $\mathbb N$ is denser than $\mathbb P$.

---

## 6. Closed form: the polylogarithm

The prime sine wave has **no** closed form (its coefficients are supported on
$\mathbb P$). The natural sine wave does, because summing over all of $\mathbb N$
is exactly the imaginary part of a polylogarithm on the unit circle.

> **Theorem 5 (closed form).** For $\sigma>1$ and all $x\in\mathbb R$,
> $$\Psi_s(x)=\mathrm{Im}\,\mathrm{Li}_s\!\big(e^{i\pi x}\big),\qquad
> \mathrm{Li}_s(z)=\sum_{n\ge1}\frac{z^n}{n^s}.$$
> The identity extends to $\tfrac12<\sigma\le1$ for $x\notin2\mathbb Z$, where the
> sine series converges conditionally (Dirichlet test) to the boundary value of
> $\mathrm{Li}_s$. In particular, at $s=1$,
> $$\Psi_1(x)=\mathrm{Im}\big[-\log(1-e^{i\pi x})\big]=\frac{\pi(1-x)}{2}\qquad(0<x<2).$$

*Proof.* For $\sigma>1$ the series $\sum_n e^{in\pi x}n^{-s}$ converges absolutely
and uniformly in $x$ (dominated by $\sum n^{-\sigma}<\infty$), so it equals
$\mathrm{Li}_s(e^{i\pi x})$; taking imaginary parts and using
$\mathrm{Im}\,e^{in\pi x}=\sin(n\pi x)$ gives $\Psi_s(x)=\mathrm{Im}\,\mathrm{Li}_s(e^{i\pi x})$.
For $\tfrac12<\sigma\le1$ and $e^{i\pi x}\ne1$, the partial sums of $e^{in\pi x}$
are bounded, so $\sum_n\sin(n\pi x)/n^s$ converges by the Dirichlet test to the
Abel/radial boundary value of the (continuous) function $\mathrm{Li}_s$, which is
its value there. For $s=1$, $\mathrm{Li}_1(z)=-\log(1-z)$; writing
$1-e^{i\theta}=-2i\sin(\tfrac\theta2)e^{i\theta/2}$ gives
$\mathrm{Im}[-\log(1-e^{i\theta})]=\tfrac{\pi-\theta}{2}$ for $0<\theta<2\pi$, i.e.
$\Psi_1(x)=\tfrac{\pi(1-x)}2$ for $0<x<2$ (the classical sawtooth Fourier series). $\;\blacksquare$

> **Remark.** $\mathrm{Im}\,\mathrm{Li}_s(e^{i\theta})$ is the **Clausen-type
> function** (for $s=2$, the Clausen function $\mathrm{Cl}_2$). So the natural sine
> wave *is* a Clausen function of $\pi x$ — a fully explicit element of $H$ for each
> $s$ with $\sigma>\tfrac12$. This is the row "$n^{-s}$" of the spectral data sheet;
> note it uses **Dirichlet** damping $n^{-s}$, distinct from the **geometric**
> damping $r^n$ of the "$\,2\Re\,\mathrm{Li}_{1/2}(re^{i\theta})$" magnitude row.

---

## 7. Numerical verification

Computed by [`victor/sine-wave-verify.py`](../victor/sine-wave-verify.py)
(NumPy grid integrals at truncation $N=2000$, $2\times10^5$ grid points; `mpmath`
at 40 dps for special values). All checks pass.

| quantity | computed | reference |
|---|---|---|
| $\int_0^2\Psi_2(x)^2\,dx$ | $1.082323233670$ | $\zeta(4)=\pi^4/90=1.0823232337$ (10-digit match) |
| $\langle\Psi_2,\Psi_3\rangle$ | $1.036927755143$ | $\zeta(5)=1.0369277551$ |
| $\langle\Psi_2,\sin\pi x\rangle$ | $1.000000000000$ | $1$ (Corollary, §4) |
| $\zeta(2\sigma)-\frac1{2\sigma-1}$ at $\sigma=0.5001$ | $0.5772302$ | $\to\gamma=0.5772156649$ (T4.1) |
| $\sum_{n\le10^6}\frac1n-\log10^6$ | $0.5772162$ | $\to\gamma$ (T4.2, harmonic rate) |
| $\Psi_2(0.25)$ | $0.9818721480$ | $\mathrm{Im}\,\mathrm{Li}_2(e^{i\pi/4})=0.9818721511$ (T5) |
| $\Psi_1(0.25)$ | $1.1780972451$ | $\tfrac{3\pi}{8}=1.1780972451$ (T5 sawtooth) |

Worst discrepancies: energy/kernel $\sim10^{-11}$, fundamental mode exact,
closed form $\sim10^{-9}$ (truncation of the conditionally convergent $s=2$ sum at
$N=2\times10^4$). The boundary constant converges to $\gamma$ as expected
($1.5\times10^{-5}$ at $\sigma=0.5001$; it is a limit, not an exact identity).

---

## 8. Scope and honest limits

- **What is proved.** T1–T5 and all lemmas/corollaries are unconditional theorems.
  $\Psi_s$ is a genuine $L^2$ function on $\Re s>\tfrac12$ — explicitly the Clausen
  function $\mathrm{Im}\,\mathrm{Li}_s(e^{i\pi x})$ — with energy $\zeta(2\sigma)$,
  inner products $\zeta(s+\overline{s'})$, and a forced singular boundary exactly on
  the critical line.
- **What is *not* claimed.** This framework does **not** prove, assume, or reduce
  the Riemann Hypothesis. The boundary at $\Re s=\tfrac12$ comes from the **simple
  pole** of $\zeta$ at $z=1$ (an unconditional fact), **not** from the nontrivial
  zeros. Indeed the energy curve $z=2\sigma$ lives in $\Re z>1$, to the *right* of
  the pole, while every nontrivial zero lies in the strip $0<\Re z<1$ — i.e. at
  $0<\sigma<\tfrac12$, strictly *inside* the forbidden region $\Re s\le\tfrac12$
  where $\Psi_s\notin H$. The zeros are never reached. The coincidence of the
  abscissa $\tfrac12$ with the conjectured zero line is exactly that — a
  coincidence of $\ell^2$ bookkeeping, not a criterion.
- **Why this case is the sharper warning.** Because the *full* Riemann zeta now
  appears (T2, T3), the temptation to read RH into the picture is stronger than in
  the prime case. The honest content is the opposite: $\zeta$ appears only through
  its values in $\Re>1$ and its pole at $1$; its zeros are provably out of reach of
  this construction.
- **Relation to the prime note.** Replacing $\mathbb N\to\mathbb P$ and
  $\zeta\to P$ recovers [prime-sine-wave.md](prime-sine-wave.md) verbatim, losing
  the closed form (T5) and flipping the fundamental-mode corollary from $1$ to $0$.

---

### Standard results used

- **Riesz–Fischer theorem** (convergence of $\sum c_n\phi_n$ and Parseval for an
  orthonormal system with $(c_n)\in\ell^2$).
- **Laurent expansion of $\zeta$** at $z=1$: $\zeta(z)=\frac1{z-1}+\gamma+O(z-1)$,
  with $\gamma$ the Euler–Mascheroni constant; meromorphic on $\mathbb C$ with this
  as the only pole.
- **Harmonic sum** $\sum_{n\le N}1/n=\log N+\gamma+o(1)$ (Euler–Maclaurin).
- **Polylogarithm / Clausen function** $\mathrm{Li}_s(z)=\sum_n z^n/n^s$, with
  $\mathrm{Li}_1(z)=-\log(1-z)$ and the classical sawtooth
  $\sum_n\sin(n\theta)/n=(\pi-\theta)/2$ on $(0,2\pi)$.
