# PSC2-000 — charter: the unified program, its inventory, and its triage

*Governance document 000 of project PSC2 (6 Jul 2026). Standalone adaptation of
`prime-sieve-continued/research-plan-2.md`: every source it cites is extracted into
[sources/](sources/) (S00–S06), every open problem is a work package in
[workpackages/](workpackages/), every verification number is in
[numerics/PSC2-N00](numerics/PSC2-N00-verification-targets.md). Conventions and the
declaration bar: [PSC2-001](PSC2-001-conventions.md). **RH is open.***

---

## 1. The unified picture: one object, four levels, and a model pair

| Level | Object | Status | Source doc |
|---|---|---|---|
| **L1 trace** | place-by-place Weil trace; sieve truncation rate $O(M_n^{-1/2})$ | **proven + verified to $10^{-36}$** | [S00](sources/PSC2-S00-verified-foundation.md) §4–6 |
| **L2 character** | flow character $\chi_W(z) = -\frac{\zeta'}{\zeta}(\tfrac12 - iz)$; circularity of "sieve bridge + Weil" | **proven** — a *closed* level | [S01](sources/PSC2-S01-character-level.md) |
| **L3 determinant** | stage determinants $\to e\,\xi$ on the strip (C1 / H\*); Hurwitz dictionary | **open**; given C1, C2 $\iff$ RH (wall) | [S02](sources/PSC2-S02-determinant-level.md) |
| **L4 eigenvalue** | sieve-Galerkin compression $H^G_n = P_nDP_n$; E-gates | **open**; completeness (E5) is RH-equivalent | [S03](sources/PSC2-S03-eigenvalue-level.md) |

The levels are bridged by proven identities ($\log\det$ ladder L1→L3; Hurwitz/Rouché L3→zero
locations), and the wall appears at the same height in every coordinate system — Weil
positivity ≡ real $\chi_W$-poles ≡ C2-given-C1 ≡ completeness-with-positivity — all proven
equivalent to RH ([S06 §4](sources/PSC2-S06-constraints-and-walls.md)). **The program is a
coordinate change on Hilbert–Pólya, not a detour around it**; the actionable residue is the
graded ladder below the wall (P2.4 zero-free-region rungs; E2 inclusion; E3b certified
enclosures).

Alongside the arithmetic object sits the **model pair**
([S04](sources/PSC2-S04-model-pair.md)): $\sin(\pi t)/\pi t = \prod(1 - t^2/n^2)$ against
$\Xi(t) = \Xi(0)\prod(1 - t^2/t_k^2)$, with the greedy Egyptian-fraction stages as the
model-side sieve. The model pair is harness apparatus — the canonical positive control and the
canonical decoy — and the source of the HS-gates. **The analogy is the control, not the
evidence.**

## 2. Inventory and triage

**T — tractable now** (clear method; standalone value regardless of the wall):

| # | Problem | WP |
|---|---|---|
| T1 | E1 pairing lemma (+ HS5 pairing-unification claim) | [WP01](workpackages/PSC2-WP01-pairing-lemma.md) — **done** ([F01](findings/PSC2-F01-pairing-lemma.md)) |
| T2 | E0 density gate: intrinsic Weyl law, zero fitted parameters; negative controls must fail | [WP02](workpackages/PSC2-WP02-density-gate.md) — **done, primary killed** ([F02](findings/PSC2-F02-density-gate.md)) |
| T3 | E2 inclusion theorem: fix the ambient (E2a), strong-resolvent inclusion (E2b) | [WP03](workpackages/PSC2-WP03-inclusion-theorem.md) |
| T4 | E3b certified enclosures (second-order relative spectra; pollution-free by theorem) | [WP04](workpackages/PSC2-WP04-certified-enclosures.md) |
| T5 | E4 evaluation harness + HS1 product gate, HS2 moment gate, HS6 sine decoy, HS7 genealogy | [WP05](workpackages/PSC2-WP05-evaluation-harness.md) |
| T6 | G1: audit the salvaged Ihara–Bass identity; derive an honest weighted locus | [WP06](workpackages/PSC2-WP06-weighted-locus.md) — **done** ([F03](findings/PSC2-F03-weighted-locus.md): identity **proven**; locus delivered, weak) |
| T7 | G3: normalised-gap census to $n \le 14$, then uniform-bound proof attempt | [WP07](workpackages/PSC2-WP07-normalised-gap.md) |
| T8 | G4: anti-Siegel block-purity theorem; $\beta$-sweep first | [WP08](workpackages/PSC2-WP08-anti-siegel.md) |
| T9 | truncation-rate proposition with constants, as a standalone tagged result | [WP09](workpackages/PSC2-WP09-trace-rate-proposition.md) |
| T10 | restricted-support Weil positivity; first new instance: places $\{\infty, 2\}$ | [WP10](workpackages/PSC2-WP10-weil-positivity-restricted.md) |
| T11 | Li coefficients: unconditional finite-range computation/asymptotics | [WP11](workpackages/PSC2-WP11-li-coefficients.md) |

**H — hard but valid** (open research, below the wall):

| # | Problem | WP |
|---|---|---|
| H1/H2 | H\* via the AFE-symmetric V2 family (G2), spectrally defined through HS5 | [WP12](workpackages/PSC2-WP12-afe-family.md) |
| H3/H4 | P3.5 gap rungs (routes α, β) → dlVP-strength zero-free region via P2.4 | [WP07](workpackages/PSC2-WP07-normalised-gap.md) §ext |
| H5 | Q-γ2 Asano gluing on the per-edge product form | [WP13](workpackages/PSC2-WP13-asano-gluing.md) |
| H6 | escape routes from the F8 no-go (energy-dependent / open / interference) | [WP14](workpackages/PSC2-WP14-escape-routes.md) |
| H7 | E3a norm-resolvent windows — wall-adjacent at full strength; partial windows only, after the cheap gates | (deferred; no WP until E2/E3b land) |
| H8–H10 | BS-convergence of unbounded-degree stages; rigorous adelic operator (with T3); Sonine/Burnol spaces | (deferred) |

**W — walls** (RH-equivalent; consulted, never scheduled): the six-entry ledger of
[S06 §4](sources/PSC2-S06-constraints-and-walls.md), with Meyer 2005 and Connes–Moscovici 2022
as standing calibrators.

**D — dead ends** (closed; binding): the twelve-entry X-ledger of
[S06 §3](sources/PSC2-S06-constraints-and-walls.md).

## 3. Live conjectures (decreasing evidential support)

1. **Uniform normalised gap** $g_{\mathrm{sym}}(n) \ge c > 0$ — measured stable
   $\approx 0.56$ (WP07).
2. **Block-purity of detached spectrum** — exact count 4 at every measured stage (WP08).
3. **H\*** — C1 in the strip for a coupled family (WP12); the single most valuable L3 target.
4. **E0 Weyl law for $H^G_n$** — **refuted** (6 Jul 2026,
   [F02](findings/PSC2-F02-density-gate.md)): the first kill executed as designed. Measured
   deviation grows $3.5 \to 6.3$ over stages $n = 4\ldots12$ against a required decrease to
   $\le 0.05$, with the harness two-sidedly validated; a proven no-go lemma extends the kill
   to every fixed-basis compression with concave counting law. No longer a live conjecture.
5. **Q-γ2 Asano structure** (WP13).
6. **HS1 paired-product gate, HS2 moment gate, HS7 genealogy** — stated in
   [S04](sources/PSC2-S04-model-pair.md) §3–7, owned by WP05. (HS5 pairing law: **proven**,
   [F01](findings/PSC2-F01-pairing-lemma.md) — no longer a conjecture.)

## 4. Ordering

```
WP01 (E1, days) ─┬→ HS5 claim (routine after E1)
                 └→ WP02 (E0, first kill) ─→ WP03 (E2) ─→ WP04 (E3b) ─→ WP05 (E4 + HS gates)
WP06 (G1 audit + honest locus) ─→ WP08 (anti-Siegel)
WP07 (gap census first, then proof; routes α/β as extensions)
WP09 · WP10 · WP11  (independent, start any time)
WP12 (V2/H*) after WP01 fixes the paired form  ·  WP13 after WP06  ·  WP14 opportunistic
```

Every WP carries its own falsifier and its own standalone value if the wall never falls. Any
outcome — including total failure of $H^G_n$ at E0 — is a reportable finding
([findings/PSC2-F00](findings/PSC2-F00-template.md)).

**Ordering update (6 Jul 2026).** That outcome occurred: WP02 ran and killed the primary
([F02](findings/PSC2-F02-density-gate.md)). Per WP02's falsifier the E-track is stopped —
WP03/WP04/WP05 carry pause notices — until a redesigned window is proposed (F02's redesign
note: wedge-shaped phase-space support / the prolate pencil $(D, D^2)$; WP04 is first in
line on reopening, since the $D^2$ matrix elements are already delivered). The project's
weight shifts to WP06–WP08 and WP12, as scheduled above.

**Ordering update (7 Jul 2026).** WP06 landed ([F03](findings/PSC2-F03-weighted-locus.md)):
the G1 identity is **proven** (audit closed) and the honest locus is delivered — in the
pre-registered *weak* branch (fat annulus; locus-detached count $0$ at every stage). Per
WP06's falsifier, **WP08 proceeds with its theorem target re-scoped to the measured census**
(β-sweep ordering unchanged); **WP13 is unblocked** (its input — the proven per-edge product
form — is now safe to build on).

## 5. Do-not list (binding; from S06)

No unfolding/fitting/calibration against $N(T)$ or the $\gamma$-list (evaluation-only
exception: E4b). No statistical claims as Hilbert–Pólya progress. No spectral conclusions from
strong-resolvent convergence alone. No eigenvalue programs at the $\{\log p\}$ density. No
block-local couplings. No one-sided $m^{-s}$ kernels. No closed $s$-independent-unitary
quantum-graph matching. No silent category change (Meyer detector). No reopening X-ledger
routes. No presenting gate progress as approaching RH.

## 6. Status ledger

| Item | Tag |
|---|---|
| L1 trace identity + verification + rate | **proven** |
| L2 character identity; circularity | **proven** |
| Hurwitz dictionary; Kotani–Sunada; Turán–Montgomery; F8 no-go; N1–N4; HB equivalence | **proven** |
| Weighted Ihara–Bass identity (multigraph form) | **proven** (6 Jul → 7 Jul 2026: explicit factorisation + exact $\mathbb Q$-certification at $n \le 6$ + Watanabe–Fukumizu cross-check, [F03](findings/PSC2-F03-weighted-locus.md); supersedes "under audit", [S05](sources/PSC2-S05-salvaged-G1.md)) |
| Weighted locus (leaf reduction; balance identities; annulus $[r_1, r_2]$ for non-real poles; Perron inner bound) | **proven**, radii fitted-constant-free; containment **verified** $n = 4\ldots9$ + census; the annulus is **weak** — cannot separate structural detachment, WP08 re-scoped to the measured census ([F03](findings/PSC2-F03-weighted-locus.md)) |
| E0 for the primary $H^G_n$ (N0 fixed-basis instantiation) | **failed — killed** ([F02](findings/PSC2-F02-density-gate.md)); no-go lemma for concave counting laws **proven**; E-track paused |
| E-gates E2–E5 (paused pending redesigned window), G-gates, H\*, P3.5, Q-γ2, HS1/HS2/HS7 | **open** (triaged above) |
| E1 pairing lemma + HS5 pairing law | **proven** ([F01](findings/PSC2-F01-pairing-lemma.md)); $J$-invariant basis **constructed** by WP02's N0 builder ([F02](findings/PSC2-F02-density-gate.md)) — residual obligation discharged |
| HS3 Sylvester basis (in WP05 backlog) | **exploratory** |
| X-ledger (12 routes) | **dead ends**, recorded |
| W-ledger (6 walls) | **RH-equivalent** |
| RH | **open** |
