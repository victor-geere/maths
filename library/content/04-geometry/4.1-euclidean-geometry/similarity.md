---
title: Similarity & Ratios
tag: geometry
summary: Two figures are similar when they have the same shape but possibly different sizes; corresponding lengths scale by a constant ratio.
links:
  - triangles-congruence
  - angles-parallel-lines
  - conic-sections
---

# Similarity & Ratios

**Similarity** generalises congruence: two figures are similar if one can be obtained from the other by a combination of rotation, reflection, translation, and **scaling**. Similar figures have the same shape but may differ in size. The ratio by which all lengths scale is the **scale factor**, and it is the same for every pair of corresponding lengths. Similarity is pervasive in geometry, trigonometry, and the analysis of proportional relationships.

## Similar Triangles

$\triangle ABC \sim \triangle DEF$ if corresponding angles are equal and corresponding sides are proportional:

$$\angle A = \angle D, \quad \angle B = \angle E, \quad \angle C = \angle F$$
$$\frac{AB}{DE} = \frac{BC}{EF} = \frac{CA}{FD} = k \quad \text{(scale factor)}$$

## Similarity Criteria

| Criterion | Conditions |
|---|---|
| **AA** | Two pairs of equal angles (third follows since angle sum = $180°$) |
| **SAS~** | Two sides proportional and the included angle equal |
| **SSS~** | All three pairs of sides proportional |

AA is the most frequently used: if two angles match, the triangles are similar.

## Ratios of Areas and Volumes

If two similar figures have scale factor $k$:
- Corresponding **lengths** scale by $k$
- Corresponding **areas** scale by $k^2$
- Corresponding **volumes** scale by $k^3$

## The Basic Proportionality Theorem (Thales)

If a line is drawn parallel to one side of a triangle and intersects the other two sides, it divides those sides in equal ratios:

$$\frac{AD}{DB} = \frac{AE}{EC}$$

This is equivalent to the AA similarity of the smaller and larger triangles.

## Applications

- **Trigonometry:** ratios $\sin\theta$, $\cos\theta$, $\tan\theta$ are defined via similar right triangles — they depend only on the angle, not the size.
- **Shadow problems:** height of an object from its shadow length using similar triangles.
- **Map scales:** a 1:50,000 map uses scale factor $k = 1/50000$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\sim$ | similar to |
| $k$ | scale factor (ratio of corresponding lengths) |
| $\triangle ABC \sim \triangle DEF$ | triangles $ABC$ and $DEF$ are similar |
| AA | Angle-Angle similarity criterion |
| SAS~ | Side-Angle-Side similarity criterion |
| SSS~ | Side-Side-Side similarity criterion |
| Corresponding sides | sides in the same relative position in two similar figures |
| Proportional | quantities whose ratios are equal |
| Scale factor | the constant ratio $k$ by which all lengths multiply |
| Thales' theorem | a line parallel to one side of a triangle divides the other two sides proportionally |
