"""
A set of functions that compare two Causal Order Results
"""
import os
from pathlib import Path
from algorithms.causal_order.generic_causal_order_algorithm import CausalOrder
from algorithms.end_to_end.end_to_end_result import EndToEndResult
from algorithms.end_to_end.original.direct_lingam_end_to_end_algorithm import DirectLingamEndToEndAlgorithm
from utilities import storage

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def get_ground_truth_causal_order(filepath: str) -> (CausalOrder, bool):
    data_path = Path(filepath)
    if "ground_truth_available" in data_path.parts:
        # Ground truth exists
        # Retrieve ground truth from same folder as dataset
        causal_order_path = data_path.parent / "causal_order.txt"
        if not causal_order_path.exists():
            raise FileNotFoundError(f"No causal_order.txt found at {causal_order_path}")
        with open(causal_order_path, "r") as f:
            line = f.readline().strip("[]").split(",")
            causal_order_list = [int(x) for x in line]
        return causal_order_list, True
    elif "ground_truth_not_available" in data_path.parts:
        # No ground truth
        # Retrieve 'ground truth' from DirLingam EndtoEnd result
        result_path = "end_to_end" + "/" + DirectLingamEndToEndAlgorithm().__str__() + "/" + os.path.splitext(os.path.basename(filepath))[0] + ".pkl"
        if storage.exists(result_path):
            res: EndToEndResult = storage.load(result_path)
            return res, False
        else:
            raise FileNotFoundError(f"No file found at {result_path}")
    else:
        raise Exception(f"Unknown result type {data_path}")

if __name__ == "__main__":
    ground_truth_causal_order, isRealTruth = get_ground_truth_causal_order("/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/sp500_5_columns/sp500_5_columns.xlsx")
    print(ground_truth_causal_order, isRealTruth)