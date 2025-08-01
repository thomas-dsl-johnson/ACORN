"""
This file finds the algorithms within the algorithms/ directory and makes a list.
"""
import os
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def is_algorithm(file_path: Path) -> bool:
    """Return True if the file is a .py algorithm and not generic or a __pycache__ item."""
    name = file_path.name
    return (
        file_path.suffix == ".py"
        and "generic" not in name.lower()
        and "__pycache__" not in file_path.parts
        and "end_to_end_result.py" != name.lower()
        and "causal_order_result.py" != name.lower()
    )

def find_non_generic_algorithms(base_dir: Path) -> list[Any]:
    """Recursively find all non-generic algorithm Python files."""
    return sorted([
        str(path.relative_to(base_dir))
        for path in base_dir.rglob("*.py")
        if is_algorithm(path)
    ])



if __name__ == "__main__":
    algorithms = find_non_generic_algorithms(PROJECT_ROOT / "algorithms")
    for algo in algorithms:
        print(algo)
    with open(PROJECT_ROOT / "algorithms" / "algorithm_list.txt", "w") as f:
        f.write("[")
        f.write(", ".join(map(str,algorithms)))
        f.write("]")
