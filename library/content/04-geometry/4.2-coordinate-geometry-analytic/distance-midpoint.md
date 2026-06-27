---
title: Distance & Midpoint
tag: geometry
summary: Formulas for the straight-line distance between two points and the point halfway between them.
links:
  - lines-plane
  - conic-sections
---

# Distance & Midpoint

The **distance formula** and **midpoint formula** are the two most basic measurements you can make between two points in the Cartesian plane. The distance formula is a direct consequence of the Pythagorean theorem — the straight-line (Euclidean) distance is the hypotenuse of a right triangle whose legs are the differences in coordinates. The midpoint is simply the average of each coordinate. Together they underpin the analytic treatment of all geometric figures.

## Distance Formula

The distance between points $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**In 3D** between $(x_1,y_1,z_1)$ and $(x_2,y_2,z_2)$:

$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$$

**In $n$ dimensions:**

$$d = \sqrt{\sum_{i=1}^n (b_i - a_i)^2}$$

## Midpoint Formula

The midpoint $M$ of segment $P_1 P_2$:

$$M = \left(\frac{x_1 + x_2}{2},\; \frac{y_1 + y_2}{2}\right)$$

In 3D: $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}, \frac{z_1+z_2}{2}\right)$.

## Section Formula (Dividing in Ratio $m:n$)

The point dividing $P_1 P_2$ in ratio $m:n$ internally:

$$P = \left(\frac{mx_2 + nx_1}{m+n},\; \frac{my_2 + ny_1}{m+n}\right)$$

Midpoint is the special case $m = n = 1$.

## Applications

- **Circle:** the set of all points at fixed distance $r$ from centre $(h,k)$: $(x-h)^2 + (y-k)^2 = r^2$.
- **Perpendicular bisector:** the locus of points equidistant from $P_1$ and $P_2$; passes through the midpoint with slope $-1/m_{P_1P_2}$.
- **Centroid of a triangle:** average of the three vertices' coordinates.

## Example

Distance from $A = (1, 2)$ to $B = (4, 6)$:

$$d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

Midpoint: $M = \left(\frac{5}{2}, 4\right)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $d$ | distance between two points |
| $(x_1,y_1)$, $(x_2,y_2)$ | coordinates of the two points |
| $M$ | midpoint |
| Euclidean distance | straight-line distance derived from Pythagoras' theorem |
| Midpoint | the point exactly halfway between two given points |
| Section formula | formula for the point dividing a segment in a given ratio |
| Perpendicular bisector | the line through the midpoint perpendicular to the segment |
| Centroid | average position of a set of points; for a triangle, average of the three vertices |
| Locus | the set of all points satisfying a given condition |
