"""
Find the results within the algorithms/ directory and prints a summary of each one
"""
import sys
from pathlib import Path
from typing import Any, List

from algorithms.causal_order.causal_order_result import CausalOrderResult
from algorithms.end_to_end.end_to_end_result import EndToEndResult
from utilities import storage

sys.path.append(str(Path(__file__).resolve().parents[1]))
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def find_result(base_dir: Path) -> list[str]:
    """Recursively find all non-generic algorithm Python files."""
    return sorted([
        str(path.relative_to(base_dir))
        for path in base_dir.rglob("*.pkl")
    ])



if __name__ == "__main__":
    results = find_result(PROJECT_ROOT / "results")
    for result in results:
        result_path = Path(result)
        # Check which directory it belongs to
        if "causal_order" in result_path.parts:
            res : CausalOrderResult = storage.load(result)
        elif "end_to_end" in result_path.parts:
            res: EndToEndResult = storage.load(result)
        else:
            raise Exception(f"Unknown result type {result_path}")
        print("\n")
        print(res)
