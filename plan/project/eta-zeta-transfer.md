# The η ↔ ζ Transfer Operator — A Phase‑2 Worked Case

*Phase‑2 deliverable (see [README](../README.md)). This is the cleanest provable
instance of "transfer between objects": the Dirichlet eta and Riemann zeta series
differ by the explicit multiplier $1-2^{1-s}$, which on the sequence side is an
alternating‑sign twist and on the circle is a rotation by $\pi$. The relation
$\eta(s)=(1-2^{1-s})\zeta(s)$ is unconditional; the RH‑level statements are
flagged as such.*

---

## 0. Summary

The Dirichlet eta function (alternating zeta) is
$$\eta(s)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n^{s}},$$
related to $\zeta$ by the elementary identity

$$\boxed{\ \eta(s)=\bigl(1-2^{1-s}\bigr)\,\zeta(s).\ }$$

| | statement | mechanism |
|---|---|---|
| **E1** Domain | $\eta$ converges (conditionally) for $\Re s>0$; $\zeta$ only for $\Re s>1$ | Dirichlet's test on alternating terms |
| **E2** Multiplier | $\eta=(1-2^{1-s})\zeta$ on $\Re s>1$, then by analytic continuation | split even/odd terms: $\sum_{\text{even}}=2^{-s}\sum n^{-s}$ |
| **E3** Twist | the eta term sequence is the zeta term sequence modulated by $(-1)^{n-1}=e^{i\pi(n-1)}$; on $\mathbb T$ this is a **rotation by $\pi$** of the zeta kernel | $\cos(n(\theta+\pi))=(-1)^n\cos(n\theta)$ |
| **E4** Zeros | $\eta$ shares all nontrivial zeros of $\zeta$, plus extra zeros at $s=1+\dfrac{2\pi ik}{\log2}$, $k\in\mathbb Z$, from $1-2^{1-s}=0$ | product structure of E2 |

---

## 1. The two series as sequences

In the spectral‑triple language ([spectral-triple.html](../victor/spectral-triple.html) §5),
the Dirichlet terms on the line $s=\sigma+ib$ are $a_n^{\zeta}=n^{-\sigma}e^{-ib\log n}$.
The eta terms are the **same sequence with an alternating sign**:
$$a_n^{\eta}=(-1)^{n-1}\,n^{-\sigma}e^{-ib\log n}=(-1)^{n-1}a_n^{\zeta}.$$

---

## 2. The multiplier identity

> **Theorem E2 (multiplier).** For $\Re s>1$,
> $\eta(s)=(1-2^{1-s})\zeta(s)$, and the identity continues analytically to
> $\Re s>0$ (where $\eta$ is given by its own convergent series and provides the
> standard analytic continuation of $\zeta$).

*Proof.* For $\Re s>1$ all series converge absolutely. Split $\zeta$ into odd and
even indices: the even part is
$\sum_{m\ge1}(2m)^{-s}=2^{-s}\zeta(s)$, so
$\zeta(s)=\zeta_{\text{odd}}(s)+2^{-s}\zeta(s)$. Meanwhile
$\eta(s)=\zeta_{\text{odd}}(s)-2^{-s}\zeta(s)=\zeta(s)-2\cdot2^{-s}\zeta(s)=(1-2^{1-s})\zeta(s)$.
Since $\eta$ converges for $\Re s>0$ (Theorem E1) and $1-2^{1-s}$ is entire, the
identity gives the meromorphic continuation of $\zeta$ to $\Re s>0$ with the
single pole at $s=1$ (where $1-2^{1-s}$ has a simple zero cancelling it). $\;\blacksquare$

> **Theorem E1 (domains).** $\sum(-1)^{n-1}n^{-s}$ converges for $\Re s>0$ by
> Dirichlet's test (bounded partial sums of $(-1)^{n-1}$, $n^{-s}\to0$
> monotonically in modulus), conditionally for $0<\Re s\le1$; $\zeta$'s defining
> series needs $\Re s>1$.

*Proof.* Dirichlet's test for the first claim; comparison with the harmonic
series for the second. $\;\blacksquare$

---

## 3. The transfer operator on kernels

The multiplier $1-2^{1-s}$ is the **transfer operator** between the two objects.
Two equivalent descriptions:

> **Theorem E3 (the twist is a rotation by $\pi$).** Building kernels by the recipe
> from the (damped) term sequences, the eta kernel is the zeta kernel evaluated at
> the rotated argument:
> $$K^{\eta}_r(\theta)=2\sum_{n\ge1}(-1)^{n-1}\frac{r^n}{n^{\sigma}}\cos(n\theta)=-\,K^{\zeta}_r(\theta+\pi).$$

*Proof.* $\cos(n(\theta+\pi))=\cos(n\theta)\cos(n\pi)=(-1)^n\cos(n\theta)$, so
$K^{\zeta}_r(\theta+\pi)=2\sum_{n\ge1}\frac{r^n}{n^{\sigma}}(-1)^n\cos(n\theta)=-K^{\eta}_r(\theta)$.
$\;\blacksquare$

So the transfer is the unitary **shift by $\pi$** (with a sign): a rotation of the
circle, the simplest nontrivial transfer operator in the catalogue. Note,
however, that the alternating signs make some Fourier coefficients negative, so
$K^{\eta}_r$ is **not** positive definite in general — a feature worth recording:
the transfer operator does not preserve the positive cone, which is exactly the
phenomenon the RH positivity question concerns.

> **Remark (multiplier description).** Equivalently, on the analytic side the
> transfer is pointwise multiplication of the Dirichlet series by
> $m(s)=1-2^{1-s}$. Its zeros $s=1+2\pi ik/\log2$ are the "extra" eta zeros (E4);
> on the critical line $s=\tfrac12+ib$ the multiplier is
> $m=1-2^{1/2}e^{-ib\log2}=1-\sqrt2\,e^{-ib\log2}$, a curve in $\mathbb C$ that
> never vanishes (since $\sqrt2\ne1$), so $\eta$ and $\zeta$ have the **same**
> zeros on the critical line.

---

## 4. Zeros and the explicit‑formula angle

> **Theorem E4 (zero sets).** $\eta(s)=0$ iff either $\zeta(s)=0$ or
> $1-2^{1-s}=0$, i.e. $s\in\{1+2\pi ik/\log2:k\in\mathbb Z\}$. In particular every
> nontrivial zero of $\zeta$ is a zero of $\eta$, and conversely the nontrivial
> ($0<\Re s<1$) zeros coincide.

*Proof.* From E2, a product is zero iff a factor is; $1-2^{1-s}=0\iff2^{1-s}=1\iff(1-s)\log2\in2\pi i\mathbb Z$,
all of which have $\Re s=1$, outside the critical strip's interior. $\;\blacksquare$

**Explicit‑formula consequence (conditional framing).** Because the nontrivial
zeros coincide, the zero‑side of any explicit formula is unchanged under the
transfer; the prime‑side changes by the Dirichlet coefficients of
$-\log(1-2^{1-s})=\sum_{k\ge1}\frac{2^{k(1-s)}}{k}$, i.e. extra spectral mass at
the points $\log(2^k)=k\log2$. This is the eta analogue of the von Mangoldt
prime‑power terms in [spectral-triple.html](../victor/spectral-triple.html) §7, and gives a
concrete, computable "transfer correction" to the explicit formula. Stating it as
an equality at the level of measures is a Phase‑2/4 task.

---

## 5. Numerical verification (to fill in)

| quantity | check |
|---|---|
| $\eta(s)$ vs. $(1-2^{1-s})\zeta(s)$ | 10‑digit match at several $s$ (e.g. $s=2,\ \tfrac12+14.1347i$) |
| $K^{\eta}_r(\theta)+K^{\zeta}_r(\theta+\pi)$ | $\approx0$ on a $\theta$‑grid (Theorem E3) |
| extra zeros $1+2\pi ik/\log2$ | $|m(s)|\to0$ there; nonzero on $\Re s=\tfrac12$ |
| transfer correction | Dirichlet coeffs of $-\log(1-2^{1-s})$ supported on $\{k\log2\}$ |

---

## 6. Scope and honest limits

- **Proven / unconditional.** E1–E4 and the rotation‑by‑$\pi$ description E3 are
  elementary and complete. The η↔ζ transfer is a genuine, fully worked example of
  a transfer operator between two catalogue objects.
- **Conditional / open.** The measure‑level explicit‑formula equality for the
  transfer correction (§4) is not proved here. Nothing in this note proves or
  bears on RH; it only records that η and ζ share critical‑strip zeros, so the
  hard part is identical for both.
- **Why this case matters.** It isolates the transfer operator as a simple
  unitary (rotation) plus a multiplier, and shows transfer operators need **not**
  preserve positive definiteness — pinpointing where the difficulty lives for the
  zeros↔primes case.
- **Standard results used.** Dirichlet's test; absolute‑convergence
  rearrangement; analytic continuation; elementary properties of $2^{1-s}$.
