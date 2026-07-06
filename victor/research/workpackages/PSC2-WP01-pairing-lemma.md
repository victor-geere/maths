# PSC2-WP01 — the pairing lemma (E1) and the pairing-unification claim (HS5)

*Status: **open** (proof expected routine — days). Priority: first; WP02 depends on it.*

## Objective

**(a) E1.** Prove: if $V_n = \mathrm{ran}\,P_n$ is $J$-invariant ($J$ the functional-equation
unitary, $JDJ^{-1} = -D$), then $\mathrm{spec}(H^G_n) = -\mathrm{spec}(H^G_n)$ with paired
eigenvectors — the stage-exact $\pm\gamma$ avatar. One page; the bipartite/chiral mechanism
(F3, [S02](../sources/PSC2-S02-determinant-level.md) §6) is the model.

**(b) HS5.** Prove: for any $\pm$-paired stage spectrum, the stage canonical product
$\Xi_n(t) = \Xi(0)\prod(1 - t^2/\lambda_k^2)$ is even and exponential-factor free, and
evenness in $t$ is exactly the stage functional equation $s \leftrightarrow 1 - s$.
Consequence to record: gate E1, design law C-2 (F6), and H\*-d are one constraint at two
levels ([S04](../sources/PSC2-S04-model-pair.md) §4).

## Inputs

[S03](../sources/PSC2-S03-eigenvalue-level.md) §1, §3(c); [S04](../sources/PSC2-S04-model-pair.md)
§1, §4; [S02](../sources/PSC2-S02-determinant-level.md) §6 (F3 mechanism).

## Deliverable

Finding note with both proofs, tag **proven**; the HS5 consequence propagated to WP12's
family definition (paired spectra, even products — replacing the kernel-schematic V2 form).

## Falsifier / risk

None expected for (a) — it is linear algebra once $J V_n = V_n$ is arranged; the real content
is *constructing* a $J$-invariant basis, which is WP02's N0 builder. If a $J$-invariant basis
compatible with the sieve inventory cannot be exhibited, that is the reportable obstruction
(and blocks E1 *by construction*, downgrading the pairing to asymptotic — record and stop).

## Pricing

Below the wall; pure construction + bookkeeping. No target data consumed.
