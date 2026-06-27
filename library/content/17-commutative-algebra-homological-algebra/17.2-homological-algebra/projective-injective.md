---
title: Projective & Injective Modules
tag: homological-algebra
summary: Projective modules are direct summands of free modules and make Hom exact from the left; injective modules make Hom exact from the right; together they are the building blocks of resolutions and derived functors.
links:
  - modules
  - exact-sequences
  - free-resolutions
  - ext-tor
  - derived-functors
---

# Projective & Injective Modules

**Projective** and **injective** modules are the two key classes of modules that control exactness of the $\mathrm{Hom}$ functor. A module $P$ is **projective** if $\mathrm{Hom}_R(P, -)$ is exact, equivalently if $P$ is a direct summand of a free module. A module $I$ is **injective** if $\mathrm{Hom}_R(-, I)$ is exact, equivalently if $I$ satisfies Baer's criterion (every homomorphism from an ideal extends to the whole ring). These two classes are dual to each other (in the categorical sense), and every module can be approximated from above by injectives and from below by projectives — these approximations are **resolutions**, the raw material for computing derived functors $\mathrm{Ext}$ and $\mathrm{Tor}$.

## Projective Modules

$P$ is **projective** if any of the following equivalent conditions hold:
1. $\mathrm{Hom}_R(P, -)$ is exact (preserves surjections).
2. Every surjection $M \twoheadrightarrow P$ splits.
3. $P$ is a direct summand of a free module: $P \oplus Q \cong R^n$.
4. Lifting property: for any surjection $f: M \to N$ and map $g: P \to N$, there is $\tilde{g}: P \to M$ with $f \circ \tilde{g} = g$.

## Injective Modules

$I$ is **injective** if any of the following equivalent conditions hold:
1. $\mathrm{Hom}_R(-, I)$ is exact (preserves injections).
2. Every injection $I \hookrightarrow M$ splits.
3. **Baer's criterion**: every $f: J \to I$ from an ideal $J \subseteq R$ extends to $R \to I$.
4. Extension property: for any injection $i: A \hookrightarrow B$ and map $f: A \to I$, there is $\tilde{f}: B \to I$ with $\tilde{f} \circ i = f$.

## Injective Envelopes

Every module $M$ has an **injective envelope** (or essential injective extension) $E(M)$: an injective module $I$ with $M \hookrightarrow I$ an essential extension (every non-zero submodule of $I$ meets $M$).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Projective module $P$ | $\mathrm{Hom}(P,-)$ exact; direct summand of free module |
| Injective module $I$ | $\mathrm{Hom}(-,I)$ exact; satisfies Baer's criterion |
| Lifting property | maps from $P$ lift through surjections |
| Extension property | maps into $I$ extend through injections |
| Baer's criterion | injectivity tested by extending maps from ideals |
| Split exact sequence | $0 \to A \to B \to C \to 0$ splits if $C$ projective or $A$ injective |
| Injective envelope $E(M)$ | smallest injective extension of $M$ |
| Free module | $R^n$; every projective is a summand of one |
| $\mathrm{Ext}^1(M,N)$ | classifies extensions; zero iff $M$ projective or $N$ injective |
