# Clustering with Approximate Computing

This repository contains code to perform experiments on clustering using approximate adders. The goal is to analyze the performance of different approximate adders in clustering algorithms and visualize the results.


## Key Files and Directories

- `main.py`: Contains the main functions for clustering and plotting.
- `combine_plots.py`: Combines individual cluster plots into a single grid.
- `create_plots.py`: Generates plots for different datasets and adders.
- `create_report.py`: Creates reports and saves results to CSV files.
- `constants.py`: Defines constants used across the project.
- `clustering_results.ipynb`: Jupyter notebook for testing clustering on datasets.
- `adders/`: Contains implementations of various approximate adders.
- `clustering_algorithms/`: Contains implementations of clustering algorithms.
- `data/`: Directory for storing datasets.
- `results/`: Directory for storing results and plots.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/clustering-with-approx-computing.git
    cd clustering-with-approx-computing
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
# Author

Syed M. M. Mosayeeb Al Hady Zaheen, some approximate adder architectures obtained from various external sources:
https://www.mdpi.com/2079-9292/10/23/2917
https://www.mdpi.com/2079-9292/11/19/3095
Approximate adder architectures not in the above are novel  

## Usage

### Running the Main Script

To run the main clustering script, use:
```sh
python main.py
