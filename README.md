# Ghost Numbers Verification Suite

This repository contains the computational verification engines accompanying the research paper: 
**"Ghost numbers: integers skipped by the factorial-power crossover"** (2026).

## Overview
A positive integer $g$ is a **ghost number** if it is skipped by the factorial-power crossover function $C(k) = \min\{n : n! > n^k\}$. This suite provides the computational proofs for the finite base cases detailed in the paper, specifically verifying the bounds where analytic continuous limits do not apply.

## Repository Structure
* `scripts/Ghosts.py`: Core algorithm for generating sequences of ghost numbers and verifying the primary counting function $G(x)$ up to $x = 10^{12}$.
* `scripts/verify_theorem_6_1.py`: Validation script computing fractional drift step deficits ($\varepsilon_m$) for all non-trivial ghost numbers under $100$.

## Getting Started

### Prerequisites
* Python 3.8 or higher
* Standard library modules (`math`, `sys`)

### Running the Verification Scripts

To execute the core ghost number generation algorithm:
```bash
python scripts/Ghosts.py
```
To execute the Theorem 6.1 verification algorithm:
```bash
python scripts/Verify_Theorem_6_1.py
