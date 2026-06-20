# Ghost Numbers Verification Suite

This repository contains the high-performance computational verification engines accompanying the research paper: 
**"Ghost Numbers: Skipped Integers in the Factorial-Power Crossover"** (2026).

## Overview

A positive integer is classified as a **Ghost Number** if it represents an intrinsic "structural skip" or latency hidden within the discrete crossover thresholds between factorial growth and power sequences. This suite splits the verification architecture into two distinct number-theoretic classes:

1. **Alpha Ghosts ($\alpha_i$):** Integers skipped by the fixed-exponent crossover function:
   $$f_\alpha(k) = \min\{n \in \mathbb{N} : n! > n^k\}$$
2. **Beta Ghosts ($\beta_i$):** Integers skipped by the base-inversion crossover function:
   $$f_\beta(k) = \min\{n \in \mathbb{N} : n! > k^n\}$$

This suite serves to computationally validate the finite base cases, invariant linear bounds, and structural gap laws where continuous analytic limits are non-applicable.

---

## Repository Structure

```text
├── scripts/
│   ├── Alpha_Ghosts.py       # Computes fixed-exponent crossover gaps & validates Theorem 4.1 & 4.2
│   ├── Beta_Ghosts.py        # Computes base-inversion threshold drops & verifies e-convergence
│   └── verify_theorem_6_1.py # Validates fractional drift step deficits (\varepsilon_m) for small bounds
├── README.md
