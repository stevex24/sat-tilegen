# SAT for Tile Based Level Generation

Reproduction repository for experiments supporting the paper
**SAT for Tile Based Level Generation**.

This repository is a clean extraction of the experimental code from the
development repository. It is intended to contain only the code, inputs,
and configuration needed to reproduce results used in the paper.

## Experimental groups

### 1. WFC and WFC-as-SAT baselines

`experiments/baseline/`

Contains the experimental machinery for comparing traditional Wave Function
Collapse with the SAT formulation, including frequency-based tile selection.

Representative inputs include:

- Stick / Line
- Celtic Knot / Simple Knot
- Zelda

The Zelda weighted sweep provides the matched WFC versus WFC-as-SAT
frequency-based comparison.

### 2. Structural constraints

`experiments/structures/`

Contains experiments in which SAT constraints represent structures extending
across multiple tiles.

Examples include:

- Zelda multi-tile objects
- Tiny Town houses

### 3. Cardinality constraints

The Tiny Town experiment supports minimum, maximum, and exact house-count
constraints. Zelda structural experiments provide machinery for constraining
multi-tile objects.

### 4. Performance measurements

Execution-time, peak-memory, and backtracking/regeneration measurements will
be added to the reproduction workflow.

## Inputs

`examples/`

Contains the source examples required by the included experiments.

## Results

Generated experimental output is written under:

`results/`

Results are generated rather than treated as source code.

## Installation

Create and activate a Python virtual environment, then install:

    python -m pip install -r requirements.txt

The environment used while preparing this repository included:

- python-sat 1.9.dev5
- Pillow 11.3.0

## Reproduction status

The extracted modules currently pass an import smoke test.

Full reproduction of the numerical experimental results is the next
verification step. Until that verification is complete, this repository
should not be interpreted as independently validated reproduction of the
paper results.

## Provenance

The experimental implementation was extracted from the development repository:

    stevex24/wfc-to-sat

Historical commit and branch metadata retained inside experiment files refer
to that development repository and are preserved for provenance.
