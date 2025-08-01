from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    algorithm_filenames = PROJECT_ROOT / 'algorithms' / 'algorithm_list.txt'
    with open(algorithm_filenames, 'r') as f:
        algorithms = f.read().strip()
        algorithms = algorithms.strip('[]')
        algorithms = [str(x) for x in algorithms.split(',')]
    print(algorithms)
    for algorithm in algorithms:
        name = snake_to_pascal(module_name)