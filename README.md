# Ghost Numbers Verification Suite

This repository contains the computational verification engines accompanying the research paper: 
**"Ghost Numbers: Skipped Integers in the Factorial-Power Crossover"** (2026).

## Overview
This suite provides the computational verification tools and high-performance generation engines for two distinct classes of latent integers arising from factorial-power crossovers:

* **Alpha Ghosts:** Non-trivial integers skipped by the original crossover sequence defined by $min(n : n! > n^k)$.
* **Beta Ghosts:** Non-trivial integers skipped by the new inverse threshold crossover sequence defined by $min(n : n! > k^n)$.

The scripts evaluate finite base cases, track geometric gap transitions, and compute convergence ratios where analytic continuous limits do not apply.

## Repository Structure
* `Alpha_Ghosts.py`: High-performance engine evaluating the original $min(n : n! > n^k)$ sequence, verifying the Linear Invariant Property and recording gap milestones.
* `Beta_Ghosts.py`: High-performance engine evaluating the new $min(n : n! > k^n)$ sequence, using un-accumulated log-gamma calculations to track base crossover shifts and milestone ratios.
* `verify_theorem_6_1.py`: Validation script computing fractional drift step deficits ($\varepsilon_m$) for all non-trivial ghost numbers under 100.

## Pre-computed Datasets (Zenodo)
For high-limit evaluations ($k \ge 100,000$), the pre-computed data output matrices are available directly via Zenodo if you prefer not to run the computation loops locally:

* **Alpha Ghosts Dataset:** [Zenodo Link Pending]
* **Beta Ghosts Dataset:** [Zenodo Link Pending]

## Getting Started

### Prerequisites
* Python 3.8 or higher
* Standard library modules (`math`, `sys`)

### Running the Verification Scripts

```bash
# Run Alpha Ghosts analysis
python Alpha_Ghosts.py

# Run Beta Ghosts analysis
python Beta_Ghosts.py

# Run fractional drift verification
python verify_theorem_6_1.py
