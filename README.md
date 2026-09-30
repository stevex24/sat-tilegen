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

The repository includes a fresh-process Zelda performance runner in
`experiments/performance/zelda_single.py`.

For the representative 20x20 Zelda experiment, fixed seeds 0-4 were measured
for ordinary WFC and WFC-as-SAT using both frequency and context heuristics.
Generation runtime comes from the established experiment code. Peak RSS is
measured around a fresh Python process for each generation, so it is a
whole-process measurement rather than solver-only memory.

The small reference measurement and methodology are recorded in
`reference-results/performance/`. Backtracking/conflict statistics are emitted
by the baseline experiment code.

A representative Tiny Town 12x10 run with exactly three houses was also
measured as a structural/cardinality example.

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

The clean-repository workflow has been verified on the extracted repository.

Verification included the Stick quick experiment, the baseline benchmark,
the Zelda 1x1 experiment, the matched Zelda weighted comparison for seeds
0-4, the Zelda structural demonstrations, and the Tiny Town exact-three-house
experiment.

A five-seed fresh-process performance sample was also run for Zelda using
ordinary WFC and WFC-as-SAT with frequency and context heuristics. Compact
reference results and the measurement methodology are stored under
`reference-results/performance/`.

Generated experimental output remains excluded from version control and can
be regenerated from the included code and inputs.

## Provenance

The experimental implementation was extracted from the development repository:

    stevex24/wfc-to-sat

Historical commit and branch metadata retained inside experiment files refer
to that development repository and are preserved for provenance.
