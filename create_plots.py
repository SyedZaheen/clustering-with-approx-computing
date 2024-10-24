from constants import DATASETS

# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from create_report import test_clustering

dataset_names = DATASETS.keys()
adder_names = ["accurate_adder", "SAAR16", "BPAA1", "BPAA2", "BPAA1_LSP1", "BPAA2_LSP1" ]

for dataset_name in dataset_names:
    for adder_name in adder_names:
        WCSS, converged = test_clustering(
            dataset_name = dataset_name,
            clustering_algorithm = "KMeans++_with_adder_mod",
            approximate_adder_name = adder_name,
            n_clusters = DATASETS[dataset_name]['clusters'],
            bit_configuration = (16, 8),
            maximum_iterations = 10,
            plot_clusters = True,
            plot_save_path = f"./results/cluster_plots/{adder_name}_{dataset_name}.png",
            plot_title=f"{adder_name} on {dataset_name}"
        )
        print(f"Dataset: {dataset_name}, Adder: {adder_name}, WCSS: {WCSS}, Converged: {converged}")
        print()