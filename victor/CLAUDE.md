# CLAUDE.md — victor/

Folder-specific guidance for `victor/`. Rigour tags, the RH declaration bar, and math-rendering
convention are defined once in the root [CLAUDE.md](../CLAUDE.md) and bind here unchanged.

## Repository structure

```
victor/
  research/               # Current research track.
                          # PSC2 ("Prime Sieve Continued, plan 2") — a further standalone offshoot
                          # extracted from prime-sieve-continued/ on 2026-07-06; read research/README.md
                          # (its charter) first. 
                          # is the track-1 circle-kernel catalogue (see research/CLAUDE.md at repo root)
  notes/                  # (empty — scratch space)
  berry-keating/          # Hilbert–Pólya "prime side" track (see §Two tracks below)
  adele/                  # Prime sieve on the adèle class space (Connes trace formula)
  flawed/                 # graveyard: discarded RH-proof attempts, kept as an audit trail
  prime-generator/        # small exploratory HTML visualisations (dyadic sieve, FFT explanation)
  prime-sieve/            # pre-fork source for the Ihara/graph-determinant lab (see prime-sieve-continued/)
  prime-sieve-continued/  # standalone forked snapshot of the adèle/berry-keating/flawed track,
```

### Declaring RH proven

An unconditional proof of RH **is a permitted outcome of this project** — the door is open. But it may be claimed only at the full bar, and the bar does not move:

- every link in the chain is itself tagged **proven** — nothing **conditional**, nothing **heuristic**, and no **RH-equivalent** restatement substituting for the conclusion;
- the chain terminates in a statement about the nontrivial zeros $\rho=\tfrac12+i\gamma$ themselves (their location), reached explicitly — not merely in positivity of a kernel, a singularity of the prime zeta, or the density/trace matching;
- the argument survives independent verification — symbolic (via the `sympy-verifier` MCP server) and numerical — and an adversarial read-through looking specifically for the gap (that is how the `flawed/` series was caught);
- until all of the above hold, RH stays tagged **open**, exactly as every current note states it is.

This convention *opens the door to a proof; it does not lower the threshold for claiming one.* If a genuine proof is assembled, say so plainly and unhedged (see the harness rule on reporting outcomes faithfully); short of that, do not hint that the project is "close."