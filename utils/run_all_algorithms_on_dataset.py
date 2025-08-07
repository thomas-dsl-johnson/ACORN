"""
When __name__ == '__main__':
    - Run the ._get_and_save_result() method of all algorithms on the selected dataset
    - Each algorithm must be in Pascal case to match its Snake case filename
"""
import importlib.util
from algorithms.generic_algorithm import GenericAlgorithm
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def snake_to_pascal(snake: str) -> str:
    return ''.join(word.capitalize() for word in snake.replace(".py", "").split('_'))

def import_algorithm_class(module_path: Path):
    try:
        module = importlib.import_module(module_path)
        class_name = snake_to_pascal(module_path.split('.')[-1])
        cls = getattr(module, class_name, None)
        if cls and issubclass(cls, GenericAlgorithm):
            return cls
        else:
            print(f"Skipping {module_path} — class {class_name} not found or not a subclass of GenericAlgorithm.")
    except Exception as e:
        print(f"Error importing {module_path}: {e}")
    return None

def run_all_algorithms(filepath):
    algorithm_list_path = PROJECT_ROOT / 'algorithms' / 'algorithm_list.txt'
    with open(algorithm_list_path, 'r') as f:
        content = f.read()

    content = content.strip().strip("[]")
    module_paths = [x.strip().strip('"').strip("'") for x in content.split(',') if x.strip()]

    for module_path in module_paths:
        algo_cls = import_algorithm_class(module_path)
        if algo_cls:
            instance = algo_cls()
            print(f"\nRunning {algo_cls.__name__} from {module_path}")
            instance._get_and_save_result(filepath)

if __name__ == "__main__":
    from algorithms.causal_order.new.para_lingam_causal_order_algorithm import ParaLingamCausalOrderAlgorithm
    #filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/S&P500/sp500_5_columns/sp500_5_columns.xlsx"
    #filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/S&P500/sp500/sp500.csv"
    #filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/IT_monitoring/Antivirus_Activity/preprocessed_2.csv"
    #filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/IT_monitoring/Middleware_oriented_message_Activity/monitoring_metrics_2.csv"
    # filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/IT_monitoring/Storm_Ingestion_Activity/storm_data_normal.csv"
    # filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/IT_monitoring/Web_Activity/preprocessed_2.csv"
    # filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/Causal_River/Bavaria/rivers_ts_bavaria_preprocessed.csv"
    # filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/Causal_River/East Germany/rivers_ts_east_germany_preprocessed.csv"
    filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/Causal_River/Flood/rivers_ts_flood_preprocessed.csv"
    run_all_algorithms(filepath)
