# PSC2-N00 — verification targets (regression numbers)

*Every value below is verbatim output of the scripts in this folder, recorded in the parent
snapshot (runs of 4–5 Jul 2026, `mpmath` dps 30–35). Any PSC2 run must reproduce these before
its new results count; a mismatch is itself a reportable finding. Cross-checking against these
tables — never ad-hoc recomputation — is rule I0.5
([S06 §5](../sources/PSC2-S06-constraints-and-walls.md)).*

## 1. L1 anchor — adelic Weil trace (`adele_trace.py`)

Place-by-place breakdown (Gaussian test, $t = 0.2$):

```
     place                  local term W_v(g)
  infinity     0.60303464961426464498    (pole + Gamma integral)
         2             0.38013321408074931683
         3             0.17810905607029957823
         5            0.035638958359344853761
         7           0.0081635277715376329746
        11          0.00068961339521426152495
     sum p             0.60303464960929003883    (arithmetic side, p<=97)
```

Explicit-formula balance:

```
  t = 0.05   right side W_inf - arithmetic : 0.00009175670097147148537
             zero side  sum_rho h(gamma)   : 0.00009175670097147148537
             discrepancy                   : 7.9e-37
  t = 0.2    discrepancy                   : 4.5e-37
```

Sieve truncation rate ($|$error$|\cdot M_n^{1/2} \to 2.0$):

```
    n       M_n       |error|  |error|*M_n^eps
    8       511    0.088009003        1.9894707
   12      8191    0.022115086        2.0015069
   16    131071   0.0055239611        1.9998799
   20   2097151   0.0013810483        1.9999711
```

## 2. Sieve and the refuted comparator (`sieve_operator.py`)

Equidistribution rate ($|\widehat\mu_n(1)|\cdot\log M_n$ stable in $[0.52, 0.61]$):

```
  n       M_n  k_n=pi(M_n)    |mu(1)|   |mu(1)|*logM_n
  8       511           97    0.09758         0.6085
 12      8191         1028    0.06106         0.5502
 16    131071        12251    0.04603         0.5424
 20   2097151       155611    0.03591         0.5227
```

Vacuity (must hold): $\lVert A\rVert_{\mathrm{op}} = 0.0000$ at every $n$ for the Def-4.1
basis; repaired coupling $\lVert A'\rVert_{\mathrm{op}} = 9.27, 19.5, 36.3, 64.71$ at
$n = 8, 10, 12, 14$. Density-mismatch witness: best affine fit of $\mathrm{Spec}(H_{14})$ to
the first 1612 zeros has RMS residual $14.7$. Trace divergence of the repaired matrix:
$\mathrm{Tr}\,g(H_n') = 16.7 \to 632.6$ ($n = 8 \to 14$) vs arithmetic side $0.603035$.

## 3. Graph lab (`prime_graph_lab.py`, seed 20260705)

Weighted Ihara–Bass (resolvent form B vs naive form A):

```
  random weighted (v=8)        max|lhs-candA| = 2.744e-02   max|lhs-candB| = 5.380e-16
  bipartite stage n=5 (v=36)   max|lhs-candA| = 4.867e-01   max|lhs-candB| = 1.687e-15
```

Normalised gap and detached census:

```
    n    g_raw     g_sym     mu1(B)    #detached  #detached-real
    6   0.80627   0.55061     3.5419       4           2
    7   0.78667   0.53722     5.2810       4           2
    8   0.81016   0.56641     7.6871       4           2
    9   0.80372   0.56004    10.9663       4           2
```

Euler control column (error/predicted ratio constant per $\sigma$): $\approx 0.068$–$0.072$
at $\sigma = 1.5$; $\approx 0.134$–$0.141$ at $\sigma = 2.0$. Strip stall at
$s = 0.75 + 10i$: $|E_n\zeta - 1| = 0.0659, 0.0871, 0.0855, 0.1006$ ($n = 6, 8, 10, 12$ —
must NOT decrease). FE-asymmetry baseline (V1 sweep): $\theta = 0$: $1.1729$; $\theta = 1$:
$32.653$ (must worsen monotonically). Q-γ1 containment: $0.167, 0.161, 0.204$
($6{\to}7, 7{\to}8, 8{\to}9$). F8 witness: mixed amplitude $0.04 \ne 0 = \Lambda(pq)$.

## 4. Classical spot-values (independent truth, `mpmath`)

$\gamma_1 = 14.1347251417\ldots$, $\gamma_2 = 21.0220396388\ldots$,
$\gamma_{10} = 49.7738324777\ldots$ (`mpmath.zetazero`; used ONLY in final-evaluation metrics
per I0.6). Explicit-formula regression instance ($h(r) = e^{-(r/6)^2}$): zero side
$0.0077863602482884239503$, sides agree to $9.4 \times 10^{-32}$. Model-pair spot-check:
$\sin(\pi\gamma_1) \approx 0.4107272152$, $\sin(\pi\gamma_1)/(\pi\gamma_1) \approx 0.009249457$
(nonvanishing — the sine decoy's zero set is *not* the arithmetic one).
