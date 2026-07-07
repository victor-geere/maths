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
| T2 | E0 density gate: intrinsic Weyl law, zero fitted parameters; negative controls must fail | [WP02](workpackages/PSC2-WP02-density-gate.md) — **done, primary killed** ([F02](findings/PSC2-F02-density-gate.md)); rewindow [WP02b](workpackages/PSC2-WP02b-density-gate-rewindow.md) — **done, passed** ([F07](findings/PSC2-F07-density-rewindow.md): W1 wedge family clears E0b; E-track reopened; per O6 not evidence about zeros) |
| T3 | E2 inclusion theorem: fix the ambient (E2a), strong-resolvent inclusion (E2b) | [WP03](workpackages/PSC2-WP03-inclusion-theorem.md) |
| T4 | E3b certified enclosures (second-order relative spectra; pollution-free by theorem) | [WP04](workpackages/PSC2-WP04-certified-enclosures.md) |
| T5 | E4 evaluation harness + HS1 product gate, HS2 moment gate, HS6 sine decoy, HS7 genealogy | [WP05](workpackages/PSC2-WP05-evaluation-harness.md) |
| T6 | G1: audit the salvaged Ihara–Bass identity; derive an honest weighted locus | [WP06](workpackages/PSC2-WP06-weighted-locus.md) — **done** ([F03](findings/PSC2-F03-weighted-locus.md): identity **proven**; locus delivered, weak) |
| T7 | G3: normalised-gap census to $n \le 14$, then uniform-bound proof attempt | [WP07](workpackages/PSC2-WP07-normalised-gap.md) — **base theorem done** ([F04](findings/PSC2-F04-normalised-gap.md): census stable to $n=15$; uniform gap **proven**, explicit $c$; sharp constant + routes α/β remain open) |
| T8 | G4: anti-Siegel block-purity theorem; $\beta$-sweep first | [WP08](workpackages/PSC2-WP08-anti-siegel.md) — **done, falsifier branch** ([F05](findings/PSC2-F05-anti-siegel.md): "exactly 4" refuted — hierarchy grows; real census clean everywhere; edge-purity theorem **proven** for all $n \ge 4$, all $\beta$) |
| T9 | truncation-rate proposition with constants, as a standalone tagged result | [WP09](workpackages/PSC2-WP09-trace-rate-proposition.md) |
| T10 | restricted-support Weil positivity; first new instance: places $\{\infty, 2\}$ | [WP10](workpackages/PSC2-WP10-weil-positivity-restricted.md) |
| T11 | Li coefficients: unconditional finite-range computation/asymptotics | [WP11](workpackages/PSC2-WP11-li-coefficients.md) |

**H — hard but valid** (open research, below the wall):

| # | Problem | WP |
|---|---|---|
| H1/H2 | H\* via the AFE-symmetric V2 family (G2), spectrally defined through HS5 | [WP12](workpackages/PSC2-WP12-afe-family.md) |
| H3/H4 | P3.5 gap rungs (routes α, β) → dlVP-strength zero-free region via P2.4 | [WP07](workpackages/PSC2-WP07-normalised-gap.md) §ext |
| H5 | Q-γ2 Asano gluing on the per-edge product form | [WP13](workpackages/PSC2-WP13-asano-gluing.md) — **done, falsifier branch** ([F06](findings/PSC2-F06-asano-gluing.md): gluing law **proven**; no locus survives; route γ **closed**, X13) |
| H6 | escape routes from the F8 no-go (energy-dependent / open / interference) | [WP14](workpackages/PSC2-WP14-escape-routes.md) |
| H7 | E3a norm-resolvent windows — wall-adjacent at full strength; partial windows only, after the cheap gates | (deferred; no WP until E2/E3b land) |
| H8–H10 | BS-convergence of unbounded-degree stages; rigorous adelic operator (with T3); Sonine/Burnol spaces | (deferred) |

**W — walls** (RH-equivalent; consulted, never scheduled): the six-entry ledger of
[S06 §4](sources/PSC2-S06-constraints-and-walls.md), with Meyer 2005 and Connes–Moscovici 2022
as standing calibrators.

**D — dead ends** (closed; binding): the twelve-entry X-ledger of
[S06 §3](sources/PSC2-S06-constraints-and-walls.md).

## 3. Live conjectures (decreasing evidential support)

1. **Uniform normalised gap** $g_{\mathrm{sym}}(n) \ge c > 0$ — **proven** (7 Jul 2026,
   [F04](findings/PSC2-F04-normalised-gap.md)): hub-minorization theorem gives explicit
   $c = 1.2\times10^{-7}$ for $n \ge 10$, Perron–Frobenius below; census extended to
   $n = 15$, flat at $\approx 0.566$. No longer a conjecture in base form; the *sharp
   constant* ($\approx 0.56$) and the α/β gap-rung extensions stay open (WP07 §ext).
2. **Block-purity of detached spectrum** — restated (7 Jul 2026,
   [F05](findings/PSC2-F05-anti-siegel.md)): the count form ("exactly 4 at every stage")
   is **refuted** — the WP08 β-sweep fired the pre-registered falsifier ($\beta = 0.30$:
   persistent fifth from $n = 8$; anchor $\beta = \tfrac12$: crosses at $n = 11$). What
   is **proven** (all $n \ge 4$, all $\beta$): edge purity — only $\pm\rho$, simple, on
   the peripheral circle; count-4 censuses forced into Perron + mirror + imaginary pair.
   What is **verified** and survives as the live conjecture: *no real detached eigenvalue
   besides the Perron pair* (no graph-Siegel avatar) — clean at all 66 grid points +
   $n = 12$, margin improving in $n$; the non-real detached set is a growing hub-mirror
   hierarchy (dictionary **heuristic**). Remaining theorem target: Bordenave-type
   real-sector bulk bound (shared engine with WP07 route β).
3. **H\*** — C1 in the strip for a coupled family (WP12); the single most valuable L3 target.
4. **E0 Weyl law for $H^G_n$** — **refuted for the N0 instantiation** (6 Jul 2026,
   [F02](findings/PSC2-F02-density-gate.md)): the first kill executed as designed. Measured
   deviation grows $3.5 \to 6.3$ over stages $n = 4\ldots12$ against a required decrease to
   $\le 0.05$, with the harness two-sidedly validated; a proven no-go lemma extends the kill
   to every fixed-basis compression with concave counting law. No longer a live conjecture.
   **Salvaged by rewindow** (7 Jul 2026, [F07](findings/PSC2-F07-density-rewindow.md)): the
   wedge-windowed $H^{G,\mathrm{w}}_n$ (W1: Berry–Keating wedge ladders on the sieve sites,
   convex counting law — outside the no-go class by construction) **passes E0b** with dev
   $0.118 \to 0.020$ and the harness valid. Per O6 this is a design certification, not
   evidence about zeros; the arithmetic question moves to E4b/WP05.
5. **Q-γ2 Asano structure** — closed (7 Jul 2026, [F06](findings/PSC2-F06-asano-gluing.md)):
   the sieve step's exact gluing law is **proven** ($p_{G+x} = p_G\Psi_x$, Green-quadratic
   multiplier), but it preserves no zero locus — strict Perron injection at every
   same-component core step, proven and measured 45/45 at $n \le 6$. The pre-registered
   falsifier fired; **route γ closed entirely** (X13). No longer a live conjecture.
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

**Ordering update (7 Jul 2026, later).** WP08 executed in the binding order (β-sweep first)
and landed in the **falsifier branch** ([F05](findings/PSC2-F05-anti-siegel.md)): the count
census is a window artifact, the real census is clean everywhere, and the edge-purity
theorem is proven for every stage and every β. The G-track's remaining open theorem on this
axis (a real-sector bulk bound) shares its engine with WP07 route β; the project's weight
moves to WP12 (H\*) and the independent WP09–WP11, as scheduled.

**Ordering update (7 Jul 2026, later still).** WP13 executed and landed in the **falsifier
branch** ([F06](findings/PSC2-F06-asano-gluing.md)): the atomic sieve step has a proven exact
gluing law (Green-quadratic multiplier; GWS-reducible Asano hypothesis), and precisely that
law shows no zero locus survives the composition — strict Perron injection at every
same-component core step. **Route γ is closed entirely (X13)**; per WP13's pre-registration,
WP07/WP08 are unaffected and W3 stays a priced wall. The banked positives (gluing law; graded
chain at $0.44\to0.70$ efficiency; off-center avoided disk) are recorded in F06 for WP07
route-β's bulk-bound engine. Remaining scheduled work: WP12 (H\*) and WP09–WP11.

**Ordering update (7 Jul 2026, E-track reopened).** The redesigned window F02's falsifier
demanded was proposed, pre-registered, and run:
[WP02b](workpackages/PSC2-WP02b-density-gate-rewindow.md) instantiates F02's own redesign
note (wedge-shaped phase-space support; sieve inventory as translation lengths) as the W1
builder, and the rewindowed primary $H^{G,\mathrm{w}}_n$ **passes E0b**
([F07](findings/PSC2-F07-density-rewindow.md)) with the harness two-sidedly valid. Per the
pre-registration: the E-track pause is lifted — **WP04 first** (its pencil input
$(P_nDP_n, P_nD^2P_n)$ is delivered by the W1 builder), then WP03, then WP05, where the
family's arithmetic content is actually decided (E4b vs the bare-wedge decoy). Binding
caveat carried at every reopened site (O6): passing E0 is not evidence about zeros — the
gate can only kill, and what it killed (N0) stays dead; F02's no-go lemma is untouched
(W1 is outside its hypothesis class by the convexity check run mechanically at every
stage).

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
| Uniform normalised gap $g_{\mathrm{sym}}(n) \ge c > 0$ (G3 base theorem) | **proven** (hub minorization, explicit $c = 1.2\times10^{-7}$ for $n \ge 10$; census flat $\approx 0.566$ to $n = 15$, [F04](findings/PSC2-F04-normalised-gap.md)); sharp constant + routes α/β **open** |
| Edge purity of $B_w$ (G4 at the spectral edge): peripheral spectrum $= \{\pm\rho\}$, simple, all $n \ge 4$, all $\beta$; count-4 censuses forced into Perron + mirror + imaginary pair | **proven** (7 Jul 2026, [F05](findings/PSC2-F05-anti-siegel.md); NB-irreducibility lemma classical with citation, machine-verified at $n = 4\ldots11$) |
| Detached-census count ("exactly 4 at every stage", F4) | **refuted** as an $n$-uniform law ([F05](findings/PSC2-F05-anti-siegel.md), pre-registered falsifier: persistent fifth at $\beta = 0.30$ from $n = 8$; anchor $\beta = \tfrac12$ crosses at $n = 11, 12$); real-detached census $= \{\pm\mu_1\}$ **verified** at every sweep point, margin improving; hub-hierarchy dictionary **heuristic** |
| E0 for the primary $H^G_n$ (N0 fixed-basis instantiation) | **failed — killed** ([F02](findings/PSC2-F02-density-gate.md)); no-go lemma for concave counting laws **proven**; N0 stays dead |
| E0b for the rewindowed primary $H^{G,\mathrm{w}}_n$ (W1 wedge instantiation, [WP02b](workpackages/PSC2-WP02b-density-gate-rewindow.md)) | **passed — verified** (7 Jul 2026, [F07](findings/PSC2-F07-density-rewindow.md); dev $0.118 \to 0.020$, harness valid; builder + derived convex Weyl law + $D/D^2$ closed forms **proven**); E-track **reopened**; per O6 not evidence about zeros |
| Sieve-step gluing law $p_{G+x} = p_G\Psi_x$ (Schur/Green form; $d=2$ transfer quadratic; multi-affine lift + GWS reduction) | **proven** (7 Jul 2026, [F06](findings/PSC2-F06-asano-gluing.md); exact $\mathbb{Q}$ certification at all 95 stage additions $n \le 6$; six MCP cross-checks) |
| Q-γ2 Asano/Lee–Yang gluing (a preserved zero locus for the sieve step); route γ | **dead end — closed** ([F06](findings/PSC2-F06-asano-gluing.md), pre-registered falsifier: strict Perron injection 45/45; factor-zero invasion; no Asano-reachable region to $n = 9$; X13 — do not reopen). Graded Asano/GWS chain (sound, efficiency $0.44\to0.70$): **exploratory** |
| E-gates E2–E4 (reopened 7 Jul 2026 on the W1 family; WP04 first), E5 (wall), G-gates, H\*, P3.5, HS1/HS2/HS7 | **open** (triaged above) |
| E1 pairing lemma + HS5 pairing law | **proven** ([F01](findings/PSC2-F01-pairing-lemma.md)); $J$-invariant basis **constructed** by WP02's N0 builder ([F02](findings/PSC2-F02-density-gate.md)) — residual obligation discharged |
| HS3 Sylvester basis (in WP05 backlog) | **exploratory** |
| X-ledger (12 routes) | **dead ends**, recorded |
| W-ledger (6 walls) | **RH-equivalent** |
| RH | **open** |
