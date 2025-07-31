"""
This module handles the storage of data from the results
"""
import pickle
import os
from typing import Any
OUTPUT_DIRECTORY = 'results'


def save(obj: Any, filename: str):
    """
    Save an object to a pickle file in the output directory.

    Parameters
    ----------
    obj : Any
        The Python object to be serialized and saved.
    filename : str
        The name of the file
    """
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    full_file_path = os.path.join(OUTPUT_DIRECTORY, filename + '.pkl')
    with open(full_file_path, 'wb') as file:
        pickle.dump(obj, file)
    return


def load(filename: str) -> Any:
    """
    Load a Python object from a pickle file in the output directory.

    Parameters
    ----------
    filename : str
        The name of the file to load (should match a file saved in the output directory).

    Returns
    -------
    obj : Any
        The Python object loaded from the pickle file.
    """
    full_file_path = os.path.join(OUTPUT_DIRECTORY, filename)
    with open(full_file_path, 'rb') as file:
        obj = pickle.load(file)
    return obj


def exists(filename: str):
    """
    Check if a file exists in the output directory.

    Parameters
    ----------
    filename : str
        The name of the file to check.

    Returns
    -------
    exists : bool
        True if the file exists, False otherwise.
    """
    full_file_path = os.path.join(OUTPUT_DIRECTORY, filename)
    return os.path.exists(full_file_path)

if __name__ == '__main__':
    x = load('/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_available/Causal_River/Flood/rivers_flood.p')
    print(x)
    print(type(x))
    print("Nodes:", x.nodes())
    print("Edges:", x.edges())
    print(x.number_of_nodes())