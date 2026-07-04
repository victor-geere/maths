# Phase 1 — The composite-generator sieve and equidistribution

*Implements §2 of [prime-sieve-adele-plan.html](prime-sieve-adele-plan.html).*
*Status: **proven** (imported from the rigorous core); numerics reproduced here.*

Back to [index.md](index.md) · Next: [phase2.md](phase2.md).

## 1.1 Objects

For $n\ge 1$ let $I_n = [2^n,\,2^{n+1}-1]$, $M_n = 2^{n+1}-1$, and $\mathcal P_n$ the primes
$< 2^n$.

**Definition 1.1 (dyadic composite generator).**
$$
G_n = \{\, x\in I_n : x = p_1p_2\cdots p_k,\ p_i\in\mathcal P_n,\ k\ge 2 \,\}.
$$

**Lemma 1.2 — proven.** $G_n$ is exactly the set of composites in $I_n$; equivalently the
primes in $I_n$ are the gaps $I_n\setminus G_n$.

*Proof.* If $x\in I_n$ is composite it has a factor $d$ with $1<d\le\sqrt{x}<2^{(n+1)/2}\le 2^n$,
so $d$ has a prime factor $p<2^n$, i.e. $p\in\mathcal P_n$; dividing out primes $<2^n$ repeatedly
expresses $x$ as a product of members of $\mathcal P_n$ with $k\ge 2$ factors. Conversely any such
product is composite. $\blacksquare$

This is the sieve's defining property: **primes are detected as the numbers the composite
generator misses.** No primality test is used beyond the recursive knowledge of $\mathcal P_n$.

## 1.2 Equidistribution (the one quantitative input the whole program leans on)

Let $k_n=\pi(M_n)$ and form the normalised empirical prime measure on $\mathbb T=[0,1)$,
$$
\mu_n = \frac1{k_n}\sum_{p\le M_n}\delta_{\{p/M_n\}}.
$$

**Theorem 1.3 (equidistribution rate) — proven.** For each fixed $k\ne 0$,
$$
\widehat\mu_n(k) = \frac1{k_n}\sum_{p\le M_n} e^{2\pi i k p/M_n} = O_k\!\Big(\frac1{\log M_n}\Big).
$$

*Proof sketch.* Summation by parts against $\pi(t)$ with the PNT error term
$\pi(t)=\mathrm{li}(t)+O(t e^{-c\sqrt{\log t}})$; the smooth $\mathrm{li}$ part integrates to
$O(1/\log M_n)$ after division by $k_n\sim M_n/\log M_n$, and the error term is smaller. Full
proof: [prime-sieve.html](../barry-keating/prime-sieve.html) Theorem 3.1; the design consequence
(C2) is discussed in [prime-side.md](prime-side.md) §1.

**Why it matters.** Equidistribution says the *positions* of primes on the circle carry only
Lebesgue density in the limit — all arithmetic information has migrated into the *multiplicative*
data $\{\log p\}$ and the von Mangoldt weights. This is exactly why later phases must build the
operator from $\log p$ and $\Lambda$, not from prime positions, and why any *normalised* prime
sum collapses (constraint C1 of [prime-side.md](prime-side.md)).

## 1.3 Numerical check (reproduced)

From `python adele/sieve_operator.py` (`phase1_report`). The last column
$|\widehat\mu_n(1)|\cdot\log M_n$ should hover around a constant if the rate is exactly
$1/\log M_n$:

```
  n       M_n  k_n=pi(M_n)    |mu(1)|    |mu(2)|    |mu(3)| |mu(1)|*logM_n
  8       511           97    0.09758    0.05782    0.04455         0.6085
 10      2047          309    0.07185    0.04895    0.04906         0.5478
 12      8191         1028    0.06106    0.04097    0.03659         0.5502
 14     32767         3512    0.05262    0.03604    0.02975         0.5471
 16    131071        12251    0.04603    0.03056    0.02394         0.5424
 18    524287        43390    0.04054    0.02652    0.01982         0.5339
 20   2097151       155611    0.03591    0.02316    0.01736         0.5227
```

The product column stays in $[0.52, 0.61]$ across $2^8$–$2^{21}$ while
$|\widehat\mu_n(1)|$ itself falls by $2.7\times$ — a clean confirmation of the
$\Theta(1/\log M_n)$ rate. (The slow drift downward is the secondary $1/(\log M_n)^2$ term.)

## 1.4 Task status

| Task | Status |
|---|---|
| Lemma 1.2 (sieve correctness) | **proven** (§1.1) |
| Theorem 1.3 (equidistribution rate) | **proven** (imported); numerics ✓ (§1.3) |
| Fourier decay implemented + checked to $n=20$ | ✓ `prime_measure_fourier` |

Phase 1 has no open mathematical problems. It is the one fully solid pillar; everything
downstream is measured against it.
