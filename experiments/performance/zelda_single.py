#!/usr/bin/env python3
"""Run one Zelda generation for reproducible time/memory measurement."""

import argparse
import json

from experiments.baseline.core_experiment import run_sat, run_wfc
from experiments.baseline.zelda_experiment import sat_instance, tile_source
from wfc_to_sat.ordinary_wfc import WFCModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("wfc", "sat"), required=True)
    parser.add_argument("--heuristic", choices=("frequency", "context"), required=True)
    parser.add_argument("--seed", type=int, required=True)
    args = parser.parse_args()

    source, rgba = tile_source()
    model = WFCModel.from_tile_grid(source)

    if args.engine == "wfc":
        result = run_wfc(model, args.heuristic, args.seed)
    else:
        cnf, mapping, tile_for_id = sat_instance(model, rgba)
        result = run_sat(cnf, mapping, tile_for_id, args.heuristic, args.seed)

    keep = {
        "engine": result["engine"],
        "heuristic": args.heuristic,
        "seed": args.seed,
        "success": result["success"],
        "runtime_seconds": result["runtime_seconds"],
        "solve_seconds": result.get("solve_seconds"),
        "conflicts": result.get("conflicts"),
        "backtracks": result.get("backtracks"),
        "decisions": result.get("decisions"),
    }
    print(json.dumps(keep))


if __name__ == "__main__":
    main()
