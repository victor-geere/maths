# PSC2-S01 — the character level (L2): the flow character and the circularity theorem

*Source document S01. Extracted from `prime-sieve-continued/adele/phase7.md` and
`berry-keating/prime-side.md` (Thm 5.3, Cor 5.4). This level sits between the proven trace
level (L1, [PSC2-S00](PSC2-S00-verified-foundation.md) §4–6) and the open determinant level
(L3, [PSC2-S02](PSC2-S02-determinant-level.md)). Its two results below are the folder's
sharpest statements of **where the zeros actually live** in the sieve's data — and why reaching
them costs an analytic continuation that is itself the Weil explicit formula.*

---

## 1. The flow character — proven

**Theorem 1.1 (weighted flow character; prime-side.md Thm 5.3). — proven.**
With $(\mathbb A, \mathbb W)$ the prime-side package of S00 §4.3 (generator with spectrum
$\{\pm k\log p\}$, von Mangoldt weights), the weighted character of the translation flow is

$$\chi_W(z) \;=\; \mathrm{Tr}\big(W e^{izA}\big) \;=\; \sum_{q \in \mathcal Q}\Lambda(q)\,q^{-\frac12+iz}
\;=\; -\frac{\zeta'}{\zeta}\Big(\frac12 - iz\Big),$$

absolutely convergent and holomorphic on $\{\mathrm{Im}\,z > \tfrac12\}$. Its meromorphic
continuation has simple poles **exactly at the zeros**, at
$z_\rho = -\gamma_\rho + i(\beta_\rho - \tfrac12)$, plus $z = \tfrac{i}{2}$ (from $\zeta$'s
pole) and the trivial-zero poles.

**Reading.** $\chi_W$ is a trace of the sieve's own data. The zeros are *not present* where the
trace converges; they appear only after continuation across $\mathrm{Im}\,z = \tfrac12$.

## 2. One function, one operation — proven

**Observation 2.1 (phase7 Obs 7.1; re-expression of the explicit formula). — proven.**
For admissible even $h$, the Guinand–Weil explicit formula (S00 §4.4 Fact 4.1) is precisely the
residue calculus of $h(z)\,\chi_W(z)$:

- pairing $h$ against $\chi_W$ on $\{\mathrm{Im}\,z > \tfrac12\}$ (where the series converges)
  yields the **prime side** $\mathrm{Tr}(\mathbb W^{1/2}g(\mathbb A)\mathbb W^{1/2})$;
- shifting the contour across $\mathrm{Im}\,z = \tfrac12$ collects the residues: the pole term
  $h(\tfrac i2) + h(-\tfrac i2)$, the **zero side** $-\sum_\rho h(\gamma_\rho)$, and the
  archimedean/$\Gamma$ terms.

Equating the two evaluations of the same integral **is** the explicit formula.

## 3. The circularity theorem — proven; binding on every plan item

Any proposal of the shape "(a) let the sieve connect primes to zeros, then (b) use Weil to
prove the two sides equal" fails as follows (phase7 §7.4):

- the sieve delivers $\chi_W$ only on $\mathrm{Im}\,z > \tfrac12$, where the zeros are absent;
- the only operation producing the zeros from $\chi_W$ is the continuation across
  $\mathrm{Im}\,z = \tfrac12$ — which *is* step (b).

Step (a) does not exist independently of step (b): the loop has unit length and returns the
explicit formula, which holds **whether or not the zeros lie on the line** — hence zero
information about $\{\beta_\rho\}$.

## 4. What the zero side genuinely needs — proven equivalences (walls)

For "zero side $=$ prime side" to constrain zero *locations*, the zero side must carry a
structural constraint forcing every zero-pole $z_\rho$ of $\chi_W$ to be real. The three known
ways, **all proven RH-equivalent** (see [PSC2-S06](PSC2-S06-constraints-and-walls.md) §4):

| Extra structure | Forces | Status |
|---|---|---|
| self-adjoint $H$ on a *new* Hilbert space, $\sigma(H) = \{\gamma_\rho\}$, $Z(h) = \mathrm{Tr}\,h(H)$ | real spectrum $\Rightarrow \beta_\rho = \tfrac12$ | **RH-equivalent**; by rigidity (S00 §5, Prop 3.7) the space cannot be the prime side re-coordinatised |
| Weil positivity $\sum_\rho h(\gamma_\rho) \ge 0$ for $h = \lvert\widehat\phi\rvert^2$-type | poles real | **RH-equivalent** |
| de Branges / Hermite–Biehler structure function for $\xi$ | zeros on the line | **RH-equivalent** |

**Corollary 4.1 (prime-side translation; prime-side.md Cor 5.4). — proven equivalence,
RH-equivalent.** RH $\iff$ $\chi_W$ continues holomorphically to
$\{\mathrm{Im}\,z > 0\}\setminus\{\tfrac i2\}$ $\iff$ every zero-pole $z_\rho$ is real.
A pure regularity statement about the already-constructed $\chi_W$ — a *restatement* of RH,
not a reduction.

---

**Use in the charter.** This document is the proof that L2 is a *closed* level: everything
provable there is proven, and everything beyond is a wall. All open work in PSC2 therefore
lives at L3 (determinant) and L4 (eigenvalue), with L1/L2 as anchors and regression targets.
