# PSC2-WP10 — restricted-support Weil positivity; the semi-local ladder

*Status: **open**. Independent of the L3/L4 tracks; classical-analysis flavour.*

## Objective

Work the tractable entry point of the Weil-positivity frontier
([S01 §4](../sources/PSC2-S01-character-level.md); parent research-findings §7.2/§9):

1. **Restricted support.** For $\mathrm{supp}\,g \subseteq (-\tfrac12\log 2, \tfrac12\log 2)$
   the prime terms of the Weil form $Q(g)$ vanish identically and $Q$ reduces to pole +
   archimedean terms — the regime of the proven archimedean positivity results (Yoshida;
   Connes–Consani). Reproduce the archimedean case self-containedly, with proofs, as this
   project's baseline.
2. **First widening.** Extend to the place set $\{\infty, 2\}$: support up to $\log 2$ brings
   in only the $p = 2$ terms — a self-contained, provable-or-refutable positivity problem.
3. Ladder bookkeeping: each further widening ($\{\infty, 2, 3\}, \dots$) is its own instance;
   **the full limit is RH (wall W6)** — the ladder is climbed for its unconditional rungs,
   never presented as approaching the top.

## Inputs

S00 §4.4 (explicit formula with verified regression instance); support bookkeeping: the prime
side involves $g \star \tilde g$, support twice that of $g$.

## Deliverable

Finding note per rung; tag targets **proven** (or a documented refutation of a rung, which
would be major and must survive adversarial + symbolic verification before being claimed).

## Falsifier

Each rung is intrinsically two-sided: positivity proven, or a violating $g$ exhibited. A
numerically-suggested violation is tagged **heuristic** until certified.
