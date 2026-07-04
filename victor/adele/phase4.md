# Phase 4 — Spectral convergence, the trace formula, and unfolding

*Implements §5–6 and §8 of [prime-sieve-adele-plan.html](prime-sieve-adele-plan.html).*
*Status: **corrected**. Conjecture 5.1 (eigenvalues $\to$ zeros) is refuted (§4.3, and Thm 3.3 —
**proven**); it is restated non-vacuously as the **trace-convergence** statement (Thm 4.1/4.2 —
**proven**), realised adelically in [phase6.md](phase6.md).*

Back: [phase3.md](phase3.md) · Index: [index.md](index.md) · Next: [phase5.md](phase5.md).

## 4.1 The plan's conjecture, stated precisely

**Conjecture 5.1 (as written).** For $H_n$ of Definition 4.1 with $\varepsilon_n=c/\log M_n$, the
rescaled eigenvalue-counting measure converges weakly to the distribution $d\Xi$ of the imaginary
parts of the zeros:
$$
\lim_{n\to\infty}\frac1{N_n}\sum_{\lambda\in\mathrm{Spec}(H_n)} f\!\Big(\frac{\lambda-\mu_n}{\sigma_n}\Big)
= \int_\mathbb{R} f(t)\,d\Xi(t),\qquad f\in C_c^\infty.
$$

Two separate objections, one logical and one empirical.

## 4.2 Logical objection: weak convergence $\ne$ Hilbert–Pólya

Even if Conjecture 5.1 held, it states convergence of the *empirical spectral distribution*
(a normalised counting measure) to a limiting density. That is a statement about **statistics**
of the spectrum, not about individual eigenvalues. It would say "$H_n$ has roughly the right
density of levels," in the spirit of GUE universality — it would **not** exhibit a self-adjoint
operator whose spectrum *equals* $\{\gamma_\rho\}$. The plan's leap from Conjecture 5.1 to
"thereby proving the Hilbert–Pólya conjecture" (plan §5) is therefore a non-sequitur: matching a
density is necessary, nowhere near sufficient. This is exactly the overclaim the repository
[rigour convention](../../CLAUDE.md) forbids ("Never assert a framework implies RH unless it is
provably tied to the zeros").

## 4.3 Empirical objection: the numbers don't converge

Because $A\equiv 0$ (Phase 3, Prop 3.1), $\mathrm{Spec}(H_n)=\{\log p-\overline{\log p}\}$, and
we can test the conjecture's affine rescaling directly. From `phase4_report`
([sieve_operator.py](sieve_operator.py)), $n=14$, $N=1612$:

```
n=14, M_n=32767, N=1612, std(diag spectrum)=0.19760
     C      eps_n    std(Spec)  mean|shift|
   0.0    0.00000      0.19760     0.000000
   1.0    0.09618      0.19760     0.000000
   5.0    0.48090      0.19760     0.000000
  10.0    0.96180      0.19760     0.000000

  best affine fit gamma ~ 2913.5811 * lambda + 1160.1696
  RMS residual over 1612 eigenvalues: 14.6879  (zeros span 14.13..2102.54)
  first 6 zeros:      [14.135 21.022 25.011 30.425 32.935 37.586]
  first 6 fitted:     [50.148 51.213 51.923 52.987 54.051 56.532]
```

The best-fit affine image of the spectrum onto the first 1612 zeros has RMS residual $14.7$ —
of the same size as the first zero. The first six "fitted" values sit near $50$–$56$ while the
first six zeros are $14$–$38$. There is no convergence to unfold. This is the concrete face of
Theorem 3.3: $\{\log p\}$ (density $\sim e^T/T$) and $\{\gamma_\rho\}$ (density $\sim T\log T$)
are the wrong shape for each other, and no affine map fixes it.

## 4.4 The statement that *is* true and *is* constructive

The explicit formula pairs the two spectra through a **Fourier transform**, not a bijection. The
right target for a sieve construction is the **prime side of the Guinand–Weil formula realised as
an operator trace**, which [prime-side.md](prime-side.md) establishes unconditionally:

**Theorem 4.1 (prime-side trace identity) — proven.** With $\mathbb A = A\oplus(-A)$,
$\sigma(A)=\{k\log p\}$, and weight $\mathbb W = w(\mathbb A)$, $w(k\log p)=(\log p)p^{-k/2}$,
$$
\mathrm{Tr}\big(\mathbb W^{1/2} g(\mathbb A)\,\mathbb W^{1/2}\big)
= \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\big(g(\log n)+g(-\log n)\big)
=: \mathcal W_{\mathrm{ar}}(g),
$$
and, plugged into Guinand–Weil (Fact 4.1 there), $\mathrm{Tr}$ *is* the prime side of the exact
identity linking zeros and primes. (prime-side.md Thm 3.4, Cor 4.2 — **proven**;
numerically balanced to $2\times10^{-31}$ in its §7E.)

**Theorem 4.2 (sieve produces the trace, with rate) — proven.** Truncating to prime powers
$q\le M_n$ (which the Phase-1 sieve enumerates exactly),
$$
\Big|\mathrm{Tr}\big(\mathbb W^{1/2}g(\mathbb A)\mathbb W^{1/2}\big)
- \mathrm{Tr}\big(\mathbb W_n^{1/2}g(\mathbb A_n)\mathbb W_n^{1/2}\big)\Big|
\ \le\ C\,c\,\frac{1+\varepsilon}{\varepsilon}\,M_n^{-\varepsilon},
$$
and $A_n\to A$ in strong resolvent sense. (prime-side.md Prop 6.1.)

**This is the honest reformulation of Conjecture 5.1.** Convergence *does* hold — not of
eigenvalues to zeros, but of the sieve-truncated **trace** to the arithmetic side of the explicit
formula, at a proven rate $M_n^{-\varepsilon}$. RH then sits, equivalently, in a
boundary-regularity statement about the flow character $\chi_W(z)=-\frac{\zeta'}{\zeta}(\tfrac12
-iz)$ (prime-side.md Cor 5.4) — constructed, but undecided.

## 4.5 The trace, produced (both the repaired-operator trace and the honest one)

**The repaired-operator trace** $\mathrm{Tr}\,g(H_n')$ is now computed
(`repaired_trace_report`, Gaussian $g$, $t=0.2$):

```
  n    dim    Tr g(diag)   Tr g(H_rep)  off-diag corr    arith side
  8     54     16.736131     16.749353       0.013222      0.603035
 10    172     54.401386     54.403643       0.002258      0.603035
 14   1900    632.543393    632.614184       0.070791      0.603035
```

It **diverges** with the matrix dimension and the off-diagonal correction is negligible: a finite
matrix on prime positions does not compute the explicit-formula trace. The honest arithmetic side
(last column) is the constant $0.603035$ — computed as the *adelic* sum over places, which is the
subject of the new [phase6.md](phase6.md).

**The honest (convergent) trace** is produced adelically in [adele_trace.py](adele_trace.py):
the explicit-formula balance is reproduced to $10^{-36}$ and the sieve truncation error is
verified to be $O(M_n^{-1/2})$. See [phase6.md](phase6.md) §6.3. This is the *convergent*
experiment that Conjecture 5.1 should have been.

## 4.6 Task status

| Task | Status |
|---|---|
| State Conjecture 5.1 precisely | ✓ (§4.1) |
| Test eigenvalue $\to$ zero unfolding | ✓ — **refuted** (§4.3) |
| Logical gap (weak-limit $\ne$ HP) | recorded (§4.2) |
| Restate Conj 5.1 non-vacuously as trace convergence | ✓ **corrected** — Thm 4.1/4.2, **proven** (§4.4) |
| Produce repaired-operator trace | ✓ `repaired_trace_report` (§4.5) — diverges, as expected |
| Produce honest convergent trace + balance | ✓ **done adelically** — [phase6.md](phase6.md) |
| Eigenvalue-to-zero unfolding | closed (negative, §4.3) — do not pursue |
