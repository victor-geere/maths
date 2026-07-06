# theorems.md — Catalog of Proven Statements, Verified Results, and Conjectures in the prime-sieve Folder

*All tags follow the repository [rigour convention](../../CLAUDE.md): **proven**, **verified** (numerically to machine precision or high accuracy), **heuristic**, **open**, **RH-equivalent**. This file aggregates every item explicitly tagged **proven** or **verified** from [path.md](path.md), [findings.md](findings.md), [notes.md](notes.md), [implementation.md](implementation.md), and related artifacts (as of 5 Jul 2026 run). RH remains **open**. No claim here advances beyond the tagged status or the wall identified in Theorem P2.3.*

*Cross-references are to the precise location where the statement is proved, verified, or refuted. Defects (D1/D2) and misstatements (M1–M5) from the old artifacts are recorded as **proven** negative results and have been repaired.*

## 1. Classical Theorems and Lemmas (Imported, Proven)

- **Lemma P1.1 (Determinant continuity / Fredholm determinant convergence currency)**: For trace-class operators, |det(I−A) − det(I−B)| ≤ ‖A−B‖₁ exp(‖A‖₁ + ‖B‖₁ + 1). Hence holomorphic trace-class families converging in trace norm yield locally uniform determinant convergence. (Simon *Trace Ideals* Thm 3.4; Gohberg–Krein.) — **proven (classical)**. ([path.md](path.md))
- **Theorem P3.1 (Kotani–Sunada pole confinement)**: For finite connected (q+1)-regular graphs, nontrivial poles of the Ihara zeta lie on the Ramanujan circle |u|=q^{-1/2} or the real axis. General irregular case gives annulus bounds. Translated to s-plane: non-real poles confined to Re s = 1/2 or real-axis Siegel avatars. — **proven (classical)**. ([path.md](path.md))
- **Lemma P3.4 (Turán–Montgomery caution)**: Partial sums ζ_N(s) have zeros with Re s > 1 for large N (Montgomery 1983), even though ζ is zero-free there. Approximants need a priori confinement (provided by graphs). — **proven (classical)**. ([path.md](path.md))

## 2. Proven Statements in the Corrected Path ([path.md](path.md))

- **Definition P0.1 (Place-cycle model X_N / D_n^{cyc}(s))**: Secular determinant of disjoint union of metric cycles of lengths log p for p ≤ M_n exactly reproduces the truncated Euler product. Orbit lengths = log m for M_n-smooth m. Geometric skeleton of Connes trace formula. — **proven (elementary)**.
- **Definition P0.2 (Bipartite divisor graph B_n)**: Non-vacuous cross-scale coupling (primes p < 2^n to composites in I_n = [2^n, 2^{n+1}) with weights a_p(m) p^{-β}). Edge count ~ 2^n log log 2^n. — **proven (non-vacuous; edges > 0)**.
- **Proposition P1.2 (C1 on Re s > 1 for place-cycle model)**: D_n^{cyc}(s) → 1/ζ(s) locally uniformly on {σ > 1} at Euler-tail rate ≍ M_n^{1−σ}/((σ−1) log M_n). — **proven**.
- **Proposition P1.3 (Bare truncation cannot cross σ = 1)**: For σ ≤ 1 the operator is not trace-class; product diverges in the strip. Analytic continuation problem exactly. — **proven**.
- **Lemmas P2.1 & P2.2 (Hurwitz dictionary: nonvanishing transfer and zero capture)**: Limit zero-free on compact K ⇒ stages eventually zero-free; zeros of stages converge to zeros of limit (with multiplicities via Rouché). — **proven**.
- **Theorem P2.3 (Endgame / the wall)**: Given C1 (uniform determinant convergence to e(s) ξ(s) on the strip), the uniform spectral-gap condition C2 on compacts away from the critical line is **equivalent to RH**. — **proven equivalence; marks the wall**.
- **Corollary P2.4 (Graded ladder / partial gaps ⇔ zero-free regions)**: Given C1, every partial confinement of stage zeros is exactly a zero-free region for ζ (and conversely classical regions force stage confinement). Partial rungs are honest unconditional theorems. — **proven**.
- **P5 Trace–Determinant Bridge**: log det(I − T_n(s)) derivative yields weighted von Mangoldt flow character χ_W(z) = −ζ′/ζ(1/2 − i z); matches [../barry-keating/prime-side.md](../barry-keating/prime-side.md) and [../adele/phase6.md](../adele/phase6.md). — **proven**.

## 3. Verified Numerical / Computational Results ([findings.md](findings.md) & [notes.md](notes.md))

- **F1: Control column & pipeline trustworthiness**: Euler-tail rate measured constant (ratio ~0.07–0.14); strip stall at σ=0.75 exactly as P1.3. Pipeline verified. — **verified** (mpmath dps 30).
- **F2: Weighted Ihara–Bass / resolvent form (obligation W numeric half)**: Candidate B (resolvent M(u) form) agrees to 10^{-15} on random weighted graph and bipartite stage n=5; naive form refuted. Identity classical (Watanabe–Fukumizu 2009; Coste–Zhu 2021). — **verified numerically to 10^{-15}**.
- **F3: Normalised spectral gap stable**: Degree-normalised one-mode gap g_sym ≈ 0.54–0.57 uniform across n=6–9 (raw gap is Perron artefact). Naive Ramanujan ratio grows. — **measurements verified**; stability **heuristic** pending proof (G3).
- **F4: No graph-Siegel zeros / pure block spectrum**: Exactly 4 detached eigenvalues per stage (Perron ±μ₁ + one complex conjugate pair); no other real detached eigs. Detached count = structural blocks (prime/composite bipartition). Pre-registered "no arithmetic exceptions" prediction confirmed at β=1/2. — **verified**.
- **F8: Quantum-graph no-go (micro-theorem)**: No finite metric flower graph with loop lengths {log p} and s-independent unitary scattering Σ can match ∑ Λ(m) m^{-s} term-by-term (mixed orbits force reducibility → bare Euler product). **Proposition (elementary) — proven**. Adds to no-go catalogue. — **proven**.
- **F9: Spectral statistics**: Neither CUE nor Poisson (KS distances recorded). — **verified null**.
- **Defects D1 & D2 (old artifacts)**: Prime graph empty (A≡0, D1); unfolding tautological (D2). Both **proven** by execution and elementary argument. Repaired in corrected bipartite graph and raw-data protocol. — **proven**.

## 4. Verified Negative Results & Eliminations (Falsifications Honoured)

- **F5 & F6: Family V1 eliminated**: One-sided m^{-s} couplings produce no strip convergence and monotonically worsen functional-equation symmetry. Design law: future H* families **must** embed s ↔ 1−s symmetry by construction (Riemann–Siegel / AFE kernels). — **verified negative**; design law **heuristic** (motivated by AFE).
- **F7: Naive γ1 (Bilu–Linial lifts) closed**: Consecutive stages show < 0.21 containment fraction; no naive covering/lift structure. γ2 (Asano on per-edge products from F2) remains open. — **verified negative** for naive map.

## 5. Open / Heuristic Items (for completeness; not proven)

- Hypothesis H* (coupled determinants converge in strip to e(s)ξ(s)): **open**, falsifiable.
- Weighted confinement locus (G1 / obligation W symbolic half): **open** (numeric half done).
- Uniform normalised gap g_sym ≥ c > 0 (G3 / P3.5): **heuristic** until proved.
- Full operator upgrade (norm-resolvent to self-adjoint positive limit): **RH-equivalent** at full strength.
- RH: **open** — unchanged by any item above.

## 6. Status Ledger Summary (from findings.md & new-research-plan.md)

All items above respect the rigour convention. The corrected path ([path.md](path.md)) relocates the wall into graph-spectral coordinates without lowering it. Future work (G1–G5) targets standalone theorems below the wall (zero-free regions, structural sieve statements, symmetric couplings). See [new-research-plan.md](new-research-plan.md) for gated next steps.

*This catalogue will be updated as new proofs or verifications land. Last updated: 2026-07-05.*
