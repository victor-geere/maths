# PSC2-001 — conventions: rigour tags, evidence hygiene, naming, declaration bar

*Governance document 001 of project PSC2. Binding on every file in this project.*

## 1. Naming and numbering

Project code **PSC2** (Prime Sieve Continued, plan 2). Every document is
`PSC2-<series><nn>-<slug>.md`:

| Series | Range | Content | Location |
|---|---|---|---|
| `0nn` | 000–009 | governance: charter, conventions | project root |
| `Snn` | S00–S99 | source documents: the standalone extraction of everything the charter builds on | `sources/` |
| `WPnn` | WP01–WP99 | work packages: one open problem each, with objective, inputs, method, falsifier, pre-registered criteria, status | `workpackages/` |
| `Nnn` | N00–N99 | numerics: verification targets and lab notes; runnable code lives beside them unprefixed | `numerics/` |
| `Fnn` | F00–F99 | findings: measured/proved results, one note per run or theorem, F00 is the template | `findings/` |

Cross-references use relative links. Status changes propagate **upward only**: a WP that lands
updates the charter's ledger; source documents are never edited to make a result look
stronger — corrections are appended with a dated notice, per the audit-trail convention.

## 2. Rigour tags (inherited unchanged; binding)

- **proven** — complete proof present in the note, or a classical result with citation.
- **conditional** — depends on RH or another named hypothesis; state it explicitly.
- **RH-equivalent** — proven *equivalent* to RH (Weil positivity, Connes' global trace
  formula, Hermite–Biehler positivity, …). These mark the **frontier**; an RH-equivalent
  restatement is not a step toward a proof and may never be presented as one.
- **heuristic/exploratory** — conjecture or numerical evidence only.
- **verified** — numerical agreement at stated precision against pre-registered criteria
  (not a substitute for proven).

Additional working tags used in this project: **open** (stated problem, no proof),
**dead end** (closed by proof or refutation; see [S06](sources/PSC2-S06-constraints-and-walls.md)
§3 — do not reopen), **wall** (RH-equivalent; priced, never scheduled).

## 3. Evidence hygiene (rule I0; binding on every experiment)

The seven rules of [S06 §5](sources/PSC2-S06-constraints-and-walls.md): no target-consuming
unfolding or normalisation; non-vacuity guards; correct loci; two-sided pre-registered
reporting; cross-checks against [N00](numerics/PSC2-N00-verification-targets.md); the
$\gamma$-list only in final evaluation; the sine decoy (S04 §5) on every new harness component.

## 4. Declaring RH proven

An unconditional proof of RH is a permitted outcome of this project — the door is open. It may
be claimed only at the full bar, which does not move:

- every link in the chain is itself tagged **proven** — nothing conditional, nothing
  heuristic, and no RH-equivalent restatement substituting for the conclusion;
- the chain terminates in a statement about the nontrivial zeros
  $\rho = \tfrac12 + i\gamma$ themselves, reached explicitly — not in kernel positivity,
  density/trace matching, or a singularity of the prime zeta;
- the argument survives independent verification — symbolic and numerical — and an
  adversarial read-through looking specifically for the gap;
- until all of the above hold, RH stays tagged **open**.

Do not present gate progress as "approaching RH". Partial results are stated as what they are
(expansion theorems, locus theorems, certified enclosures, zero-free-region equivalences).

## 5. Math rendering

Standard LaTeX (GitHub KaTeX). Use `\mathrm{}`, never `\operatorname{}`.
