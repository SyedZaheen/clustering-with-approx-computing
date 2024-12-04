from constants import DATASETS

# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from create_report import test_clustering

dataset_names = ["aggregation"]
adder_names = ["BPAA2_LSP1", ]

for dataset_name in dataset_names:
    for adder_name in adder_names:
        for inaccurate_bits in range(4, 10):
            WCSS, converged = test_clustering(
                dataset_name = dataset_name,
                clustering_algorithm = "KMeans++_with_adder_mod",
                approximate_adder_name = adder_name,
                n_clusters = DATASETS[dataset_name]['clusters'],
                bit_configuration = (16, inaccurate_bits),
                maximum_iterations = 10,
                plot_clusters = True,
                plot_save_path = f"./results/cluster_plots_BPAA_LSP1/{adder_name}_{dataset_name}_{inaccurate_bits}.png",
                plot_title=f"{adder_name} on {dataset_name}, {inaccurate_bits} inaccurate bits"
            )
            print(f"Dataset: {dataset_name}, Adder: BPAA_LSP1, WCSS: {WCSS}, Converged: {converged}")
            print()