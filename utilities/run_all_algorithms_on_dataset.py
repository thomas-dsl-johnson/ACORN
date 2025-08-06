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

def import_algorithm_class(file_path: Path):
    module_name = file_path.stem
    class_name = snake_to_pascal(module_name)

    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        cls = getattr(module, class_name, None)
        if cls and issubclass(cls, GenericAlgorithm):
            return cls
        else:
            print(f"Skipping {file_path.name} — class {class_name} not found or not a subclass of GenericAlgorithm.")
    return None

def run_all_algorithms(filepath):
    algorithm_list_path = PROJECT_ROOT / 'algorithms' / 'algorithm_list.txt'
    with open(algorithm_list_path, 'r') as f:
        content = f.read()

    content = content.strip().strip("[]")
    raw_paths = [x.strip().strip('"').strip("'") for x in content.split(',') if x.strip()]
    algorithm_paths = [PROJECT_ROOT / "algorithms" / p for p in raw_paths]

    for file in algorithm_paths:
        if not file.exists():
            print(f"File not found: {file}")
            continue

        algo_cls = import_algorithm_class(file)
        if algo_cls:
            instance = algo_cls()
            print(f"\nRunning {algo_cls.__name__} from {file.name}")
            instance._get_and_save_result(filepath)

if __name__ == "__main__":
    #filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/sp500_5_columns/sp500_5_columns.xlsx"
    filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/sp500/sp500.csv"
    run_all_algorithms(filepath)
