# findings.md — measured results of the corrected prime-sieve program

*All numbers below are verbatim output of [prime_graph_lab.py](prime_graph_lab.py)
(run 5 Jul 2026, `mpmath` dps 30, seed 20260705; reproduce with
`cd victor && source .venv/bin/activate && python prime-sieve/prime_graph_lab.py`).
Experiments and their success/failure criteria were pre-registered in
[implementation.md](implementation.md); tags follow the repository
[rigour convention](../../CLAUDE.md). Defect reports D1/D2 and corrections M1–M5 are in
[notes.md](notes.md) §2; the proof-path context for every finding is [path.md](path.md).*

---

## F1. The control column behaves exactly as proven — and the strip stalls exactly as proven

```
  sigma    n        |err|            predicted        ratio
  1.50     6       0.00248243        0.0366359    0.06776
  1.50     8       0.00102483        0.0141869    0.07224
  1.50    10      0.000408167       0.00579803     0.0704
  1.50    12      0.000173761       0.00245244    0.07085
  2.00     6       0.00021721       0.00162546     0.1336
  2.00    12       1.90889e-6       1.35488e-5     0.1409
  --- strip point s = 0.75 + 10i ---
  0.75  n=6,8,10,12:  |Euler_n*zeta - 1| = 0.0659, 0.0871, 0.0855, 0.1006
```

The error/predicted ratio is constant in $n$ at each $\sigma > 1$ (P1.2's Euler-tail rate,
**proven**, now also measured), and at $\sigma = 0.75$ the error does **not** decrease —
the numerical face of P1.3 (**proven**: the bare truncation cannot cross $\sigma = 1$).
*Significance:* the pipeline is trustworthy, and the strip stall is now a measured baseline
any H\* candidate must beat.

## F2. The weighted Ihara–Bass identity is the resolvent form — obligation W's numeric half settled

```
  random weighted (v=8)             max|lhs-candA| = 2.744e-02   max|lhs-candB| = 5.380e-16
  bipartite stage n=5 (v=36)        max|lhs-candA| = 4.867e-01   max|lhs-candB| = 1.687e-15
```

Candidate B validates to machine precision on both a random symmetric-weighted graph and the
actual stage-5 bipartite graph; the naive weighted Bass form (candidate A) is refuted:

$$\det(I - uB_w) \;=\; \prod_{e \in E}\big(1 - u^2 w_e^2\big)\cdot \det M(u),\qquad
M(u)_{xx} = 1 + u^2\!\!\sum_{y \sim x}\!\frac{w_{xy}^2}{1 - u^2 w_{xy}^2},\quad
M(u)_{xy} = \frac{-u\, w_{xy}}{1 - u^2 w_{xy}^2}.$$

Tag: **verified numerically to $10^{-15}$**; the identity is classical in substance
(Watanabe–Fukumizu 2009; Coste–Zhu 2021) — the symbolic re-derivation for our weight class is
task G1 of [new-research-plan.md](new-research-plan.md). *Significance:* (i) the entire pole
analysis of the weighted stages now goes through the explicit vertex matrix $M(u)$; (ii) the
confinement locus is **not** a single circle — it is weight-dependent, so the unweighted
Kotani–Sunada picture (path.md P3.1) must be re-derived through $M(u)$ before "Ramanujan-ness"
of the stages even has a meaning; (iii) the per-edge product $\prod_e(1 - u^2w_e^2)$ is
exactly the multiplicative structure Asano contractions act on — route γ2 gains a concrete
handle (see F7 note).

## F3. Gap census: the raw gap is a scaling artefact; the *normalised* gap is stable at ≈ 0.56

```
    n    g_raw     g_sym     mu1(B)     |mu2|(B)   |mu2|/sqrt(mu1)
     6   0.80627   0.55061     3.5419     3.2985     1.7526
     7   0.78667   0.53722     5.2810     4.8682     2.1184
     8   0.81016   0.56641     7.6871     7.1517     2.5794
     9   0.80372   0.56004    10.9663    10.2298     3.0891
```

Three separate facts:
1. the **raw** one-mode gap ($\approx 0.80$) is confirmed as Perron-scaling artefact (first
   flagged in implementation.md I8) — not usable;
2. the **degree-normalised** one-mode gap is **stable at $g_{\mathrm{sym}} \approx
   0.54$–$0.57$ across $n$** — a genuine uniform-expansion signal for the random-walk
   normalisation of the divisor graph, and the natural candidate statement for the
   sieve-inequality proof (P3.5 restated: prove $g_{\mathrm{sym}} \ge c > 0$ uniformly);
3. the naive non-backtracking Ramanujan ratio $|\mu_2|/\sqrt{\mu_1}$ **grows** ($1.75 \to
   3.09$): at $\beta = \tfrac12$ the stages are *not* almost-Ramanujan in the unweighted-
   benchmark sense. Given F2 (the benchmark itself must be re-derived for weights), this is
   recorded as calibration data, not as a verdict.

Tags: measurements **verified**; the stability of $g_{\mathrm{sym}}$ is **heuristic** until
proven (task G3). *Falsification honoured:* the pre-registered "audit" criterion fired on
$g_{\mathrm{raw}}$, and the pre-registered dlVP-calibration test moves to the normalised gap.

## F4. Graph-Siegel tracking: no arithmetic exceptions — the detached spectrum is pure block structure

```
    n    #eigs   mu1       #detached  #detached-real   detached real list
     6     218     3.542         4           2       [±3.542]   (bipartite mirror: yes)
     7     476     5.281         4           2       [±5.281]
     8    1010     7.687         4           2       [±7.687]
     9    2146    10.966         4           2       [±10.966]
```

At every stage exactly **4** eigenvalues of $B_w$ detach from the $\sqrt{\mu_1}$ disk: the
Perron eigenvalue, its bipartite mirror $-\mu_1$ (both real), and a single complex-conjugate
pair. **No other real eigenvalue ever detaches — the pre-registered "no graph-Siegel zeros"
prediction (P3.2) is confirmed at this weighting**, and the constant detached count has a
clean reading borrowed from community detection (Krzakala et al.): detached non-backtracking
eigenvalues count *structural blocks* — here the prime/composite bipartition — so the
detached set is exhausted by structure, leaving no arithmetic exceptions. Tag: measurement
**verified**; the block-counting reading **heuristic**. *Significance:* the stage spectra
show no avatar of a Landau–Siegel configuration; when the weighted locus (G1) is available,
this experiment upgrades to the honest confinement statement of path.md P3.

## F5. Coupled determinant (H\* probe, family V1): no strip convergence; small θ marginally helps, large θ destroys

```
  theta     r_8->9   r_9->10    |D_last*zeta-1|     (s0 = 0.75 + 10i)
   0.00     0.0418     0.0477        0.0855          <- control (bare Euler truncation)
   0.25     0.0540     0.0463        0.0775
   0.50     0.1074     0.1154        0.1148
   1.00     0.4443     0.7789        0.4889
  -0.50     0.0912     0.0909        0.0856
```

The V1 coupling ($C_{pq}(s) = \sum_{m \in I_n,\, pq \mid m} a_p a_q\, (pq)^{s/2} m^{-s}$)
does **not** produce stage-to-stage convergence at the strip point for any tested $\theta$;
$\theta = 0.25$ gives a marginal, non-decisive improvement in $\zeta$-proximity
($0.0855 \to 0.0775$), and $|\theta| \ge 0.5$ is strictly destructive. Tag: **verified
negative** for family V1; H\* itself remains **open** (one family is eliminated, not the
hypothesis).

## F6. Functional-equation asymmetry: V1 coupling makes it *worse* — the design law for H\*

```
  theta    median |eta(s)/eta(1-s) - 1|      (eta = G(s)/D_n ; Re s = 0.6; t = 5,10,15; n = 9)
   0.00          1.1729    <- baseline: bare truncation has no FE, quantified
   0.25          1.3824
   0.50          8.0996
   1.00         32.6530
```

The bare truncation's FE asymmetry is $O(1)$ (baseline now measured), and the V1 coupling
**monotonically destroys** what symmetry there is. This is the most instructive negative of
the run: couplings built from one-sided kernels $m^{-s}$ cannot approach a functional
equation. **Design law extracted (for the plan):** H\* candidate families must carry the
$s \leftrightarrow 1-s$ symmetry *by construction* — couplings in symmetrised kernels of
Riemann–Siegel/approximate-functional-equation type ($m^{-s} + \chi\text{-weighted } m^{s-1}$),
not one-sided ones. Tag: **verified negative**; the design law is **heuristic** (well-motivated
by the AFE, Hardy–Littlewood).

## F7. Q-γ1 covering probe: no naive lift structure between consecutive stages

```
   n->n+1   containment fraction (rel tol 2%)   [lift signature would be ~1.0]
   6->7     0.167        7->8     0.161        8->9     0.204
```

Consecutive stage spectra are nowhere near containment: $B_{n+1}$ is **not** a Bilu–Linial-type
lift of $B_n$ in any naive sense. Route γ1 as originally posed is closed; the surviving
question is whether a *different* cross-scale map (e.g. induced by $m \mapsto 2m$ on
composites) carries a lift structure. Tag: **verified negative** for the naive map.
*Note for route γ2:* F2's per-edge product form is Asano-compatible, so the γ2 (gluing)
question stays open and is now better-posed than γ1.

## F8. Quantum-graph no-go (new micro-theorem): unitary mixing is incompatible with the von Mangoldt support

```
   m      amplitude      Lambda(m)/sqrt(m)    ratio        (Neumann flower, loops 2,3,5,7,11)
     2      0.20000        0.49013       0.4081
     4      0.04000        0.34657       0.1154
     8      0.00800        0.24506       0.0326
  mixed orbits:  |sigma_pq sigma_qp| = 0.04  vs  Lambda(pq) = 0   for (2,3),(2,5),(3,5)
```

**Proposition (no-go, elementary). — proven.** No finite metric "flower" graph with loop
lengths $\{\log p\}$ and an $s$-independent unitary vertex scattering matrix $\Sigma$ can have
its periodic-orbit expansion match $\sum_m \Lambda(m)\, m^{-s}$ term by term. *Proof.* Orbit
lengths are $\log m$ by construction, and by unique factorisation distinct $m$ give distinct
lengths, so matching is forced termwise as generalised Dirichlet series. A mixed orbit through
distinct loops $p \ne q$ has length $\log(pq\cdots)$ with $\Lambda = 0$, so its amplitude
(product of $\Sigma$-entries) must vanish. If *every* mixed closed word has zero amplitude,
$\Sigma$ is reducible on the loop blocks, i.e. the evolution decouples into single loops —
which is exactly the bare Euler product, provably non-convergent in the strip (P1.3). If
$\Sigma$ is irreducible, some mixed closed word has all steps nonzero — contradiction.
$\blacksquare$

*Significance:* this adds an N5-shaped design fence to the repo's no-go catalogue
(research-findings §3): **within closed, $s$-independent-unitary quantum graphs, "chaotic
mixing" and "arithmetic support on prime powers" are mutually exclusive.** Whatever realises
the explicit formula spectrally must either make amplitudes energy-dependent (where the
$\Gamma$-factor lives), work with open systems/resonances (the de Branges/Hermite–Biehler
direction, research-findings §6.2), or achieve the $\Lambda$-support by *interference across
pseudo-orbits* rather than termwise — quantified targets for the plan (task G5). The measured
Neumann table above is the witness: mixed amplitude $0.04 \ne 0$.

## F9. Spectral statistics: neither CUE nor Poisson at this calibration — null recorded

```
  n=8: N=230 gaps; KS to CUE = 0.8872, KS to Poisson = 0.8267
```

Raw non-backtracking angle gaps (data-internal normalisation) match no RMT reference at
$\beta = \tfrac12$, $n = 8$: the spectrum is locus/structure-dominated. Tag: **verified null**.
Recorded so any future "GUE emerges" claim has a baseline to beat; per research-findings §8,
statistics would in any case not constrain zero locations.

## F10. Defects fixed across the folder — audit trail

- [ihara-riemann-spectrums.py](ihara-riemann-spectrums.py),
  [ihara-zeta-convergence.py](ihara-zeta-convergence.py),
  [numeric-verification.py](numeric-verification.py): D1 fixed (vertices = generator primes
  $p < 2^n$, non-empty, with regression asserts), D2 retired (unfolding functions now raise
  with an explanatory error; all evidentiary panels replaced by raw-data statistics), M1
  corrected in captions; the genuine explicit-formula panel kept with its cross-check pointer
  to [../adele/adele_trace.py](../adele/adele_trace.py).
- [proof-sketch.md](proof-sketch.md), [closed-form.md](closed-form.md),
  [ihara-connes.html](ihara-connes.html): correction notices prepended (M1–M5, D1/D2),
  originals preserved below per the audit-trail convention of
  [../flawed/](../flawed/).

---

## Status ledger after this run

| Item | Status |
|---|---|
| Pipeline + control rates (F1) | **verified**; strip stall measured (P1.3 **proven**) |
| Weighted Ihara–Bass = resolvent form (F2) | **verified to $10^{-15}$**; symbolic proof = task G1 |
| Normalised gap $\approx 0.56$ stable (F3) | measured; uniform lower bound = task G3 (**open**) |
| No graph-Siegel zeros at $\beta = \tfrac12$ (F4) | **verified** (prediction confirmed); locus theorem pending G1 |
| H\* family V1 (F5, F6) | **eliminated**; design law: AFE-symmetric kernels (task G2) |
| Naive covering route γ1 (F7) | **closed**; γ2 (Asano on per-edge products) open, better-posed |
| Quantum-graph termwise match (F8) | **impossible — proven no-go**; escape routes enumerated (task G5) |
| RMT statistics (F9) | null at this calibration |
| RH | **open** — unchanged; nothing above is, or is claimed as, progress toward it beyond the tagged items |
