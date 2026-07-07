# PSC2-S06 — constraints, refutations, dead ends, and walls

*Source document S06. The complete negative knowledge of the program: no-go theorems (N),
proven refutations and corrections (D/M/Thm 3.3), closed routes (X), and RH-equivalent walls
(W). Extracted from `prime-sieve-continued/berry-keating/research-findings.md` §3/§7,
`prime-sieve/notes.md` §2, `adele/phase3–4.md`, and the charter's ledger. **Every item here is
binding on every PSC2 work package**: a proposal violating an N/X item is dead on arrival; a
proposal whose success would be a W item must be priced as the wall, never scheduled as a step.*

---

## 1. No-go theorems — all proven

**N1 (spectral confinement of contractive compressions).** Every eigenvalue of $VAV^*$
($A$ bounded normal, $V$ a contraction) lies in $\{tw : t \in [0,1],\ w \in
\mathrm{conv}\,\sigma(A)\}$. *Consequence:* no contractive compression of a bounded model
produces eigenvalues near $\gamma_1 = 14.13\ldots$; finite stages must let the numerical range
grow.

**N2 ($1/\pi(M)$-normalised prime kernels degenerate).** The averaged prime Gram kernel tends
to $0$ locally uniformly on $\{\mathrm{Im}\,u > -1\}$ and blows up below; positivity cannot
pass to the limit through it. Unnormalised kernels (the von Mangoldt package, S00 §4) are the
correct objects.

**N3 (real entire functions are never Hermite–Biehler).** If $\overline{E(\bar z)} = E(z)$
then $|E(x - iy)| = |E(x + iy)|$: the strict HB inequality fails everywhere. $\Xi$ itself
cannot be a de Branges structure function; the correct (RH-equivalent) target is W5.

**N4 (holomorphic moments cannot certify real support).** $\delta_0$ and the uniform circle
measure share all moments $\int z^k d\nu = \delta_{k,0}$: no "trace moments are real and
determinate, hence the limiting support is real" argument is valid. Reality comes from
self-adjointness, nothing else.

**F8 (quantum-graph no-go).** No closed flower graph with loop lengths $\{\log p\}$ and
$s$-independent unitary scattering matches $\sum_m \Lambda(m)m^{-s}$ termwise (unique
factorisation forces mixed-orbit amplitudes to vanish; that forces reducibility; that is the
bare Euler product, dead in the strip). Full statement and proof: S00 §10. Escape doors
(energy dependence / openness / pseudo-orbit interference) = WP14.

## 2. Proven refutations and corrections

**2.1 Vacuity (D1 / Prop 3.1).** Within one dyadic block, large primes cannot be coupled
through composites of that block ($pq \ge 2^{2n} > 2^{n+1}$). Proven twice (Def 4.1's
$A \equiv 0$; the scripts' empty graph). Design principle: **all non-vacuous coupling is
cross-scale** (primes $< 2^n$ to composites in $I_n$). Details: S00 §2.

**2.2 Density mismatch (Thm 3.3 / Prop 3.7).** $\{\log p\}$-type spectra count as $e^T/T$;
zeros count as $\frac{T}{2\pi}\log\frac{T}{2\pi}$; no unitary conjugation or affine rescaling
reconciles them. RMS residual of the best affine fit: $14.7$, the size of $\gamma_1$. Kills
every eigenvalue program at the $\{\log p\}$ density. Proof: S00 §5.

**2.3 Rank-unfolding fabrication (D2).** Unfolding against the target's own counting function
is input-independent and was range-capped below $\gamma_2$: every reported "match" was
manufactured. Now rule I0.1 (S00 §11), binding.

**2.4 Weak convergence is not Hilbert–Pólya.** Distributional/statistical spectral convergence
is necessary, nowhere near sufficient (S00 §3). No statistical claim counts as L4 progress.

**2.5 Classical-theory corrections (M1–M5).** M1: the Ramanujan locus is $|u| = q^{-1/2}$,
never $|u| = 1$. M2: per-block Euler factors tend to $1$ — corrected objects are cumulative.
M3: $\mathrm{Tr}\,|D|^{-s}$ is Voros' *secondary* zeta (spectrum in poles), not
$\pi^{-s/2}\Gamma(s/2)\zeta(s)$ (zeros as zeros) — keep the categories separate. M4: Connes
1999 proves the *semi-local* trace formula; the global Hilbert-space statement is
RH-equivalent; Meyer 2005 realises all zeros unconditionally on *nuclear non-Hilbert* spaces —
positivity is the entire remaining content. M5: *strong* resolvent convergence does not
control spectra (pollution); *norm*-resolvent is the mode that does (Reed–Simon VIII.7).

## 3. Dead ends (X-ledger) — closed; do not reopen

| # | Route | Killed by |
|---|---|---|
| X1 | eigenvalue→zero at $\{\log p\}$ scaling, any affine rescaling | §2.2 (**proven**) |
| X2 | block-local coupling | §2.1 (**proven**) |
| X3 | rank-unfolding / target-consuming normalisation as evidence | §2.3 (**proven + executed**) |
| X4 | one-sided $m^{-s}$ coupling kernels (family V1) | F6: FE asymmetry monotonically worsens (**verified negative**) |
| X5 | naive stage-to-stage lifts (route γ1) | F7: containment $\approx 0.17$ (**verified negative**) |
| X6 | closed, $s$-independent-unitary quantum graphs | F8 (**proven no-go**) |
| X7 | greedy harmonic threshold-family decomposition | refuted by execution (nesting fails; counting $O(\log\log N)$); Beurling generalized primes is the principled home |
| X8 | the Weierstrass "sweep" as evidence about zero locations | paths chosen from the known zero list — target-consuming (S04 §5) |
| X9 | "zero ordinates near integers" | density classes $T$ vs $T\log T$ (S04 §5) |
| X10 | gate-1.md locus + Asano proofs as written | audit failures itemised in [S05](PSC2-S05-salvaged-G1.md) header |
| X11 | statistics/ensemble agreement as Hilbert–Pólya progress | §2.4; F9 null |
| X12 | the discarded `barry-keating-hp-*` proof series | refuted at three independent provable points; audit trail in the parent snapshot's `flawed/` and `berry-keating/worksheet.md` |
| X13 | stage-to-stage Asano/Lee–Yang gluing (route γ2) — and with X5 the whole of route γ below the W3 wall | WP13's pre-registered falsifier fired ([F06](../findings/PSC2-F06-asano-gluing.md)): the sieve step's exact gluing law is **proven**, and that law shows the multiplier vanishes inside every centered candidate region (strict Perron injection, 45/45 core steps $n \le 6$); no Asano-reachable region survives to $n = 9$ |

> **Addendum (7 Jul 2026).** Row X13 appended per the audit-trail convention when WP13 landed
> in the falsifier branch; the table above is otherwise unchanged. W3 (route γ at *full*
> Ramanujan strength, with C1) is untouched — it remains an RH-equivalent wall, not a dead end.

## 4. Walls (W-ledger) — proven RH-equivalent; priced, never attacked

| # | Wall | Equivalence proven in |
|---|---|---|
| W1 | E5 completeness: $\mathrm{spec} = \{\pm\gamma\}$, nothing extra/missing, on a genuine Hilbert space | Weil positivity; S01 §4 |
| W2 | C2 at full uniform strength, given C1 | Hurwitz dictionary P2.3 (S02 §4) |
| W3 | route γ at full Ramanujan strength, with C1 | P2.3 corollary; MSS reality-of-roots = HB in polynomial coordinates |
| W4 | norm-resolvent convergence with a positive limit pairing | path P4 chain; Meyer calibration |
| W5 | any HB function $E$ with $A$-part $= \Xi$; equivalently $K_h \succeq 0$ for all $h > 0$ | research-findings Thm 7.1 (**full proof in the parent snapshot**) |
| W6 | Weil positivity; Li positivity for all $n$; Connes' global trace formula | classical (Weil 1952; Bombieri–Lagarias 1999; Connes 1999) |

**Calibrators.** *Meyer 2005:* unconditional realization of all zeros on nuclear non-Hilbert
spaces — the standing category-change detector: any claimed spectral success must say where
its positivity comes from, or it has silently reproduced Meyer. *Connes–Moscovici 2022:*
proven semiclassical counting match, exact identification open — the precedent that E0a's
smooth Weyl law is attainable *and* the proof that matching it is not evidence of matching
zeros (obstruction O6, the shape decoy).

## 5. Evidence hygiene (rule I0) — binding on every experiment

1. No rank-based unfolding against the target's counting function; comparisons use raw
   quantities against independently computed truth (`mpmath.zetazero`, `mpmath.zeta`).
2. Non-vacuity guards on every constructed object (edges $> 0$; operator $\ne 0$).
3. Correct loci ($|u| = q^{-1/2}$ / weighted annulus; never $|u| = 1$).
4. Two-sided reporting: falsification criteria declared before running; results recorded
   either way.
5. Cross-checks against in-repo verified numbers
   ([PSC2-N00](../numerics/PSC2-N00-verification-targets.md)), not ad-hoc recomputation.
6. The $\gamma$-list appears only inside final-evaluation metrics (E4b), never in
   construction, scaling, or normalisation.
7. The sine model (S04 §5, HS6) runs as decoy on every new harness component.
