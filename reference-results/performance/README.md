# Performance reference results

These are small reproducibility measurements for the paper experiments, not
large-scale performance benchmarks.

## Zelda 20x20

Five fixed seeds (0-4) were run for each combination of ordinary WFC and
WFC-as-SAT with frequency and context tile-selection heuristics.

Generation runtime is measured internally by the established experiment code.
Peak RSS is measured by macOS `/usr/bin/time -l` around a fresh Python process
for each individual generation. Peak RSS therefore represents whole-process
memory, including Python, model setup, and, for WFC-as-SAT, SAT formula
construction. It must not be interpreted as solver-only memory.

Observed means:

| Heuristic | Engine | Mean runtime | Mean peak RSS |
| --- | --- | ---: | ---: |
| frequency | ordinary WFC | 0.222 s | 55.3 MiB |
| frequency | WFC-as-SAT | 0.922 s | 518.2 MiB |
| context | ordinary WFC | 0.222 s | 55.3 MiB |
| context | WFC-as-SAT | 0.871 s | 476.6 MiB |

Frequency SAT peak RSS ranged from 476.4 to 546.5 MiB; context SAT ranged
from 476.5 to 477.1 MiB. Because this is only a five-seed reproducibility
sample, these measurements should not be treated as a scaling study.

## Tiny Town structural/cardinality example

The verified 12x10 Tiny Town example with exactly three houses, seed 4, took
0.72 s wall-clock and had a whole-process maximum RSS of 200,196,096 bytes
(about 190.9 MiB) under macOS `/usr/bin/time -l`.

These Tiny Town numbers are a single representative structural/cardinality
run, not an ordinary-WFC versus SAT comparison.
