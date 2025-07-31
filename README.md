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

#### 1\.a Clone the repository
To get started, clone the repository and install the necessary Python packages using the `requirements.txt` file. (It is recommended to install packages and run all scripts within a virtual environment to avoid dependency conflicts.)
```bash
git clone https://github.com/thomas-dsl-johnson/ACORN.git
cd ACORN
pip install -r requirements.txt
```
We now have the following file structure. To see a full explanation, got to [📂 Repository Structure](https://github.com/thomas-dsl-johnson/ACORN?tab=readme-ov-file#-repository-structure)
```
.
├── algorithms/ ...
├── data/ ...
├── external/ ...
├── README.md
├── requirements.txt
├── run.py
└── utils/ ...
```
#### 1\.b Complete setup of Causal River datasets
Let's look at the `data/` directory. 
```
data
├── ground_truth_available
│   ├── Causal_River
│   │   └── Flood/ ...
│   └── IT_monitoring
│       ├── Antivirus_Activity/
│       ├── Middleware_oriented_message_Activity/
│       ├── Storm_Ingestion_Activity/ ...
│       └── Web_Activity/ ...
└── ground_truth_not_available
    └── sp500/ ...
```
The `data/Causal_River/` directory is missing the `Bavaria/` and `East Germany/` directories that appear in its [repository structure explanation](https://github.com/thomas-dsl-johnson/ACORN?tab=readme-ov-file#data). This is because the `CausalRiverBavaria` and `CausalRiverEastGermany` datasets are too large for this repository. We will need to download them from the original [CausalRivers GitHub repository](https://github.com/CausalRivers/causalrivers). If you do not require this, you can skip these steps. 
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

We are done. Our Causal River file structure should now match as it appears [here](https://github.com/thomas-dsl-johnson/ACORN?tab=readme-ov-file#data)

#### 1\.c Complete setup of S&P500 dataset


## 📂 Repository Structure

```
ACORN
├── README.md
├── algorithms
│   ├── causal_order/
│   └── end_to_end/
├── data
│   ├── ground_truth_available
│   │   ├── Causal_River/
│   │   └── IT_monitoring/
│   └── ground_truth_not_available
│       └── sp500/
├── external
│   ├── causal_rivers/
│   └── recover_causal_graph_from_causal_order/
├── requirements.txt
├── results/
├── run.py
└── utils
    └── storage.py
```

#### `algorithms/`

```
├── causal_order
│   ├── causal_order_result.py
│   ├── generic_causal_order_algorithm.py
│   ├── new
│   │   ├── direct_lingam_causal_order_algorithm_adding_nodes_in_batches_of_two.py
│   │   └── direct_lingam_causal_order_algorithm_no_updates.py
│   └── original
│       └── direct_lingam_causal_order_algorithm.py
└── end_to_end
    ├── end_to_end_result.py
    ├── generic_end_to_end_algorithm.py
    ├── new
    └── original
```

#### `data/`

```
├── ground_truth_available
│   ├── Causal_River
│   │   ├── Bavaria
│   │   │   ├── causal_order.txt
│   │   │   ├── rivers_bavaria.p
│   │   │   ├── rivers_ts_bavaria.csv
│   │   │   ├── rivers_ts_bavaria_preprocessed.csv
│   │   │   └── summary_matrix.npy
│   │   ├── East Germany
│   │   │   ├── causal_order.txt
│   │   │   ├── rivers_east_germany.p
│   │   │   ├── rivers_ts_east_germany.csv
│   │   │   ├── rivers_ts_east_germany_preprocessed.csv
│   │   │   └── summary_matrix.npy
│   │   └── Flood
│   │       ├── causal_order.txt
│   │       ├── rivers_flood.p
│   │       ├── rivers_ts_flood.csv
│   │       ├── rivers_ts_flood_preprocessed.csv
│   │       ├── rivers_ts_flood_preprocessed_dates_removed.csv
│   │       └── summary_matrix.npy
│   └── IT_monitoring
│       ├── Antivirus_Activity
│       │   ├── causal_graph_label.png
│       │   ├── causal_order.txt
│       │   ├── preprocessed_1.csv
│       │   ├── preprocessed_2.csv
│       │   ├── structure.txt
│       │   └── summary_matrix.npy
│       ├── Middleware_oriented_message_Activity
│       │   ├── causal_graph_label.png
│       │   ├── causal_order.txt
│       │   ├── monitoring_metrics_1.csv
│       │   ├── monitoring_metrics_2.csv
│       │   ├── structure.txt
│       │   └── summary_matrix.npy
│       ├── Storm_Ingestion_Activity
│       │   ├── causal_graph_label.png
│       │   ├── causal_order.txt
│       │   ├── storm_data_normal.csv
│       │   ├── structure.txt
│       │   └── summary_matrix.npy
│       └── Web_Activity
│           ├── causal_graph_label.png
│           ├── causal_order.txt
│           ├── preprocessed_1.csv
│           ├── preprocessed_2.csv
│           ├── structure.txt
│           └── summary_matrix.npy
└── ground_truth_not_available
    └── sp500
        ├── sp500.xlsx
        ├── sp500_100_columns.xlsx
        ├── sp500_20_columns.xlsx
        ├── sp500_3_columns.xlsx
        └── sp500_50_columns.xlsx
```

This directory contains the datasets. Each dataset has its own subfolder, which includes the raw data and the corresponding ground truth files. The repository includes:
* `ground_truth_available/`
  * IT Monitoring Data:  Source: [Case\_Studies\_of\_Causal\_Discovery](https://github.com/ckassaad/Case_Studies_of_Causal_Discovery_from_IT_Monitoring_Time_Series)
  * CausalRiver Datasets: Source: [CausalRivers](https://github.com/CausalRivers/causalrivers). For the Bavaria and East Germany data you must complete [step 1b](https://github.com/thomas-dsl-johnson/ACORN?tab=readme-ov-file#1b-complete-setup). 
* `ground_truth_not_available/`
  * s&p500 Data


#### `external/`
We have 2 submodules.
[Causal Rivers](https://github.com/CausalRivers/causalrivers)
[Causal Graph Recovery from Causal Order Repository](https://github.com/ckassaad/Case_Studies_of_Causal_Discovery_from_IT_Monitoring_Time_Series)

#### `results/`

#### `utils/`


-----
## 📝 Notes

  * Ensure that the number of variables in your dataset matches the dimensions of the summary matrix.
  * For large datasets (more than 15 variables), such as `CausalRiverFlood`, visualising the full causal graph is not recommended as it can become cluttered and difficult to interpret.
  * Thank you to Zhao Tong (@jultrishyyy) for the [Causal Graph Recovery from Causal Order Repository](https://github.com/jultrishyyy/Recover-Causal-Graph-from-Causal-Order/tree/50e7f0a7b06cca6623de99a4b467a71f70deca1b?tab=readme-ov-file#causal-graph-recovery-from-causal-order) and its detailed README 
  * For any issues or questions, please open an issue on the repository's issue tracker.