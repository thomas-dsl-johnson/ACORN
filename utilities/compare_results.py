"""
A set of functions that compare two results
"""
import os
import numpy as np
from pathlib import Path

from algorithms.causal_order.causal_order_result import CausalOrderResult
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
            return res.causal_order_result.causal_order, False
        else:
            raise FileNotFoundError(f"No file found at {result_path}")
    else:
        raise Exception(f"Unknown result type {data_path}")

def get_ground_truth_summary_matrix(filepath: str) -> (CausalOrder, bool):
    data_path = Path(filepath)
    if "ground_truth_available" in data_path.parts:
        # Ground truth exists
        # Retrieve ground truth from same folder as dataset
        summary_matrix_path = data_path.parent / "summary_matrix.npy"
        if not summary_matrix_path.exists():
            raise FileNotFoundError(f"No summary_matrix.npy found at {summary_matrix_path}")
        summary_matrix = np.load(summary_matrix_path)
        return summary_matrix, True
    elif "ground_truth_not_available" in data_path.parts:
        # No ground truth
        # Retrieve 'ground truth' from DirLingam EndtoEnd result
        result_path = "end_to_end" + "/" + DirectLingamEndToEndAlgorithm().__str__() + "/" + os.path.splitext(os.path.basename(filepath))[0] + ".pkl"
        if storage.exists(result_path):
            res: EndToEndResult = storage.load(result_path)
            return res.summary_matrix, False
        else:
            raise FileNotFoundError(f"No file found at {result_path}")
    else:
        raise Exception(f"Unknown result type {data_path}")


def get_result_file_causal_order(dataset_path: str, algorithm_name: str) -> CausalOrder:
    dataset_path = Path(dataset_path)
    dataset_filename = dataset_path.stem + ".pkl"

    # Extract the relative path from the dataset root
    try:
        relative_path = dataset_path.relative_to(PROJECT_ROOT / "data")
    except ValueError:
        raise ValueError(f"Dataset path {dataset_path} is not under the expected 'data' directory.")

    # Drop the first component (e.g., "ground_truth_available")
    parts = list(relative_path.parts)[1:-1]  # Skip file name and root folder
    subdir = Path(*parts) if parts else Path() # Maybe change file structure later

    # Full result path
    result_file_path = PROJECT_ROOT / "results" / "causal_order" / algorithm_name / dataset_filename
    causal_order_result : CausalOrderResult = storage.load(str(result_file_path))
    return causal_order_result.causal_order

def count_inverted_pairs(discovered_causal_order: CausalOrder, ground_truth_matrix: np.ndarray) -> float:
        def correct_in_causal_order(order, j, i):
            return order.index(j) < order.index(i)

        total_number_of_pairs = len(discovered_causal_order) * (len(discovered_causal_order) - 1)
        inverted_pairs = 0
        A = ground_truth_matrix
        n = len(A)
        for i in range(0, n):
            for j in range(0, n):
                x = A[i, j]
                if x != 0:  # j -> i
                    if not correct_in_causal_order(discovered_causal_order, j, i):
                        inverted_pairs += 1
        return inverted_pairs / total_number_of_pairs



if __name__ == "__main__":
    dataset = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/sp500_5_columns/sp500_5_columns.xlsx"
    # dataset = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/sp500_5_columns/sp500_5_columns.xlsx"
    ground_truth_causal_order, isRealTruth = get_ground_truth_causal_order(dataset)
    ground_truth_summary_matrix, _ = get_ground_truth_summary_matrix(dataset)
    print(ground_truth_causal_order, isRealTruth)
    print(ground_truth_summary_matrix)
    algorithm_name = "DirectLingamAlgorithmAddingNodesInBatchesOfTwo"
    found_causal_order = get_result_file_causal_order(dataset, algorithm_name)
    if isRealTruth:

    else:
        print("Ratio of inverted pairs: ", count_inverted_pairs(found_causal_order, ground_truth_summary_matrix))