"""
Find the results within the algorithms/ directory and prints a summary of each one
"""
import sys
from pathlib import Path
from typing import Any, List

from algorithms.causal_order.causal_order_result import CausalOrderResult
from algorithms.end_to_end.end_to_end_result import EndToEndResult
from utils import storage

sys.path.append(str(Path(__file__).resolve().parents[1]))
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def find_result(base_dir: Path) -> list[str]:
    """Recursively find all non-generic algorithm Python files."""
    return sorted([
        str(path.relative_to(base_dir))
        for path in base_dir.rglob("*.pkl")
    ])

def get_all_results():
    results = find_result(PROJECT_ROOT / "results")
    ret = []
    for result in results:
        result_path = Path(result)
        # Check which directory it belongs to
        if "causal_order" in result_path.parts:
            res: CausalOrderResult = storage.load(result)
        elif "end_to_end" in result_path.parts:
            res: EndToEndResult = storage.load(result)
        else:
            raise Exception(f"Unknown result type {result_path}")
        ret.append(res)
    return ret

def print_all_results():
    all_results = get_all_results()
    print("\n\n".join(map(str,all_results)))

def get_results_for_dataset(dataset_name: str):
    results = find_result(PROJECT_ROOT / "results")
    ret = []
    for result in results:
        result_path = Path(result)
        # Check which directory it belongs to
        if "causal_order" in result_path.parts:
            res: CausalOrderResult = storage.load(result)
        elif "end_to_end" in result_path.parts:
            res: EndToEndResult = storage.load(result)
            res = res.causal_order_result
        else:
            raise Exception(f"Unknown result type {result_path}")
        if res.target_file != dataset_name:
            continue
        ret.append(res)
    return ret

def print_all_results_for_dataset(dataset_name: str):
    all_results = get_results_for_dataset(dataset_name)
    print("\n\n".join(map(str,all_results)))

if __name__ == "__main__":
    print_all_results()
    #print_all_results_for_dataset("/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/IT_monitoring/Antivirus_Activity/preprocessed_2.csv")