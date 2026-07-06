# PSC2-WP03 — the inclusion theorem (E2): unconditional convergence

*Status: **open** (unconditional target). Depends on: WP02's builder (for the concrete core).*

## Objective

- **E2a (the ambient, fixed once).** State rigorously the space on which the target $D$ acts
  (Hilbert $L^2(X)$-with-regularisation vs Meyer nuclear ambient) and record, with tags, what
  is proven about $\mathrm{spec}(D)$ there — the M4 correction
  ([S06](../sources/PSC2-S06-constraints-and-walls.md) §2.5) done properly so no later step
  can equivocate. Overlaps the "rigorous adelic operator" item (charter H9).
- **E2b (inclusion).** Prove $P_n \to I$ strongly on an explicit core of $D$ (Schwartz-type
  spherical vectors), hence $H^G_n \to D$ in the strong-resolvent sense, hence **spectral
  inclusion**: every point of $\mathrm{spec}(D)$ is a limit of stage eigenvalues — *no zero
  is missed*.

## Honest payoff statement (binding)

E2 can never certify an eigenvalue *is* near a zero (K2 pollution,
[S03](../sources/PSC2-S03-eigenvalue-level.md) §2); it certifies none are missing. Claims are
limited accordingly.

## Method

Named-theorem route: Reed–Simon VIII; Weidmann's compression conditions. The finite-place
core is explicit (finitely supported vectors on the prime-power inventory, cf. the proven
prototype in [S00](../sources/PSC2-S00-verified-foundation.md) §5 Prop 6.1(1)); the archimedean
core needs the window's dilation structure.

## Deliverable

Finding note with the E2a ambient record (every statement tagged) and the E2b theorem,
tag target **proven**.

## Falsifier / risk

If the $J$-invariant window of WP02 is incompatible with a common core (domain pathology),
document; that constrains the window design, not the theorem's ambition.
