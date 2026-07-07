# PSC2-S02 — the determinant level (L3): stage determinants, the Hurwitz dictionary, H\*, and the measured record

*Source document S02. Extracted from `prime-sieve-continued/prime-sieve/` — path.md (nodes
P0–P6), findings.md (F1–F10), new-research-plan.md (gates G1–G6). Everything tagged; proofs
included where short and load-bearing, otherwise statement + provenance. The salvaged half of
gate G1 lives in [PSC2-S05](PSC2-S05-salvaged-G1.md).*

---

## 1. The corrected finite objects — proven

**Definition 1.1 (place-cycle model $X_N$; the Connes-faithful control).** One directed metric
cycle of length $\ell_p = \log p$ per prime $p \le M_n$; holonomy $p^{-s}$. Stage secular
determinant
$$D_n^{\mathrm{cyc}}(s) = \det(I - T_n(s)) = \prod_{p \le M_n}(1 - p^{-s}),$$
the truncated Euler product exactly. Periodic-orbit lengths are $\{\log m\}$, $m$
$M_n$-smooth — the support of the explicit formula's prime side. **proven** (elementary).

**Definition 1.2 (bipartite divisor graph $B_n$; the coupled object).** Vertex classes
$\mathcal P_n = \{p < 2^n\}$ and $\mathcal C_n = \{$composites $m \in I_n\}$; edge $p \sim m$
iff $p \mid m$, weight $w_\beta(p,m) = a_p(m)\,p^{-\beta}$, default $\beta = \tfrac12$.
**Non-vacuous: proven** (every even $m \in I_n$ joins $2$ to its odd part's factors). This is
the *only* non-vacuous coupling the dyadic sieve admits — block-local coupling is impossible
(vacuity theorem, [PSC2-S06](PSC2-S06-constraints-and-walls.md) §2.1).

**Division of labour.** $X_N$ owns arithmetic exactness; $B_n$ owns coupling freedom. The open
conjecture H\* (§3) is the bet that coupling freedom buys strip convergence.

## 2. Where the bare model lives and dies — proven

**Lemma 2.1 (determinant continuity; Simon, Trace Ideals Thm 3.4). — proven (classical).**
$|\det(I-A) - \det(I-B)| \le \lVert A-B\rVert_1 \exp(\lVert A\rVert_1 + \lVert B\rVert_1 + 1)$
for trace-class $A,B$; holomorphic trace-norm convergence of kernels gives locally uniform
convergence of Fredholm determinants.

**Proposition 2.2 (C1 on $\mathrm{Re}\,s > 1$). — proven.**
$D_n^{\mathrm{cyc}}(s) \to 1/\zeta(s)$ locally uniformly on $\{\sigma > 1\}$ (Euler-tail rate
$\asymp M_n^{1-\sigma}/((\sigma-1)\log M_n)$; measured, F1).

**Proposition 2.3 (death at the line). — proven.** For $\sigma \le 1$, $T(s)$ is not trace
class and $\prod_{p \le M_n}(1-p^{-s})$ has no nonzero limit in the strip. **The strip version
of C1 for the uncoupled model is exactly the analytic-continuation problem.** Measured: at
$s = 0.75 + 10i$ the truncation error does not decrease ($0.066 \to 0.101$, $n = 6\ldots12$).

## 3. The conjecture H\* and target C1 — open (the level's load-bearing beam)

**Target C1.** Stage determinants $D_n(s)$ (entire, sieve-computable, archimedean prefactor
$\times$ weighted Bass/secular determinant) with $D_n \to e(s)\,\xi(s)$ locally uniformly on
$\Omega = \{0 < \mathrm{Re}\,s < 1\}$. — **open.**

**Hypothesis H\*. — open, falsifiable.** A sieve-computable coupling correction built from
$B_n$'s composite couplings satisfies C1 on $\Omega$. Proof obligations, separable:
(a) weight class/calibration; (b) local-uniform convergence on $\{\sigma > 1\}$ with couplings
on; (c) normal-family bound on compacts of $\Omega$; (d) exact stage functional-equation
symmetry $D_n(s) \leftrightarrow D_n(1-s)$ — the identification set for Vitali, and a design
constraint (see the pairing law, charter conjecture HS5).
*Evidence for:* Gonek–Hughes–Keating hybrid formula (arithmetic factor $\times$ spectral
factor). *Against:* Turán–Montgomery (§5.2); family V1's elimination (§6, F5/F6).

## 4. The Hurwitz dictionary — proven; prices the whole level

Given C1, with $Z = e\,\xi$:

- **P2.1 (limit $\to$ stages).** $Z$ zero-free on compact $K \Rightarrow$ $D_n$ eventually
  zero-free on $K$. — **proven** (elementary).
- **P2.2 (stages $\to$ limit; Hurwitz/Rouché).** Stage zeros converging into $\Omega$ land on
  zeros of $Z$; every zero of $Z$ captures the right count of stage zeros in small discs. —
  **proven.**
- **P2.3 (the endgame).** Define C2: eventual stage-zero-freeness on every compact
  $K \subset \Omega \setminus \{\mathrm{Re}\,s = \tfrac12\}$. Then **C2 $\iff$ RH.** —
  **proven equivalence; this is the wall in determinant coordinates.**
- **P2.4 (graded ladder).** Partial stage-zero confinement on open $\Omega' \iff$ zero-free
  region of $\zeta$ on $\Omega'$. Every unconditional partial gap theorem is a genuine
  zero-free-region theorem — the honest rungs below the wall. — **proven.**

## 5. Confinement and the caution — proven (classical)

**5.1 Kotani–Sunada (P3.1).** For finite $(q{+}1)$-regular graphs all nontrivial Ihara poles
lie on $|u| = q^{-1/2}$ or on the real axis; irregular graphs: non-real poles in the annulus
$q_{\max}^{-1/2} \le |u| \le q_{\min}^{-1/2}$. Finite regular stages cannot have generic
complex off-line zeros — the only escape is real ("graph-Siegel") poles.

**5.2 Turán–Montgomery (P3.4).** Partial sums $\sum_{n \le N} n^{-s}$ have zeros with
$\mathrm{Re}\,s > 1$ for all large $N$ (Montgomery 1983) although $\zeta$ is zero-free there:
approximants do **not** inherit zero-freeness. Spectral origin + self-adjointness of the graph
stages is the advantage over partial sums; **family choice is load-bearing.**

## 6. The measured record (findings F1–F10, run 5 Jul 2026) — verified

| # | Finding | Tag |
|---|---|---|
| F1 | control column at the proven Euler-tail rate; strip stall measured | **verified** (pipeline trustworthy) |
| F2 | weighted Ihara–Bass **resolvent form** validates to $10^{-15}$ on the actual stage graph; naive weighted Bass refuted at $10^{-1}$ | **verified**; symbolic proof = [PSC2-S05](PSC2-S05-salvaged-G1.md) / [WP06](../workpackages/PSC2-WP06-weighted-locus.md) |
| F3 | raw gap ($\approx 0.80$) is Perron-scaling artefact; **normalised** gap stable $g_{\mathrm{sym}} \approx 0.54$–$0.57$ for $n = 6\ldots9$; NB-Ramanujan ratio grows | measured; uniform bound = WP07 |
| F4 | exactly 4 detached eigenvalues at every stage — Perron, mirror, one conjugate pair; **no arithmetic exceptionals** | **verified** at $n \le 9$, $\beta = \tfrac12$; theorem target = WP08 — **correction 2026-07-07, see notice below** |
| F5 | coupled family V1: no strip convergence at any tested $\theta$ | **verified negative** — V1 eliminated |
| F6 | V1 coupling monotonically **destroys** FE symmetry (baseline asymmetry 1.17; $\theta = 1$: 32.7) | **verified negative**; design law C-2: AFE symmetry by construction |
| F7 | consecutive stage spectra containment $\approx 0.17$ — no naive lift structure | **verified negative**; route γ1 closed |
| F8 | quantum-graph no-go (unitary mixing vs $\Lambda$-support) | **proven** (S00 §10) |
| F9 | spectral statistics: neither CUE nor Poisson at this calibration | **verified null** |
| F10 | D1/D2 defects fixed; correction notices in place | audit trail |

> **Correction notice (2026-07-07).** WP08's pre-registered β-sweep
> ([PSC2-F05](../findings/PSC2-F05-anti-siegel.md)) fired the falsifier on F4's count:
> "exactly 4 at every stage" is a finite-window artifact of $n \le 10$, $\beta \ge 0.4$ —
> at $\beta = 0.30$ a fifth eigenvalue detaches persistently from $n = 8$, and at
> $\beta = \tfrac12$ the census becomes $6$ at $n = 11, 12$; the detached set is a growing
> hierarchy of imaginary pairs (leading member = the $(2,3)$-hub mirror). The F4 numbers at
> $n \le 9$, $\beta = \tfrac12$ remain correct as measured. The **no-arithmetic-exceptionals
> half survives and strengthens**: the real-detached census is exactly the Perron pair at
> every sweep point, and F05's edge-purity theorem proves (all $n \ge 4$, all $\beta$) that
> no eigenvalue — real or not — shares the peripheral circle with the Perron pair.

The stage polynomial identity (F2), verified numerically:
$$\det(I - uB_w) = \prod_{e \in E}(1 - u^2 w_e^2)\cdot\det M(u),\qquad
M(u)_{xx} = 1 + u^2\!\sum_{y \sim x}\!\frac{w_{xy}^2}{1 - u^2 w_{xy}^2},\quad
M(u)_{xy} = \frac{-u\,w_{xy}}{1 - u^2 w_{xy}^2}.$$

## 7. Gate state imported into PSC2

| Gate (origin) | Content | Status → PSC2 work package |
|---|---|---|
| G1 | weighted Ihara–Bass identity + honest confinement locus | identity salvageable ([S05](PSC2-S05-salvaged-G1.md)); locus **open** → WP06 |
| G2 | AFE-symmetric coupling family V2 (the corrected H\* attack) | **open** → WP12 |
| G3 | uniform normalised gap $g_{\mathrm{sym}} \ge c$ | **open** → WP07 |
| G4 | block-purity of detached spectrum (anti-Siegel theorem) | **open** → WP08 |
| G5 | escape routes from the F8 no-go | **exploratory** → WP14 |
| G6 | Asano gluing on the per-edge product (route γ2) | **open**, machine-checkable → WP13 |
| P3.5 | $c/\log M_n$ gap from sieve inequalities → dlVP rung via P2.4 | **open, tractable** → WP07 |
| route γ full | uniform Ramanujan with C1 | **= RH** by P2.3 — wall, not scheduled |

> **Closure notice (2026-07-07).** G6 executed as WP13 and landed in the pre-registered
> falsifier branch ([PSC2-F06](../findings/PSC2-F06-asano-gluing.md)): the sieve step's exact
> gluing law is **proven** ($p_{G+x} = p_G\Psi_x$, Green-quadratic multiplier, GWS-reducible
> Asano hypothesis), and that law decides the gate negatively — no zero locus survives the
> composition (strict Perron injection at every same-component core step; no Asano-reachable
> region to $n = 9$). **Route γ2 is closed (X13)**; with X5 (γ1) route γ is closed entirely.
> The "route γ full" row is unaffected: it is the W3 wall, not a schedulable gate.
