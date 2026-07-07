# PSC2-WP03 — the inclusion theorem (E2): unconditional convergence

*Status: **done — E2a delivered; E2b theorem proven; W1 instantiation in the falsifier
branch, quantified** (7 Jul 2026,
[PSC2-F09](../findings/PSC2-F09-inclusion-theorem.md)). E2a: the ambient record (normal
form $D = -i\,d/du$ on $L^2(\mathbb R, du)$, Mellin unitarity, $J$-parity, and the M4
four-ambient separation) is fixed once, every statement tagged. E2b: the route as worded
below needed repair — $P_n \to I$ strongly does **not** imply strong-resolvent
convergence of compressions (graph-norm control is the missing hypothesis; F09 Part II
Remark 1) — and the proven replacement is the **inclusion criterion** (graph-norm stage
density $\Rightarrow$ $r_n(\lambda) \to 0$ $\Rightarrow$ spectral inclusion,
quantitative), plus the honest s.r.c. version (Prop 2′), the finite-place prototype
realising the chain verbatim (S00 Prop 6.1(1)), and coarse inclusion on W1 with explicit
constants ($9.18/11.5$; no gap $> 18.4$ in the covered bulk). For W1 on fixed windows
the falsifier fired in quantified form: certified quasi-mode floors
$r_n \ge 0.73$ on $[0,50]$ at every fine-grid stage (grid minima $\approx 0.98$,
stage-stable), $\mathrm{dist}(\varphi_{\mathrm{far}}, V_n) = 1.0000$, and a permanent
spectral hole below $9.34$ — not a domain pathology but the wedge's fixed aperture (the
F08 fingerprint as an exact lower envelope). Per the falsifier text this constrains the
window design (prolate-pencil escalation stands pre-registered), not the theorem. The
script's mechanical branch rule returned INDETERMINATE via a disclosed
operationalisation artifact (vacuous $n=12$ coarse-grid Lipschitz margin); the $n=12$
fine-grid floor is filed via the labelled post-hoc supplement ($c_{12} = 0.7331$ —
floors certified at all five stages). **WP05 next**, its E4b
resolution budget now binding (F08 (a) + F09 (b)/(c)). Previously: **open — first in
line** (7 Jul 2026) — WP04 landed
([PSC2-F08](../findings/PSC2-F08-certified-enclosures.md): E3b gate passed; certified
radii saturate at a floor $\approx 1.72$ on $[0,50]$ — a resolution caveat this WP's E2b
core inherits as context), so per the charter ordering this WP now runs next, then WP05.
Previously: **open — reopened** (7 Jul 2026) — WP02b's rewindowed primary
$H^{G,\mathrm{w}}_n$ (W1 wedge builder) passed E0b
([PSC2-F07](../findings/PSC2-F07-density-rewindow.md)); per the pre-registration the E-track
pause is lifted, WP04 first in line. The concrete core for E2b is now the W1 family
(`numerics/wp02b_rewindow.py`). O6 caveat carried over: the E0b pass is not evidence about
zeros. Was: **paused** (6 Jul 2026, WP02 falsifier —
[PSC2-F02](../findings/PSC2-F02-density-gate.md)); before that **open** (unconditional
target). E2a (fixing the ambient) was window-independent throughout. Depends on: WP02b's
builder (for the concrete core).*

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
