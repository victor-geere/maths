---
title: Volumes & Surface Areas
tag: geometry
summary: Formulas for the volume enclosed by and the surface area bounding common three-dimensional solids.
links:
  - platonic-solids
  - eulers-polyhedra
---

# Volumes & Surface Areas

**Volume** measures the amount of three-dimensional space enclosed by a solid, and **surface area** measures the total area of its bounding faces or curved surface. These two quantities are fundamental in physics (buoyancy, heat transfer, capacity), engineering, and everyday calculation. For each solid, the formulas follow either from integration or from elegant decomposition arguments.

## Common Solids

### Cube (side $a$)
$$V = a^3, \qquad SA = 6a^2$$

### Rectangular Box (cuboid, sides $a, b, c$)
$$V = abc, \qquad SA = 2(ab + bc + ca)$$

### Prism (base area $B$, height $h$)
$$V = Bh, \qquad SA = 2B + Ph$$

where $P$ is the perimeter of the base.

### Cylinder (radius $r$, height $h$)
$$V = \pi r^2 h, \qquad SA = 2\pi r h + 2\pi r^2$$

### Cone (base radius $r$, height $h$, slant height $l = \sqrt{r^2 + h^2}$)
$$V = \frac{1}{3}\pi r^2 h, \qquad SA = \pi r l + \pi r^2$$

### Sphere (radius $r$)
$$V = \frac{4}{3}\pi r^3, \qquad SA = 4\pi r^2$$

### Pyramid (base area $B$, height $h$)
$$V = \frac{1}{3}Bh$$

## Cavalieri's Principle

Two solids have the same volume if every horizontal cross-section at the same height has the same area. This justifies the factor $\tfrac{1}{3}$ for cones and pyramids compared to their prism/cylinder counterparts.

## Scaling Laws

If all linear dimensions are scaled by factor $k$:
- Surface area scales by $k^2$
- Volume scales by $k^3$

This is why large animals have a smaller surface-area-to-volume ratio — with biological implications for heat loss and metabolic rate.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $V$ | volume |
| $SA$ | surface area |
| $r$ | radius |
| $h$ | height |
| $l$ | slant height of a cone or pyramid |
| $a, b, c$ | side lengths |
| $B$ | area of the base |
| $P$ | perimeter of the base |
| $\pi$ | pi ($\approx 3.14159$) |
| Prism | solid with two congruent parallel polygonal bases and rectangular lateral faces |
| Pyramid | solid with a polygonal base and triangular faces meeting at an apex |
| Cone | solid with a circular base tapering to a point (apex) |
| Sphere | set of all points at distance $r$ from a centre in 3D |
| Cavalieri's principle | equal cross-sectional areas at every height imply equal volumes |
| Slant height | distance from apex to a point on the base edge (along the lateral face) |
