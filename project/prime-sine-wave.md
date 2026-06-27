# The Prime Sine Wave — A Rigorous Hilbert-Space Framework

*Every statement below is a theorem with a complete proof, or a citation to a
standard one (Riesz–Fischer, Mertens, the prime zeta function). Nothing is
conditional on the Riemann Hypothesis, and nothing claims to bear on it; see
[§7 Scope](#7-scope-and-honest-limits).*

---

## 0. Summary

In $H=L^2[0,2]$, the harmonics $\{\sin(n\pi x)\}_{n\ge1}$ are orthonormal. Weighting
the **prime** frequencies by $p^{-s}$ defines the *prime sine wave*

$$\Psi_s(x)=\sum_{p\in\mathbb P}\frac{\sin(p\pi x)}{p^{s}} .$$

The framework consists of four theorems, all unconditional:

| | statement | mechanism |
|---|---|---|
| **T1** Domain | the series converges in $H$ $\iff \sigma:=\Re s>\tfrac12$ | Riesz–Fischer + Cauchy criterion |
| **T2** Energy | $\lVert\Psi_s\rVert_H^2=P(2\sigma)$ (prime zeta), independent of $\Im s$ | Parseval |
| **T3** Kernel | $\langle\Psi_s,\Psi_{s'}\rangle_H=P(s+\overline{s'})$ | orthonormality |
| **T4** Boundary | $\lVert\Psi_s\rVert_H^2\sim\log\frac{1}{2\sigma-1}$ as $\sigma\to\tfrac12^+$; on the line the energy diverges at the Mertens rate $\log\log N$ | singularity of $P$ at $1$ |

The half-plane of definition is exactly $\Re s>\tfrac12$; the **critical line
$\Re s=\tfrac12$ is its natural boundary.**

---

## 1. The space and its orthonormal harmonics

Let $H=L^2[0,2]$ over $\mathbb C$, with
$\langle f,g\rangle=\int_0^2 f(x)\overline{g(x)}\,dx$ and $\lVert f\rVert^2=\langle f,f\rangle$.
For $n\in\mathbb Z_{\ge1}$ put $\phi_n(x)=\sin(n\pi x)$.

> **Lemma 1 (orthonormality).** $\langle\phi_a,\phi_b\rangle=\delta_{ab}$ for all $a,b\in\mathbb Z_{\ge1}$.

*Proof.* With $a,b$ real integers $\sin$ is real, so
$$\int_0^2\sin(a\pi x)\sin(b\pi x)\,dx=\tfrac12\int_0^2\big[\cos((a-b)\pi x)-\cos((a+b)\pi x)\big]dx.$$
For an integer $k\ne0$, $\int_0^2\cos(k\pi x)\,dx=\big[\tfrac{\sin(k\pi x)}{k\pi}\big]_0^2=\tfrac{\sin(2k\pi)}{k\pi}=0$.
If $a\ne b$ both $k=a-b$ and $k=a+b$ are nonzero integers, giving $0$. If $a=b$ the
first integrand is $\cos 0=1$ with $\int_0^2 1\,dx=2$, and the second term vanishes;
the prefactor $\tfrac12$ gives $1$. $\;\blacksquare$

> **Remark.** $\{\phi_n\}_{n\ge1}$ is orthonormal but **not** a basis of $H$: the
> complete sine basis of $[0,2]$ is $\sin(n\pi x/2)$. The $\phi_n=\sin(n\pi x)$ are a
> complete orthonormal system for the closed subspace
> $H_-=\{f\in H:\ f(2-x)=-f(x)\ \text{a.e.}\}$. Completeness is **not used** below;
> orthonormality (Lemma 1) is all the framework needs.

The **prime zeta function** is $P(z)=\sum_{p\in\mathbb P}p^{-z}$, absolutely
convergent for $\Re z>1$. Throughout, $\sigma=\Re s$ and $\tau=\Im s$.

---

## 2. The prime sine wave and its domain of definition

> **Definition.** For $s\in\mathbb C$, the *prime sine wave* is the formal series
> $$\Psi_s(x)=\sum_{p\in\mathbb P}p^{-s}\,\phi_p(x)=\sum_{p\in\mathbb P}\frac{\sin(p\pi x)}{p^{s}},$$
> indexed over the primes. We say $\Psi_s$ *exists in $H$* if its partial sums
> $\Psi_s^{(N)}=\sum_{p\le N}p^{-s}\phi_p$ converge in $H$.

> **Theorem 1 (domain).** $\Psi_s$ exists in $H$ **if and only if** $\sigma>\tfrac12$.
> When it exists, the convergence is unconditional (independent of the ordering of
> the primes).

*Proof.* The coefficients are $c_p=p^{-s}$, so $|c_p|^2=p^{-2\sigma}$ and
$$\sum_{p}|c_p|^2=\sum_p p^{-2\sigma}=P(2\sigma),$$
which is finite $\iff 2\sigma>1\iff\sigma>\tfrac12$.

($\Leftarrow$) If $\sigma>\tfrac12$ then $(c_p)\in\ell^2$. By the **Riesz–Fischer
theorem** applied to the orthonormal system $\{\phi_p\}$ (Lemma 1), the series
$\sum_p c_p\phi_p$ converges in $H$, unconditionally, to an element of $H$.

($\Rightarrow$) If $\sigma\le\tfrac12$ then $\sum_p|c_p|^2=\infty$. For $N<M$,
orthonormality gives
$$\big\lVert\Psi_s^{(M)}-\Psi_s^{(N)}\big\rVert^2=\sum_{N<p\le M}|c_p|^2,$$
whose tails do **not** tend to $0$ (the full sum diverges). Hence $(\Psi_s^{(N)})$ is
not Cauchy in $H$ and does not converge. $\;\blacksquare$

---

## 3. Energy: the prime zeta function

> **Theorem 2 (Parseval / prime-zeta energy).** For $\sigma>\tfrac12$,
> $$\boxed{\ \lVert\Psi_s\rVert_H^2=\sum_{p\in\mathbb P}p^{-2\sigma}=P(2\sigma)\ }$$
> In particular the energy depends only on $\sigma=\Re s$, not on $\tau=\Im s$:
> the imaginary part of $s$ only rotates the phases $p^{-i\tau}$, which have modulus $1$.

*Proof.* Immediate from the Parseval identity of Riesz–Fischer for the orthonormal
system $\{\phi_p\}$: $\lVert\sum_p c_p\phi_p\rVert^2=\sum_p|c_p|^2$, with
$|c_p|^2=|p^{-\sigma-i\tau}|^2=p^{-2\sigma}$. $\;\blacksquare$

---

## 4. The reproducing kernel is the prime zeta function

> **Theorem 3 (inner products).** For $\sigma,\sigma'>\tfrac12$,
> $$\langle\Psi_s,\Psi_{s'}\rangle_H=\sum_{p\in\mathbb P}p^{-s}\,\overline{p^{-s'}}
>   =\sum_{p\in\mathbb P}p^{-(s+\overline{s'})}=P\!\big(s+\overline{s'}\big).$$
> The series on the right converges absolutely, since
> $\Re(s+\overline{s'})=\sigma+\sigma'>1$.

*Proof.* For $\ell^2$ coefficient sequences $(a_p),(b_p)$ over an orthonormal system,
$\langle\sum_p a_p\phi_p,\sum_p b_p\phi_p\rangle=\sum_p a_p\overline{b_p}$ (continuity
of the inner product plus Lemma 1). Take $a_p=p^{-s}$, $b_p=p^{-s'}$; then
$a_p\overline{b_p}=p^{-s}\,\overline{p^{-s'}}=p^{-(s+\overline{s'})}$. Absolute
convergence holds because $\sigma+\sigma'>1$. $\;\blacksquare$

> **Corollary.** The Gram matrix of any finite set $\{\Psi_{s_1},\dots,\Psi_{s_m}\}$
> is $\big[P(s_j+\overline{s_k})\big]_{j,k}$, a positive semidefinite matrix built
> entirely from values of the prime zeta function. Setting $s'=s$ recovers Theorem 2.

> **Corollary (orthogonality to the fundamental).** For every $s$ with $\sigma>\tfrac12$,
> $$\langle\Psi_s,\ \sin(\pi x)\rangle_H=\sum_{p}p^{-s}\langle\phi_p,\phi_1\rangle=\sum_p p^{-s}\delta_{p,1}=0,$$
> because $1\notin\mathbb P$. Thus $\Psi_s$ lies in the orthogonal complement of the
> fundamental mode: **the prime sine wave never reproduces $\sin(\pi x)$.**

---

## 5. The critical line as the natural boundary

The energy $P(2\sigma)$ is finite for $\sigma>\tfrac12$ and the map $s\mapsto\Psi_s$
is a curve in $H$ defined exactly on the open half-plane $\Re s>\tfrac12$. We quantify
its behaviour as $s$ approaches the critical line.

> **Theorem 4 (boundary blow-up).**
> 1. As $\sigma\to\tfrac12^{+}$, with $C_0=\sum_{k\ge2}\frac{\mu(k)}{k}\log\zeta(k)$,
> $$\lVert\Psi_s\rVert_H^2=P(2\sigma)=\log\frac{1}{2\sigma-1}+C_0+o(1)\ \longrightarrow\ +\infty.$$
> 2. On the critical line $s=\tfrac12+i\tau$ itself ($\Psi_s\notin H$ by Theorem 1),
> the truncated energy diverges at the **Mertens rate**:
> $$\big\lVert\Psi_{\frac12+i\tau}^{(N)}\big\rVert_H^2=\sum_{p\le N}\frac1p=\log\log N+M+o(1),\qquad M=0.26149\ldots$$

*Proof.* (1) The standard identity (valid for $\Re z>1$, by Möbius inversion of the
Euler product)
$$P(z)=\sum_{k\ge1}\frac{\mu(k)}{k}\log\zeta(kz)$$
splits as $P(z)=\log\zeta(z)+\sum_{k\ge2}\frac{\mu(k)}{k}\log\zeta(kz)$. As $z\to1^+$,
$\zeta(z)=\frac{1}{z-1}+O(1)$ gives $\log\zeta(z)=-\log(z-1)+o(1)$, while the tail
$\sum_{k\ge2}\frac{\mu(k)}{k}\log\zeta(kz)\to C_0$ (each $\log\zeta(kz)$ is analytic at
$z=1$ for $k\ge2$, and the sum converges absolutely since $\log\zeta(kz)=O(2^{-kz})$).
Put $z=2\sigma$, so $z-1=2\sigma-1\to0^+$. (2) is Mertens' second theorem; the
truncated energy is $\sum_{p\le N}|p^{-1/2-i\tau}|^2=\sum_{p\le N}p^{-1}$, independent
of $\tau$. $\;\blacksquare$

> **Why $\tfrac12$ and not some other line.** By the $P$-formula of Theorem 4, the
> energy $\sigma\mapsto P(2\sigma)$ inherits the singularities of the prime zeta
> function. The one nearest from the right is the logarithmic singularity of $P(z)$ at
> $z=1$ — i.e. at $2\sigma=1$. So the critical line $\sigma=\tfrac12$ is *forced* as
> the abscissa where the prime sine wave leaves $H$. (Further in, $P(z)$ has a natural
> boundary at $\Re z=0$, i.e. $\sigma=0$, with singularities dense at $z=1/k$.)

---

## 6. Numerical verification

At $s=2$ (so $\sigma=2$, energy $P(4)$), computed with primes $p\le 2000$ and checked
against $P(4)=\sum_p p^{-4}$:

| quantity | computed | reference |
|---|---|---|
| $\int_0^2\Psi_2(x)^2\,dx$ | $0.0769931398$ | $P(4)=0.0769931398$ (10-digit match) |
| $\langle\Psi_2,\sin\pi x\rangle$ | $0.0\times10^{0}$ | $0$ (Corollary, §4) |
| $\Psi_2(0.25)$ | $0.2888923342$ | — |
| $C_0=\sum_{k\ge2}\frac{\mu(k)}{k}\log\zeta(k)$ | $-0.3157\ldots$ | constant in Theorem 4(1) |

These confirm Theorem 2 (Parseval), the orthogonality corollary, and the boundary
constant.

---

## 7. Scope and honest limits

- **What is proved.** T1–T4 and all lemmas/corollaries are unconditional theorems.
  The object $\Psi_s$ is a genuine $L^2$ function on $\Re s>\tfrac12$, with energy
  $P(2\sigma)$, inner products $P(s+\overline{s'})$, and a forced singular boundary
  exactly on the critical line.
- **What is *not* claimed.** This framework does **not** prove, assume, or reduce the
  Riemann Hypothesis. The boundary at $\Re s=\tfrac12$ comes from the singularity of
  the *prime zeta function* at $1$ (an unconditional fact), **not** from the zeros of
  $\zeta$. It is a clean coincidence of abscissa, not a criterion. In particular,
  nothing here distinguishes the truth or falsity of RH.
- **Relation to earlier notes.** $\Psi_s$ is purely additive and, by the
  orthogonality corollary, cannot represent the fundamental $\sin(\pi x)$; this is why
  the additive "harmonic ansatz" route fails and the genuine prime expansion is
  multiplicative. The present note keeps only what
  survives rigorously.
- **Open (and external to this note).** A rigorous *RH-equivalent* framework is a
  different object — e.g. the Nyman–Beurling–Báez-Duarte criterion in $L^2(0,1)$,
  where RH $\iff$ the constant function lies in the closed span of the dilations
  $\{1/(nx)\}$. That criterion, unlike this note, is provably tied to the zeros of
  $\zeta$.

---

### Standard results used

- **Riesz–Fischer theorem** (convergence of $\sum c_n\phi_n$ and Parseval for an
  orthonormal system with $(c_n)\in\ell^2$).
- **Mertens' second theorem**, $\sum_{p\le N}1/p=\log\log N+M+o(1)$.
- **Prime zeta function** $P(z)=\sum_{k\ge1}\frac{\mu(k)}{k}\log\zeta(kz)$, analytic
  for $\Re z>1$, logarithmic singularity at $z=1$, natural boundary at $\Re z=0$.
