# Phase 6 — The sieve *in* adèle space: the trace formula place by place (the fix)

*New phase (not in the original plan). Fixes the vacuity of Phase 3 by realising the sieve
directly on $X=\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$ à la Connes, instead of as a finite matrix
on a Hilbert space of prime positions.*
*Status: **proven** trace identity (imported), **implemented and verified** numerically here.*

Back: [phase5.md](phase5.md) · Index: [index.md](index.md) · Next: [phase7.md](phase7.md).

## 6.1 Why the finite-matrix approach was the wrong vehicle

[phase3.md](phase3.md) showed the plan's operator $H_n = D_n + \varepsilon_n A$ is vacuous
($A\equiv 0$), and the natural repair $H_n' = D_n' + \varepsilon_n A'$ (basis = primes $<2^n$)
has the wrong normalisation and — worse — the wrong spectral density to be the zeros
([phase4.md](phase4.md) §4.3, Thm 3.3). We can now say this quantitatively at the level of the
*trace*. From `repaired_trace_report` in [sieve_operator.py](sieve_operator.py), Gaussian test
$g$ at $t=0.2$:

```
  n    dim    Tr g(diag)   Tr g(H_rep)  off-diag corr    arith side
  8     54     16.736131     16.749353       0.013222      0.603035
 10    172     54.401386     54.403643       0.002258      0.603035
 12    564    183.501682    183.504221       0.002539      0.603035
 14   1900    632.543393    632.614184       0.070791      0.603035
```

$\mathrm{Tr}\,g(H_n')$ **diverges** with the matrix dimension ($16.7\to 632.6$): it just counts
eigenvalues piled near the recentred mean, and the off-diagonal correction is a rounding effect.
It has nothing to do with the arithmetic side of the explicit formula, which is the constant
$0.603035$. **No finite matrix on prime positions computes the explicit-formula trace**, because
that trace is not $\sum_i g(\lambda_i)$ over a spectrum — it is a sum of *local distributions*,
one per place of $\mathbb Q$. So we move to the space where those distributions live.

## 6.2 The construction on $X$ (Connes 1999)

Connes realises the Weil explicit formula as the trace of the scaling action of the idèle class
group $C_\mathbb{Q}=\mathbb I_\mathbb{Q}/\mathbb{Q}^\times$ on functions over the adèle class space
$X$. For a test function the trace **factors over the places** $v$ of $\mathbb Q$ into local
principal-value integrals of the action of $\mathbb Q_v^\times$:

$$
\underbrace{\sum_\rho h(\gamma_\rho)}_{\text{spectral side}}
\;=\;
\underbrace{W_\infty(g)}_{\text{archimedean place}}
\;-\;
\underbrace{\sum_{p} W_p(g)}_{\text{finite places = the sieve}} ,
$$

with the local terms

$$
W_p(g) \;=\; \int_{\mathbb Q_p^\times}{}' \frac{g(|u|)}{|1-u|_p}\,d^*u
\;=\; 2\sum_{k\ge1}\frac{\log p}{p^{k/2}}\,g(k\log p),
\qquad
W_\infty(g) \;=\; h(\tfrac{i}{2})+h(-\tfrac{i}{2}) - g(0)\log\pi + \frac{1}{2\pi}\!\int h(r)\,\mathrm{Re}\,\frac{\Gamma'}{\Gamma}\!\Big(\tfrac14+\tfrac{ir}{2}\Big)dr .
$$

The finite-place term $W_p$ is a **single prime's** full prime-power contribution; the
$p$-adic principal-value integral evaluates exactly to the von Mangoldt block $\Lambda(p^k)/p^{k/2}$.
Crucially $\sum_p W_p(g) = 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n)$ is a genuine sum
**over places**, not over a basis of vectors — there is no finite Hilbert space and no matrix
$H_n$ at all. (This is the same object proven, from the Hilbert-space side, to be a trace in
[prime-side.md](prime-side.md) Thm 3.4 / Cor 4.2; here it is organised geometrically.)

**Where the sieve enters.** The finite places of $\mathbb Q$ are the primes. The
composite-generator sieve of [phase1.md](phase1.md) enumerates them **exactly**, block by block
$I_n=[2^n,2^{n+1})$, so "compute the geometric side to stage $n$" means "sum $W_p$ over the primes
the sieve has output by stage $n$." This is the constructive content the program wanted — now
attached to the right object.

## 6.3 Implementation and verification

[adele_trace.py](adele_trace.py) computes each local term and assembles the trace. Three checks.

### (a) The geometric side, place by place (`place_breakdown`, $t=0.2$)

```
     place                  local term W_v(g)
  infinity     0.60303464961426464498    (pole + Gamma integral)
         2             0.38013321408074931683
         3             0.17810905607029957823
         5            0.035638958359344853761
         7           0.0081635277715376329746
        11          0.00068961339521426152495
       ...          (decaying like p^{-1/2} g(log p))
     sum p             0.60303464960929003883    (arithmetic side, p<=97)
```

Each prime is one place, contributing one number; the finite places sum to $0.6030346496\ldots$

### (b) Explicit-formula balance (`balance_report`) — reproduces prime-side.md §7E adelically

```
  t = 0.05
    right side  W_inf - arithmetic  : 0.00009175670097147148537
    zero side   sum_rho h(gamma)    : 0.00009175670097147148537
    discrepancy                     : 7.9e-37

  t = 0.2
    right side  W_inf - arithmetic  : 8.860364360447289769e-18
    zero side   sum_rho h(gamma)    : 8.8603643604472897685e-18
    discrepancy                     : 4.5e-37
```

The geometric (place) side and the spectral (zero) side agree to $\sim 10^{-36}$ at 35-digit
precision — an independent adelic recomputation of the values pinned to $2\times10^{-31}$ in
[prime-side.md](prime-side.md) §7E.

### (c) Sieve truncation rate (`truncation_rate`) — Prop 6.1's $O(M_n^{-\varepsilon})$

Summing local terms over the sieve's output up to $M_n$, the partial arithmetic side approaches
its limit at exactly the proven rate. With $\varepsilon=\tfrac12$, $|\text{error}|\cdot M_n^{1/2}$
is constant:

```
    n       M_n       |error|  |error|*M_n^eps
    8       511    0.088009003        1.9894707
   12      8191    0.022115086        2.0015069
   16    131071   0.0055239611        1.9998799
   20   2097151   0.0013810483        1.9999711
```

$|\text{error}|\cdot M_n^{1/2}\to 2.0$: the sieve produces the geometric side **stage by stage
with a controlled $M_n^{-1/2}$ error** — precisely [prime-side.md](prime-side.md) Proposition 6.1,
now realised on the adèle side. (A Gaussian test decays super-exponentially, so its own truncation
is far faster; the polynomial rate is exhibited here on the canonical Dirichlet tail
$\sum\Lambda(q)q^{-1-\varepsilon}\to-\frac{\zeta'}{\zeta}(1+\varepsilon)$ that Prop 6.1 bounds.)

## 6.4 What this fixes, and what it (honestly) does not

**Fixes.** The vacuous/ill-scaled finite operator is replaced by a well-defined, convergent
object living on $X$: the geometric side of the Connes trace formula, computed one place at a
time, with the sieve supplying the places and a proven truncation rate. The "produce a trace from
the sieve" goal of the plan is met — as a sum over places, not a matrix trace.

**Does not.** This is still the *prime/geometric* side of a duality. It equals the zero side by
the explicit formula (verified above), but that identity is Guinand–Weil, not a construction of a
self-adjoint operator whose spectrum *is* $\{\gamma_\rho\}$. RH remains encoded, equivalently, in
the boundary regularity of the flow character $\chi_W(z)=-\frac{\zeta'}{\zeta}(\tfrac12-iz)$
([prime-side.md](prime-side.md) Cor 5.4) — undecided. Per the repository
[rigour convention](../CLAUDE.md), no claim is made that this implies RH. The advance is
**constructive and organisational**: the sieve now feeds the correct adelic object at the correct
rate, instead of a finite matrix that computes nothing arithmetic.

## 6.5 Task status

| Task | Status |
|---|---|
| Local finite-place term $W_p(g)$ | ✓ `local_finite` (adele_trace.py) |
| Archimedean local term $W_\infty(g)$ | ✓ `local_archimedean` |
| Place-by-place geometric side | ✓ `place_breakdown` (§6.3a) |
| Adelic explicit-formula balance to $10^{-36}$ | ✓ `balance_report` (§6.3b) |
| Sieve truncation rate $O(M_n^{-\varepsilon})$ | ✓ `truncation_rate` (§6.3c) |
| Contrast vs finite-matrix trace | ✓ `repaired_trace_report` (§6.1) |
| Self-adjoint operator with spectrum = zeros | **open / undecided** (= RH) |
| Twist to $L(s,\chi)$ (adelic, over $\mathrm{GL}_1$) | **open**, tractable — see [phase5.md](phase5.md) §5.2 |
