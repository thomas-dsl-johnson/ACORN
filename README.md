# ACORN - Assess Causal Order Results Neatly
The ACORN repository provides a neat and simple way to assess and visualise the differences between different algorithms that generate causal orders from data

-----
## 🚀 Getting Started

### Python Version

The repository was tested using the following version of Python.

```
Python 3.12.4
```
You can check your own Python version by running this command in your terminal:
```bash
python --version
```

### 1\. Installation
To get started, clone the repository and install the necessary Python packages using the `requirements.txt` file. (It is recommended to install packages and run all scripts within a virtual environment to avoid dependency conflicts.)
```bash
git clone https://github.com/thomas-dsl-johnson/ACORN.git
cd ACORN
pip install -r requirements.txt
```
We now have the following file structure:
```
.
├── algorithms/ ...
├── data
│   ├── ground_truth_available
│   │   ├── Causal_River/
│   │   │   └── Flood/
│   │   └── IT_monitoring/ ...
│   └── ground_truth_not_available/ ...
├── external/ ...
├── README.md
├── requirements.txt
├── run.py
└── utils/ ...
```
The `CausalRiverBavaria` and `CausalRiverEastGermany` datasets are too large for this repository. We will need to download them from the original [CausalRivers GitHub repository](https://github.com/CausalRivers/causalrivers).
```bash
# 1. Clone the submodules
git submodule update --init --recursive
cd external/causal_rivers
# 2. Follow the install steps for causal rivers
./install.sh
conda activate causalrivers
python 0_generate_datsets.py
# 3. Create and Populate the Bavaria and East Germany Directories inside data/ground_truth_available/Causal_river/
cd ../..
mkdir data/ground_truth_available/Causal_River/Bavaria
mkdir data/ground_truth_available/Causal_River/East\ Germany              ─╯
cp external/causal_rivers/product/rivers_bavaria.p data/ground_truth_available/Causal_River/Bavaria
cp external/causal_rivers/product/rivers_east_germany.p data/ground_truth_available/Causal_River/East\ Germany
cp external/causal_rivers/product/rivers_ts_bavaria.csv data/ground_truth_available/Causal_River/Bavaria
cp external/causal_rivers/product/rivers_ts_east_germany.csv data/ground_truth_available/Causal_River/East\ Germany
```
4.a)
We must now create the preprocessed .csv files using the Causal Graph Recovery from Causal Order Repository. Using your favourite editor change the following constants in `external/recover_causal_graph_from_causal_order/generate_ground_truth/process_causalriver.py`
```python
ROOT_DIR = os.getcwd()
DATA_PATH = os.path.join(ROOT_DIR, "data/ground_truth_available/Causal_River", "East Germany")
input_filename = DATA_PATH + "/rivers_ts_east_germany.csv"
output_filename = DATA_PATH + "/rivers_ts_east_germany_preprocessed.csv"
```
Run the file.
```bash
python external/recover_causal_graph_from_causal_order/generate_ground_truth/process_causalriver.py
```
Now repeat for Bavaria
```python
ROOT_DIR = os.getcwd()
DATA_PATH = os.path.join(ROOT_DIR, "data/ground_truth_available/Causal_River", "Bavaria")
input_filename = DATA_PATH + "/rivers_ts_bavaria.csv"
output_filename = DATA_PATH + "/rivers_ts_bavaria_preprocessed.csv"
```
Run the file.
```bash
python external/recover_causal_graph_from_causal_order/generate_ground_truth/process_causalriver.py
```
4.b)
Now we will create the `summary_matrix.npy` files for Bavaria and East Germany. We will edit `external/recover_causal_graph_from_causal_order/generate_ground_truth/generate_causalriver_summary_matrix.py` 
```python
ROOT_DIR = os.getcwd()
DATA_PATH = os.path.join(ROOT_DIR, "data/ground_truth_available/Causal_River", "East Germany")
input_data_filename = DATA_PATH + "/rivers_ts_east_germany_preprocessed.csv" # Make sure this path is correct
input_label_filename = DATA_PATH + "/rivers_east_germany.p" # Ground truth graph data
output_matrix_filename = DATA_PATH + '/summary_matrix.npy'
```
Then run the file.
```bash
python external/recover_causal_graph_from_causal_order/generate_ground_truth/generate_causalriver_summary_matrix
```
Now repeat for Bavaria
```python
ROOT_DIR = os.getcwd()
DATA_PATH = os.path.join(ROOT_DIR, "data/ground_truth_available/Causal_River", "Bavaria")
input_data_filename = DATA_PATH + "/rivers_ts_bavaria_preprocessed.csv" # Make sure this path is correct
input_label_filename = DATA_PATH + "/rivers_bavaria.p" # Ground truth graph data
output_matrix_filename = DATA_PATH + '/summary_matrix.npy'
```
Then run the file.
```bash
python external/recover_causal_graph_from_causal_order/generate_ground_truth/generate_causalriver_summary_matrix
```
For completeness we shall generate the `causal_order.txt` files. We will edit `external/recover_causal_graph_from_causal_order/generate_ground_truth/generate_order_from_matrix`
```python
ROOT_DIR = os.getcwd()

...

DATA_PATH = os.path.join(ROOT_DIR, "data/ground_truth_available/Causal_River", "East Germany")
```
Then run the file.
```bash
python external/recover_causal_graph_from_causal_order/generate_ground_truth/generate_order_from_matrix.py
```
Then change for Bavaria.
```python
ROOT_DIR = os.getcwd()

...

DATA_PATH = os.path.join(ROOT_DIR, "data/ground_truth_available/Causal_River", "Bavaria")
```
Then run the file.
```bash
python external/recover_causal_graph_from_causal_order/generate_ground_truth/generate_order_from_matrix.py
```

We are done. Our Causal River file structure should now look like this. 
```
data/ground_truth_available/Causal_River
├── Bavaria
│   ├── causal_order.txt
│   ├── rivers_bavaria.p
│   ├── rivers_ts_bavaria.csv
│   ├── rivers_ts_bavaria_preprocessed.csv
│   └── summary_matrix.npy
├── East Germany
│   ├── causal_order.txt
│   ├── rivers_east_germany.p
│   ├── rivers_ts_east_germany.csv
│   ├── rivers_ts_east_germany_preprocessed.csv
│   └── summary_matrix.npy
└── Flood
    ├── causal_order.txt
    ├── rivers_flood.p
    ├── rivers_ts_flood.csv
    ├── rivers_ts_flood_preprocessed.csv
    ├── rivers_ts_flood_preprocessed_dates_removed.csv
    └── summary_matrix.npy
```
-----
## 📝 Notes

  * Ensure that the number of variables in your dataset matches the dimensions of the summary matrix.
  * For large datasets (more than 15 variables), such as `CausalRiverFlood`, visualising the full causal graph is not recommended as it can become cluttered and difficult to interpret.
  * Thank you to Zhao Tong for the [Causal Graph Recovery from Causal Order Repository](https://github.com/jultrishyyy/Recover-Causal-Graph-from-Causal-Order/tree/50e7f0a7b06cca6623de99a4b467a71f70deca1b?tab=readme-ov-file#causal-graph-recovery-from-causal-order) and its detailed README 
  * For any issues or questions, please open an issue on the repository's issue tracker.