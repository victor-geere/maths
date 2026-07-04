# Phase 3 — The Sieving Laplacian $H_n = D_n + \varepsilon_n A$

*Implements §4 (Definition 4.1) of [prime-sieve-adele-plan.html](prime-sieve-adele-plan.html).*
*Status: **flaw found** — the definition is vacuous as written; a repair is proposed and tested.*

Back: [phase2.md](phase2.md) · Index: [index.md](index.md) · Next: [phase4.md](phase4.md).

## 3.1 The plan's construction

On $V_n = \{\text{primes } p\in I_n\}$ and $W_n=\{\text{composites } m\in I_n\}$, Definition 4.1
sets
$$
A_{p,q} = \sum_{m\in W_n} \frac{a_p(m)\,a_q(m)}{\mathrm{rad}(m)}\,\delta_{p\ne q},
\qquad
D_n = \mathrm{diag}\big(\log p - \tfrac1{N_n}\textstyle\sum_q\log q\big),
\qquad
H_n = D_n + \varepsilon_n A,\ \ \varepsilon_n = \frac{c}{\log M_n},
$$
with $a_p(m)$ the exponent of $p$ in $m$. The idea (plan §4): the off-diagonal $A$ supplies
"level repulsion" that shifts the raw eigenvalues $\log p$ toward the Riemann zeros.

## 3.2 The flaw: $A\equiv 0$

**Proposition 3.1 (vacuity). — proven.** With $V_n=\{\text{primes in }I_n\}$ as in Definition
4.1, $A = 0$ identically, hence $H_n = D_n$ for every $n$.

*Proof.* A term $a_p(m)a_q(m)$ with $p\ne q$ is nonzero only if $m$ is divisible by two distinct
primes $p,q\in V_n$, i.e. $p,q\ge 2^n$. Then $m \ge pq \ge 2^n\cdot 2^n = 2^{2n}$. But
$m\in I_n$ means $m < 2^{n+1}$, and $2^{2n} \ge 2^{n+1}$ for all $n\ge 1$ — contradiction. So no
$m\in W_n$ contributes any off-diagonal entry. $\blacksquare$

The mechanism the plan relies on therefore does not exist: with the prescribed basis there is
nothing off-diagonal to shift $\log p$ anywhere.

**Numerical confirmation** (`phase3_report` in [sieve_operator.py](sieve_operator.py)):

```
  n       M_n   N=|V_n|     eps_n   ||A||_op   min eig H   max eig H
  8       511        43   0.16035     0.0000    -0.37856     0.30481
 10      2047       137   0.13116     0.0000    -0.37244     0.30949
 12      8191       464   0.11098     0.0000    -0.38135     0.31094
 14     32767      1612   0.09618     0.0000    -0.38098     0.30994
 16    131071      5709   0.08486     0.0000    -0.38271     0.31041
```

`||A||_op = 0.0000` throughout, and $\mathrm{Spec}(H_n)=\mathrm{Spec}(D_n)$ is completely
insensitive to the coupling strength (`phase4_report`, all $C$ give
`mean|shift| = 0.000000`). Definition 4.1 is empty.

## 3.3 The repair

The fix is to let composites in $I_n$ couple the *smaller* primes they are actually built from.

**Definition 3.2 (repaired Sieving Laplacian).** Take the basis $V_n' = \{\text{primes } p<2^n\}
= \mathcal P_n$ (Phase 1's sieve primes). For composites $m\in I_n$,
$$
A'_{p,q} = \sum_{m\in W_n}\frac{a_p(m)\,a_q(m)}{\mathrm{rad}(m)}\,\delta_{p\ne q},
\qquad p,q\in\mathcal P_n,
$$
and $H_n' = D_n' + \varepsilon_n A'$ with $D_n'=\mathrm{diag}(\log p)_{p<2^n}$ (recentred).
Now $m = pq\cdots$ with $p,q<2^n$ and $pq\in[2^n,2^{n+1})$ is perfectly possible, so $A'\ne 0$.
Implemented as `compute_leakage_matrix_repaired`.

**Numerical check** (`repair_report`):

```
  n   dim V   ||A||_op    nnz(A)   eps_n*||A||
  8      54     9.2682       298        1.4863
 10     172    19.4920      1150        2.5568
 12     564    36.2938      4324        4.0277
 14    1900    64.7064     16136        6.2231
```

So the repaired $A'$ is genuinely coupled — but a **new problem** appears: $\varepsilon_n
\lVert A'\rVert$ climbs from $1.5$ to $6.2$ and keeps growing. The scaling
$\varepsilon_n\sim 1/\log M_n$ was chosen so the off-diagonal is a *small* perturbation of
$D_n$; here it dominates. $\lVert A'\rVert$ grows because $A'$ sums over $\sim 2^n$ composites on
a basis of only $\sim 2^n/n$ primes. To keep $\varepsilon_n\lVert A'\rVert$ bounded one needs
roughly $\varepsilon_n = c/\lVert A'\rVert = O(1/2^{n/2})$ (empirically $\lVert A'\rVert$ grows
like $\sim 2^{n/2}$), **not** $1/\log M_n$. The plan's normalisation and its coupling matrix are
therefore mutually inconsistent.

## 3.4 The deeper obstruction (why no local fix rescues eigenvalue-to-zero)

Even a well-normalised $H_n'$ cannot have the zeros as eigenvalues, for a reason independent of
the choice of $A$:

**Theorem 3.3 (density mismatch) — proven, imported.** The spectrum $\{\log p\}$ (and any
bounded perturbation of it on a comparable basis) has counting function
$N_A(T)\sim e^T/T$, growing exponentially; the zeros have $N(T)\sim\frac{T}{2\pi}\log\frac
{T}{2\pi}$, growing like $T\log T$. No unitary conjugation and no affine rescaling $aA+b$ maps one
counting asymptotic to the other. (Full statement and proof: [prime-side.md](prime-side.md)
Proposition 3.7.)

So the correct role of $H_n$ is **not** "its eigenvalues are the zeros" — Phase 4 takes this up.

## 3.5 Task status

| Task | Status |
|---|---|
| Implement Def 4.1 exactly | ✓ `compute_leakage_matrix` |
| Prove/verify $A\equiv 0$ (Prop 3.1) | **proven** + numerics ✓ |
| Repair basis to $\mathcal P_n$ (Def 3.2) | ✓ `compute_leakage_matrix_repaired`; $A'\ne 0$ |
| Fix the $\varepsilon_n$ scaling | **open** — must be $\sim 1/\lVert A'\rVert\approx 2^{-n/2}$, not $1/\log M_n$ |
| Eigenvalues $\to$ zeros | **refuted** (Thm 3.3); see [phase4.md](phase4.md) |

**Recommendation.** Redefine the phase-3 deliverable as: *build the trace-class operator
$\mathbb W^{1/2} g(\mathbb A)\mathbb W^{1/2}$ of [prime-side.md](prime-side.md) §3 stage-by-stage
from the sieve*, whose stage-$n$ truncation error is proven $\ll_\varepsilon M_n^{-\varepsilon}$
(prime-side.md Prop 6.1). That is a well-posed, convergent construction; "$H_n=D_n+\varepsilon_n
A$ with eigenvalues the zeros" is not.
