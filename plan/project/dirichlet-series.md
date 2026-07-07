# Dirichlet $L$-functions — The Character Sine Wave and the Kernel ↔ Functional-Equation Dictionary

*Phase 2c deliverable. The Hilbert-space core (T1–T3) is **proven and
unconditional**: it generalises the prime/natural sine wave verbatim to a
Dirichlet character $\chi$. The character-theoretic structure — energy as a
principal-character $L$-value, the reproducing kernel as $L(s,\chi_1\bar\chi_2)$,
and the **Gauss-sum transfer operator** that writes the character twist as a
finite superposition of circle rotations — is the precise generalisation of the
$\eta\leftrightarrow\zeta$ case ([eta-zeta-transfer.md](eta-zeta-transfer.md),
which is the degenerate $q=2$ instance). The functional equation and explicit
formula are stated with standard citations; their **dictionary entries** (parity
$\leftrightarrow$ cosine/sine kernel and $\Gamma$-factor; root number
$\leftrightarrow$ transfer normalisation) are made precise. Nothing here proves,
assumes, or bears on RH; see [§7 Scope](#7-scope-and-honest-limits).*

---

## 0. Summary

Fix a Dirichlet character $\chi$ modulo $q$. In $H=L^2[0,2]$ the harmonics
$\phi_n(x)=\sin(n\pi x)$ are orthonormal (Lemma 1 of
[prime-sine-wave.md](prime-sine-wave.md)). Weighting frequency $n$ by
$\chi(n)\,n^{-s}$ defines the **character sine wave**

$$\Psi^{\chi}_s(x)=\sum_{n\ge1}\chi(n)\,n^{-s}\,\sin(n\pi x).$$

Write $\sigma=\Re s$, $\chi_0$ for the principal character mod $q$,
$\tau(\chi)=\sum_{n\bmod q}\chi(n)e^{2\pi in/q}$ for the Gauss sum, and
$a=\tfrac12(1-\chi(-1))\in\{0,1\}$ for the parity index.

| | statement | mechanism | status |
|---|---|---|---|
| **D1** Domain | $\Psi^{\chi}_s$ exists in $H$ $\iff\sigma>\tfrac12$ | $\sum_n|\chi(n)|^2n^{-2\sigma}=L(2\sigma,\chi_0)<\infty$ | **proven** |
| **D2** Energy | $\lVert\Psi^{\chi}_s\rVert^2=L(2\sigma,\chi_0)=\zeta(2\sigma)\!\prod_{p\mid q}(1-p^{-2\sigma})$ | Parseval; $\lvert\chi(n)\rvert^2=\mathbf 1_{(n,q)=1}$ | **proven** |
| **D3** Kernel | $\langle\Psi^{\chi_1}_s,\Psi^{\chi_2}_{s'}\rangle=L\!\big(s+\overline{s'},\,\chi_1\bar\chi_2\big)$ | orthonormality; $\chi_1\bar\chi_2$ is a character | **proven** |
| **D4** Parity | $\chi$ even $\Rightarrow$ cosine kernel $\&$ $\Gamma(\tfrac s2)$; $\chi$ odd $\Rightarrow$ sine kernel $\&$ $\Gamma(\tfrac{s+1}2)$ | $\chi(-1)=(-1)^a$ | **proven** (kernel side); FE **cited** |
| **D5** Transfer | $\Psi^{\chi}_s=\dfrac{1}{\tau(\bar\chi)}\displaystyle\sum_{a=1}^{q-1}\bar\chi(a)\,R_{2\pi a/q}\,\Psi^{\mathrm{add}}_s$ — a Gauss-sum-weighted sum of $\phi(q)$ rotations | finite-Fourier separability of $\chi$ | **proven** |

The reproducing kernel of the **family** $\{\Psi^{\chi}_s:\chi\bmod q\}$ is the
Dirichlet $L$-function itself (D3): the Gram matrix is built from values
$L(s+\overline{s'},\psi)$, one for each character $\psi=\chi_1\bar\chi_2$. The
half-plane of definition is exactly $\Re s>\tfrac12$; the critical line is the
natural boundary, for the **same** prime-zeta reason as in the unweighted case
and with **no** bearing on RH.

---

## 1. Setup: characters and $L(s,\chi)$ as a Dirichlet series

Let $q\ge1$ and let $\chi:(\mathbb Z/q\mathbb Z)^\times\to\mathbb C^\times$ be a
Dirichlet character, extended by $\chi(n)=0$ for $(n,q)>1$. It is **completely
multiplicative**, $q$-periodic, and $|\chi(n)|=\mathbf 1_{(n,q)=1}$. The
principal character $\chi_0$ has $\chi_0(n)=\mathbf 1_{(n,q)=1}$. The associated
$L$-function is
$$L(s,\chi)=\sum_{n\ge1}\chi(n)\,n^{-s}=\prod_{p\nmid q}\big(1-\chi(p)p^{-s}\big)^{-1}\qquad(\Re s>1),$$
with $L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s})$. For $\chi\ne\chi_0$ the
series converges (conditionally) for $\Re s>0$ and $L(s,\chi)$ is entire.

We work in $H=L^2[0,2]$ with $\langle f,g\rangle=\int_0^2 f\bar g$ and the
orthonormal system $\phi_n(x)=\sin(n\pi x)$, $n\ge1$ (orthonormality is Lemma 1
of [prime-sine-wave.md](prime-sine-wave.md); completeness is not used).

---

## 2. Kernel construction and positive definiteness

> **Theorem D1 (domain).** $\Psi^{\chi}_s$ exists in $H$ **iff** $\sigma>\tfrac12$,
> with unconditional (order-independent) convergence.

*Proof.* The coefficients are $c_n=\chi(n)n^{-s}$, so
$|c_n|^2=|\chi(n)|^2n^{-2\sigma}=\mathbf 1_{(n,q)=1}\,n^{-2\sigma}$ and
$$\sum_{n}|c_n|^2=\sum_{(n,q)=1}n^{-2\sigma}=L(2\sigma,\chi_0),$$
finite $\iff 2\sigma>1$. The two directions are Riesz–Fischer ($\Leftarrow$) and
the Cauchy criterion against orthonormality ($\Rightarrow$), exactly as in
Theorem 1 of [prime-sine-wave.md](prime-sine-wave.md). $\;\blacksquare$

> **Theorem D2 (energy).** For $\sigma>\tfrac12$,
> $$\boxed{\ \lVert\Psi^{\chi}_s\rVert_H^2=\sum_{(n,q)=1}n^{-2\sigma}=L(2\sigma,\chi_0)=\zeta(2\sigma)\!\prod_{p\mid q}\!\big(1-p^{-2\sigma}\big).\ }$$
> The energy depends only on $\sigma$ (and on the **support** of $\chi$, i.e. on
> $q$ through its prime divisors), **not** on $\Im s$ nor on which character of
> modulus $q$ is chosen.

*Proof.* Parseval for $\{\phi_n\}$ gives
$\lVert\Psi^{\chi}_s\rVert^2=\sum_n|c_n|^2$; then $|\chi(n)|^2=\mathbf 1_{(n,q)=1}$
and the Euler factorisation of $L(\,\cdot\,,\chi_0)$ over $p\mid q$. $\;\blacksquare$

**Positive definiteness.** On the circle the catalogue recipe forms the kernel
$K^{\chi}_r(\theta)=\sum_{n\in\mathbb Z}\lambda_n e^{in\theta}$ from the damped
symmetrised coefficients $\lambda_n=\chi(n)r^{|n|}$ (geometric damping $r<1$ in
place of $n^{-s}$). By Bochner, $K^{\chi}_r$ is **positive definite iff all
$\lambda_n\ge0$**. This holds for $\chi=\chi_0$ (then $\lambda_n=r^{|n|}\ge0$ and
$K^{\chi_0}_r$ is the Poisson kernel restricted to $(n,q)=1$), and **fails** for
every non-principal $\chi$, whose values include roots of unity off the positive
axis. This is the same break of positivity recorded for $\eta$
([eta-zeta-transfer.md](eta-zeta-transfer.md) §3): the character twist moves mass
off the positive cone, which is precisely where the RH positivity question lives.

---

## 3. The reproducing kernel is the $L$-function

> **Theorem D3 (inner products).** For $\sigma,\sigma'>\tfrac12$ and characters
> $\chi_1,\chi_2$ of modulus $q$,
> $$\langle\Psi^{\chi_1}_s,\Psi^{\chi_2}_{s'}\rangle_H
>   =\sum_{n\ge1}\chi_1(n)\overline{\chi_2(n)}\,n^{-(s+\overline{s'})}
>   =L\!\big(s+\overline{s'},\,\chi_1\bar\chi_2\big),$$
> the series converging absolutely since $\Re(s+\overline{s'})=\sigma+\sigma'>1$.

*Proof.* For $\ell^2$ coefficient sequences over the orthonormal $\{\phi_n\}$,
$\langle\sum a_n\phi_n,\sum b_n\phi_n\rangle=\sum a_n\overline{b_n}$. Take
$a_n=\chi_1(n)n^{-s}$, $b_n=\chi_2(n)n^{-s'}$; then
$a_n\overline{b_n}=\chi_1(n)\overline{\chi_2(n)}\,n^{-(s+\overline{s'})}$. Finally
$\chi_1\bar\chi_2$ is again a Dirichlet character mod $q$, so the sum is its
$L$-series, absolutely convergent because $\sigma+\sigma'>1$. $\;\blacksquare$

> **Corollary (the family's Gram matrix is $L$-valued).** For any finite set of
> parameters $\{(s_j,\chi_j)\}$ the Gram matrix
> $\big[L(s_j+\overline{s_k},\chi_j\bar\chi_k)\big]_{j,k}$ is positive
> semidefinite, and is assembled **entirely from values of Dirichlet
> $L$-functions** — one $L$-function per coset $\chi_j\bar\chi_k$ of characters.
> Setting $\chi_1=\chi_2$, $s'=s$ recovers D2 (then $\chi_1\bar\chi_2=\chi_0$).

This is the central dictionary fact: **the catalogue's "kernel = dual object"
slot is occupied, for this family, by the $L$-function**, with the dual character
read off as the product $\chi_1\bar\chi_2$. Two characters whose product is
$\chi_0$ pair into the principal energy; orthogonal characters pair into a
genuinely non-principal $L$-value.

---

## 4. The functional equation as kernel symmetry

Throughout this section $\chi$ is **primitive** mod $q$ (the conductor case). The
completed $L$-function is, with parity index $a=\tfrac12(1-\chi(-1))\in\{0,1\}$,
$$\Lambda(s,\chi)=\Big(\tfrac{q}{\pi}\Big)^{(s+a)/2}\Gamma\!\Big(\tfrac{s+a}{2}\Big)L(s,\chi),$$
and the **functional equation** (standard; Davenport, *Multiplicative Number
Theory*, Ch. 9, or Iwaniec–Kowalski §3.8) is
$$\boxed{\ \Lambda(s,\chi)=\varepsilon(\chi)\,\Lambda(1-s,\bar\chi),\qquad
\varepsilon(\chi)=\frac{\tau(\chi)}{i^{a}\sqrt q},\quad |\varepsilon(\chi)|=1,\ }$$
since $|\tau(\chi)|=\sqrt q$ for primitive $\chi$. Two pieces of this translate
into exact statements about the kernel; a third does not, and we say so.

> **Theorem D4 (parity $\leftrightarrow$ cosine/sine kernel and $\Gamma$-factor).**
> The harmonics carry the parity of $\chi$:
> - $\chi$ **even** ($\chi(-1)=1$, $a=0$): the symmetric extension
>   $\lambda_n=\lambda_{-n}=\chi(n)r^{|n|}$ gives a real **cosine** kernel
>   $K^{\chi}_r(\theta)=\sum_{n}\chi(n)r^{|n|}\cos n\theta$, matching the
>   archimedean factor $\Gamma(s/2)$.
> - $\chi$ **odd** ($\chi(-1)=-1$, $a=1$): the antisymmetric extension
>   $\lambda_{-n}=-\lambda_n$ gives a **sine** kernel
>   $K^{\chi}_r(\theta)=\sum_{n}\chi(n)r^{|n|}\sin n\theta$, matching
>   $\Gamma\big((s+1)/2\big)$.
>
> Equivalently: the sine-wave harmonics $\sin(n\pi x)$ are odd about $x=1$, so the
> natural pairing of $\Psi^{\chi}_s$ with the reflection $x\mapsto2-x$ reproduces
> $\chi(-1)$, which is exactly the sign $(-1)^a$ selecting the $\Gamma$-shift.

*Proof (kernel side).* $\chi(-n)=\chi(-1)\chi(n)=(-1)^a\chi(n)$; substituting into
$\sum_{n\in\mathbb Z}\lambda_n e^{in\theta}$ collapses the $\pm n$ pair to
$2\cos n\theta$ when $a=0$ and to $2i\sin n\theta$ when $a=1$. The identification
of $a$ with the $\Gamma$-shift is the definition of $\Lambda$ above. $\;\blacksquare$

> **Theorem D5 (Gauss-sum transfer operator).** Let $\Psi^{(\alpha)}_s$ denote the
> additive (Hurwitz/Lerch) sine wave
> $\Psi^{(\alpha)}_s(x)=\sum_{n\ge1}e^{2\pi in\alpha}n^{-s}\sin(n\pi x)$, which for
> every $\alpha\in\mathbb R$ lies in $H$ for $\sigma>\tfrac12$ with energy
> $\zeta(2\sigma)$. For primitive $\chi$ mod $q$ the **separability identity**
> $$\chi(n)=\frac{1}{\tau(\bar\chi)}\sum_{a=1}^{q-1}\bar\chi(a)\,e^{2\pi ian/q}$$
> holds for all $n$, hence
> $$\boxed{\ \Psi^{\chi}_s=\frac{1}{\tau(\bar\chi)}\sum_{a=1}^{q-1}\bar\chi(a)\,R_{2\pi a/q}\,\Psi^{(0)}_s,\ }\qquad
> (R_{\beta}\,\Psi)\ :\ \text{multiply harmonic }n\text{ by }e^{in\beta}.$$
> The transfer operator $M_\chi=\tau(\bar\chi)^{-1}\sum_a\bar\chi(a)R_{2\pi a/q}$
> is a **finite superposition of $\phi(q)$ unitary circle rotations**, weighted by
> the conjugate character and normalised by the Gauss sum. As a Fourier multiplier
> it acts by $n\mapsto\chi(n)$, so $\lVert M_\chi\rVert=1$ (a contraction).

*Proof.* The separability identity is the finite Fourier expansion of $\chi$,
valid for primitive $\chi$ (Davenport Ch. 9; it is equivalent to
$\tau(\chi)\bar\chi(n)=\sum_{a}\chi(a)e^{2\pi ian/q}$). Applying $R_{2\pi a/q}$ to
$\Psi^{(0)}_s=\sum_n n^{-s}\phi_n$ multiplies harmonic $n$ by $e^{2\pi ian/q}$;
the weighted sum multiplies harmonic $n$ by $\chi(n)$, giving $\Psi^{\chi}_s$. The
multiplier symbol is $(\chi(n))_n$ with $\sup_n|\chi(n)|=1$. $\;\blacksquare$

> **The dictionary, made precise.** Of the three ingredients of the functional
> equation:
> 1. the **archimedean factor** $\Gamma((s+a)/2)$ is the parity of the kernel
>    (D4) — the cosine/sine dichotomy, i.e. the $L^2(\gamma)$ Gamma factor of the
>    OU object ([ou-process.md](ou-process.md)) shifted by $a$;
> 2. the **root number** $\varepsilon(\chi)=\tau(\chi)/i^a\sqrt q$ is exactly the
>    normalising constant of the transfer operator $M_\chi$ (D5): the Gauss sum
>    that converts $\chi$ into a sum of rotations is the same Gauss sum that
>    appears in $\varepsilon(\chi)$;
> 3. the **reflection $s\leftrightarrow1-s$ with $\chi\leftrightarrow\bar\chi$**
>    is **not** visible inside $H$: the sine wave lives only on $\sigma>\tfrac12$
>    (D1), whereas the reflection is a statement of analytic continuation across
>    the critical line. We record this as the honest boundary of the construction
>    (§7), not as a theorem.

**The $\eta\leftrightarrow\zeta$ case is $q=2$.** Modulus $2$ has only the
principal character, and the alternating sign $(-1)^{n-1}$ is the **additive**
character $\alpha=\tfrac12$: $e^{2\pi in/2}=(-1)^n$, so $R_{2\pi\cdot1/2}=R_\pi$ is
the rotation by $\pi$ of [eta-zeta-transfer.md](eta-zeta-transfer.md) E3. The
Gauss-sum transfer D5 is thus the genuine generalisation of that single rotation
to a weighted sum of $\phi(q)$ rotations.

---

## 5. Explicit formula

The Weil explicit formula for $L(s,\chi)$ (primitive, mod $q$) is standard; we
state it and identify the archimedean correction, flagging it as a citation
rather than a re-proof (Iwaniec–Kowalski, *Analytic Number Theory*, Thm 5.12).

> **Explicit formula (cited).** Let $\rho=\tfrac12+i\gamma$ run over the
> non-trivial zeros of $L(s,\chi)$, and let $g$ be a suitable even test function
> with transform $h(t)=\int g(u)e^{itu}\,du$. Then
> $$\sum_{\rho}h(\gamma)=\frac{\log(q/\pi)}{2\pi}\!\int_{\mathbb R}\!h(t)\,dt
>  +\frac{1}{2\pi}\!\int_{\mathbb R}\!h(t)\,\Re\,\psi\!\Big(\tfrac{a}{2}+\tfrac14+\tfrac{it}{2}\Big)dt
>  -\sum_{n\ge1}\frac{\Lambda(n)\big(\chi(n)+\bar\chi(n)\big)}{\sqrt n}\,g(\log n),$$
> where $\psi=\Gamma'/\Gamma$ is the digamma function and
> $a=\tfrac12(1-\chi(-1))$.

The **archimedean ($\Gamma$) correction** is the digamma term: it is the digamma
of $(s+a)/2$ on the critical line, i.e. the logarithmic derivative of the **same
parity-shifted $\Gamma$-factor** that D4 reads off the cosine/sine kernel. The
**prime side** carries the character twist $\chi(n)+\bar\chi(n)=2\Re\chi(n)$ on
the von Mangoldt weights — the catalogue's "transfer correction," supported on
prime powers and modulated by the character. For $\chi=\chi_0$ this reduces to the
zeta explicit formula minus the finitely many primes $p\mid q$; the difference
$L(s,\chi_0)$ vs. $\zeta(s)$ is the finite Euler product $\prod_{p\mid q}(1-p^{-s})$,
giving extra spectral mass at $\{k\log p:p\mid q\}$ — the exact analogue of the
$\eta$ mass at $\{k\log2\}$.

---

## 6. Numerical verification

Computed with `mpmath` at 30 digits (`victor/dirichlet-lf-verify.py`), modulus
$q=4$: $\chi_4$ is the unique primitive character mod $4$ (odd, $a=1$), with
$L(s,\chi_4)=\beta(s)$ the Dirichlet beta function; $\chi_{0}$ is the principal
character mod $4$.

| quantity | computed | reference |
|---|---|---|
| $\lVert\Psi^{\chi_4}_{2}\rVert^2$ (D2) | $1.0146780316$ | $(1-2^{-4})\zeta(4)=1.0146780316$ (10-digit) |
| $\langle\Psi^{\chi_4}_{2},\Psi^{\chi_{0}}_{2}\rangle$ (D3) | $0.9889445517$ | $L(4,\chi_4)=\beta(4)=0.9889445517$ (10-digit) |
| Gauss sum $\tau(\chi_4)$ | $2.0\,i$ | $|\tau|=\sqrt4=2$ |
| separability max error, $n\le12$ (D5) | $3.3\times10^{-32}$ | $\chi_4(n)$ exactly |
| root number $\varepsilon(\chi_4)=\tau/(i^{1}\sqrt4)$ | $1.0$ | $|\varepsilon|=1$ |
| $\Psi^{\chi_4}_{2}(0.25)$ | $0.6168502751$ | — (spot value) |

The cross-character pairing D3 is the sharpest check: $\chi_4\cdot\bar\chi_{0}=\chi_4$
on odd $n$, so the inner product of an **odd** with a **principal** character
sine wave returns the genuinely non-principal value $\beta(4)$, confirming that
the reproducing kernel of the family is the $L$-function with character read off
as the product.

---

## 7. Scope and honest limits

- **Proven / unconditional.** D1–D3 are theorems: $\Psi^{\chi}_s$ is a genuine
  $L^2[0,2]$ function exactly on $\Re s>\tfrac12$, with energy $L(2\sigma,\chi_0)$,
  and the family's reproducing kernel is $L(s+\overline{s'},\chi_1\bar\chi_2)$.
  D4 (parity $\to$ cosine/sine kernel) and D5 (Gauss-sum transfer operator) are
  proven on the kernel/operator side; they are the precise generalisation of the
  $q=2$ case [eta-zeta-transfer.md](eta-zeta-transfer.md).
- **Cited (standard).** The functional equation of §4 and the explicit formula of
  §5 are quoted from Davenport and Iwaniec–Kowalski, not re-derived. Their
  **dictionary entries** — archimedean factor $\leftrightarrow$ kernel parity,
  root number $\leftrightarrow$ transfer normalisation — are proven
  correspondences.
- **Not claimed.** The reflection $s\leftrightarrow1-s$ is **not** an internal
  feature of the Hilbert space: $\Psi^{\chi}_s$ leaves $H$ at $\Re s=\tfrac12$
  (D1), and the critical line is a natural boundary forced by the
  $L(2\sigma,\chi_0)$ singularity at $2\sigma=1$, **not** by the zeros of
  $L(s,\chi)$. As in [prime-sine-wave.md](prime-sine-wave.md) §7, this is a
  coincidence of abscissa, not a zero criterion; nothing here proves, assumes, or
  bears on the (Generalised) Riemann Hypothesis.
- **Open / next.** (i) Numerically verify D5 on a $\theta$-grid for a complex
  character (e.g. order-$4$ character mod $5$) and tabulate the rotation sum.
  (ii) Promote the §5 "transfer correction" at $\{k\log p:p\mid q\}$ to a
  measure-level equality, jointly with the Phase 2a $\eta$ task
  ([eta-zeta-transfer.md](eta-zeta-transfer.md) §4). (iii) Imprimitive $\chi$:
  reduce to the primitive inducing character and track the removed Euler factors.

---

### Standard results used

- **Riesz–Fischer** (convergence and Parseval for $\sum c_n\phi_n$, $(c_n)\in\ell^2$).
- **Dirichlet characters**: complete multiplicativity, $|\chi|=\mathbf 1_{(n,q)=1}$,
  finite-Fourier separability $\tau(\chi)\bar\chi(n)=\sum_a\chi(a)e^{2\pi ian/q}$,
  $|\tau(\chi)|=\sqrt q$ for primitive $\chi$ (Davenport, Ch. 9).
- **Functional equation** of $L(s,\chi)$ with root number $\tau(\chi)/i^a\sqrt q$
  (Davenport Ch. 9; Iwaniec–Kowalski §3.8).
- **Weil explicit formula** for $L(s,\chi)$ (Iwaniec–Kowalski, Thm 5.12).
