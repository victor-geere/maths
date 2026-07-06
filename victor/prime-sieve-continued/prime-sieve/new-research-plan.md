# new-research-plan.md — the prime-sieve program after the first measured findings

*Derived from [findings.md](findings.md) (run of 5 Jul 2026); the standing map is
[path.md](path.md) — this file is the marching order. Tags per the repository
[rigour convention](../CLAUDE.md). RH is **open**; by path.md Theorem P2.3 the program's
terminal rung is the known wall, so every task below is deliberately priced *below* the wall,
with its own falsifier and its own standalone value.*

---

## 0. Constraints now binding (extracted from the findings)

| # | Constraint | Source |
|---|---|---|
| C-1 | All weighted-stage spectral reasoning goes through the resolvent-form Ihara–Bass identity and its vertex matrix $M(u)$ — never through unweighted Bass intuition | F2 |
| C-2 | Coupling families for H\* must be $s \leftrightarrow 1-s$ symmetric **by construction** (AFE/Riemann–Siegel-type kernels); one-sided $m^{-s}$ kernels provably degrade the functional equation | F6 |
| C-3 | Closed quantum-graph models with $s$-independent unitary scattering are dead for termwise arithmetic matching — work only in the three escape directions (energy-dependent, open/resonance, pseudo-orbit interference) | F8 (**proven no-go**) |
| C-4 | The meaningful gap observable is the *normalised* one ($g_{\mathrm{sym}}$), not the raw Perron-dominated gap | F3, I8 |
| C-5 | Naive stage-to-stage lift/covering arguments are closed; cross-scale structure must be sought through explicit maps or through Asano gluing on the per-edge product form | F7, F2 |
| C-6 | Evidence rules of implementation.md I0 (no unfolding, non-vacuity guards, pre-registered falsifiers, cross-checks) apply to every experiment below | F10, D1/D2 |

---

## 1. Gate G1 — the weighted locus theorem (the single gating lemma)

**Task.** Prove symbolically, for the weight class $w_{pm} = a_p(m)\,p^{-\beta}$ (and general
symmetric positive weights), the identity verified in F2:
$\det(I - uB_w) = \prod_e (1 - u^2w_e^2)\,\det M(u)$; then derive from $\det M(u) = 0$ the
**confinement locus** of the weighted stage poles — the replacement for Kotani–Sunada's
circle-plus-reals (path.md P3.1) — including: where non-real poles can live as a function of
the weight distribution, and what "detached/exceptional" means intrinsically.

- *Method:* sympy-verifier MCP at $n \le 6$ (coefficient-level identity), then the standard
  proof skeleton (Watanabe–Fukumizu 2009; Coste–Zhu 2021) adapted; locus analysis via the
  Herglotz-type structure of $M(u)$'s diagonal (each term $u^2w^2/(1-u^2w^2)$ is a Möbius
  function of $u^2$ — the reality/positivity structure is favourable).
- *Deliverable:* a `W-theorem` section (here or a dedicated note), tagged **proven**.
- *Falsifier:* none needed — F2's $10^{-15}$ agreement makes failure of the identity
  implausible; the open risk is that the locus statement is weak (a fat annulus). Even a weak
  locus unblocks G4.
- *Why first:* F4's "no graph-Siegel zeros" and any Ramanujan-type claim are **undefined**
  until this locus exists (findings F3.3, F4).

## 2. Gate G2 — AFE-symmetric coupling family (the corrected H\* attack)

**Task.** Replace family V1 (eliminated, F5/F6) by V2 obeying C-2: couplings built from
symmetrised kernels, schematically
$$C^{V2}_{pq}(s) \;=\; \sum_{m \in I_n,\ pq \mid m} a_p a_q\,
\Big[ m^{-s} \varphi(s) + m^{s-1} \varphi(1-s) \Big]\cdot(pq)^{\text{calibration}},$$
with $\varphi$ a smooth AFE cutoff (Hardy–Littlewood; Riemann–Siegel as the sharp case), so
that $C^{V2}(s) = C^{V2}(1-s)$ identically. Re-run the F5 stability sweep and the F6
asymmetry sweep.

- *Gate criterion (pre-registered):* median FE asymmetry **decreasing in $n$** at some fixed
  $\theta \ne 0$, while the $\sigma > 1$ control stays intact (C1-consistency, F1). That
  outcome would be the first genuine evidence for H\*; tag would remain **heuristic** until a
  convergence proof.
- *Falsifier:* if no V2 member beats the $\theta = 0$ baseline (1.17), H\* in determinant form
  is demoted: record, and refocus the folder on the trace-ladder payoffs (G3/G4), which do
  not need H\*.
- *Physics note (why V2 is plausible):* the AFE *is* the discrete functional-equation
  symmetry; building it into the stage operator mirrors how the prolate/archimedean fiber
  carries the $\Gamma$-factor in Connes–Moscovici — symmetry first, convergence second.

## 3. Gate G3 — the normalised-gap theorem (dlVP rung, restated by the data)

**Task.** Prove: there is $c > 0$ with $g_{\mathrm{sym}}(n) \ge c$ for all $n$ — the uniform
random-walk spectral gap of the divisor graph $B_n$ (measured stable at $\approx 0.56$, F3).

- *Method:* the normalised one-mode operator is a doubly-smoothed divisor-correlation form;
  the Perron vector is explicit to first order ($\sim$ degree profile $2^n/p$-type); the
  fluctuation part is a bilinear form over $\#\{m \in I_n : pq \mid m\} - 2^n/(pq)$ —
  Brun–Titchmarsh + Montgomery's large sieve territory (path.md route α), now aimed at the
  *right* normalisation per C-4.
- *Deliverable:* Proposition (uniform normalised expansion of sieve divisor graphs), tagged
  **proven** if it lands; independently publishable-grade regardless of the zeta connection.
- *Payoff dictionary:* through G1's locus + (if G2 succeeds) H\*, P2.4 converts a uniform gap
  into a zero-free region; the honest expected strength at $c/1$-type gaps must be computed,
  not assumed — the dlVP-strength claim is a *target output* of this task, not an input.
- *Falsifier:* census at larger $n$ (sparse eigensolvers, $n \le 14$) showing
  $g_{\mathrm{sym}}$ drifting down would kill the uniform-gap conjecture early — run the
  census extension *before* investing in the proof.

## 4. Gate G4 — block-purity of the detached spectrum (the anti-Siegel theorem)

**Task.** Upgrade F4 from measurement to theorem: relative to G1's locus, the detached
spectrum of $B_w$ consists exactly of the structural (Perron + bipartite-mirror + block) part
— no arithmetic exceptionals. Sweep $\beta \in [0.3, 0.7]$ numerically first to check the
finding is not a $\beta = \tfrac12$ accident.

- *Method:* community-detection technology (Krzakala et al.; Bordenave–Lelarge–Massoulié):
  detached non-backtracking eigenvalues $\leftrightarrow$ block structure; our graph has an
  explicit 2-block (prime/composite) + degree-profile structure, so the expected detached set
  is computable. The proof input is again divisor-count concentration (shared with G3).
- *Significance if proven:* the finite stages provably exhibit **no Landau–Siegel avatar** —
  a clean structural statement about the sieve, meaningful independent of RH; and the honest
  finite-stage half of the "avoiding exceptional zeros" step that proof-sketch.md step 3
  hand-waved.
- *Falsifier:* a $\beta$ where a fifth eigenvalue detaches persistently — would be a genuine
  discovery either way (document per I4.2's two-sided rule).

## 5. Gate G5 — the three escape routes from the F8 no-go (exploratory tier)

Per C-3, closed unitary $s$-independent models are dead. Three doors remain, each with a
small, concrete first experiment:

1. **Energy-dependent scattering** $\Sigma(s)$: fit the minimal $s$-dependence restoring the
   $\Lambda$-support on $m \le 100$; compare its analytic shape to the archimedean
   $\Gamma$-factor and to the Connes–Moscovici prolate structure (the natural home of
   energy dependence). *Question:* is the required $\Sigma(s)$ inner-function-like
   (unitary on the critical line, contractive off it)? That property is Hermite–Biehler-shaped
   — if it appears, it connects this folder to research-findings §6.2/§7.1 exactly at the
   wall, as it must.
2. **Open graphs / resonances:** make the flower lossy (subunitary $\Sigma$); zeros as
   resonances of an open system. First experiment: can a rank-one opening reproduce the first
   Weil-term signs? (Ties to Lee–Yang: openness $=$ boundary field.)
3. **Pseudo-orbit interference:** compute the size of the mixed-orbit sector that must cancel
   at each length $\log m$; quantify as a function of cutoff — the "interference budget" the
   arithmetic demands (Berry–Keating resurgence heuristics as guide).

All tagged **exploratory**; each has a numeric first step in the existing lab framework.

## 6. Gate G6 — Asano gluing on the per-edge product (route γ2, now well-posed)

**Task.** Using F2's form: the stage polynomial is $\prod_e(1 - u^2w_e^2)\det M(u)$ — test at
$n \le 6$ (symbolically) whether the sieve step $n \to n+1$ acts on these polynomials by an
Asano-type contraction/Schur–Szegő composition preserving a zero-locus. C-5 killed the naive
covering route; this is the surviving structural question, and the product form is exactly
Asano-native.

- *Falsifier:* no identifiable gluing structure at small $n$ ⇒ record and close route γ
  entirely; the gap program (G3/G4) does not depend on it.

---

## 7. Ordering, dependencies, effort

```
G1 (locus theorem)  ──┬─→ G4 (anti-Siegel theorem)
                      └─→ [dictionary for] G3 payoff
G2 (AFE family)     ────→ H* verdict → (with G1, P2.4) zero-free-region ladder
G3 (normalised gap) ────→ dlVP-rung candidate (independent value regardless)
G5, G6              ────→ exploratory; feed design constraints back into G2
```

Priority order: **G1 → (G2 ∥ G3) → G4 → G6 → G5.** G1 is pure finite mathematics with the
numeric half already banked (F2) — start there. The plan's honest near-term deliverables are
the two theorems G1 and G3/G4; H\* (G2) is the high-risk/high-value line; G5/G6 are scouts.

## 8. Do-not list (binding)

- No further work on naive stage-to-stage lifts (closed by F7).
- No closed-unitary $s$-independent quantum-graph matching attempts (proven dead, F8).
- No rank-unfolding or any target-consuming comparison (D2; rule I0.1).
- No claim that any gap/locus/symmetry result "approaches RH": by path.md P2.3, the terminal
  rung *is* RH-equivalent territory; per [CLAUDE.md](../CLAUDE.md), RH-equivalent
  restatements are walls, not bridges, and the declaration bar is the full chain, adversarial
  review included. Partial results are to be stated as what they are (expansion theorems,
  locus theorems, zero-free-region equivalences).

## 9. Relation to the repository's two tracks

This plan lives in the Hilbert–Pólya/adèle track. The verified anchor remains the
trace-level Weil balance ([../adele/phase6.md](../adele/phase6.md), $10^{-36}$); this folder
attacks the *determinant level* above it (path.md P5 ladder). The circle-kernel track is
untouched. Any result here that reaches "proven" should be reflected in
[./to-be-reviewed/adele-index.md](../adele/index.md)'s status tables and, where relevant, in
[./to-be-reviewed/berry-keating/research-findings.md](../berry-keating/research-findings.md) §3's no-go
catalogue (the F8 no-go is a candidate N5 entry).
