"""
This file finds the algorithms within the algorithms/ directory and makes a list.
The output is written to the algorithms/ directory in algorithm_list.txt
"""
import os
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
"""
This file finds the algorithms within the algorithms/ directory and makes a list.
The output is written to the algorithms/ directory in algorithm_list.txt
"""
import os
from pathlib import Path
from typing import List

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ALGORITHMS_DIR = PROJECT_ROOT / "algorithms"

def is_algorithm(file_path: Path) -> bool:
    """Return True if the file is a .py algorithm and not generic or a __pycache__ item."""
    name = file_path.name
    return (
        file_path.suffix == ".py"
        and "generic" not in name.lower()
        and "__init__" not in name.lower()
        and "__pycache__" not in file_path.parts
        and name.lower() not in {"end_to_end_result.py", "causal_order_result.py"}
    )

def path_to_module(path: Path) -> str:
    """Convert a Path like algorithms/x/y/z.py to a Python module path: algorithms.x.y.z"""
    return ".".join(path.with_suffix("").parts)

def find_algorithm_modules(base_dir: Path) -> List[str]:
    """Recursively find all non-generic algorithm Python files and return as importable module paths."""
    return sorted([
        path_to_module(path.relative_to(PROJECT_ROOT))
        for path in base_dir.rglob("*.py")
        if is_algorithm(path)
    ])

if __name__ == "__main__":
    module_paths = find_algorithm_modules(ALGORITHMS_DIR)

    for module in module_paths:
        print(module)

    output_file = ALGORITHMS_DIR / "algorithm_list.txt"
    with open(output_file, "w") as f:
        f.write("[\n")
        for module in module_paths:
            f.write(f'    "{module}",\n')
        f.write("]\n")

