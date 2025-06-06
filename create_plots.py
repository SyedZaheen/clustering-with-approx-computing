# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from create_report import perform_clustering_with_AA
from constants import DATASETS


for adder_name in "NAA", "accurate_adder":
    
    for dataset in DATASETS.keys():
        
        WCSS, converged = perform_clustering_with_AA(
            dataset_name=dataset,
            clustering_algorithm="KMeans++_with_adder_mod",
            approximate_adder_name=adder_name,
            n_clusters=DATASETS[dataset]['clusters'],
            bit_configuration=(16, 7),
            maximum_iterations=10,
            plot_clusters=True,
            # plot_save_path=f"./results/cluster_plots_NAA_7/{adder_name}_{dataset}_7.png",
            plot_title=f"{adder_name} on {dataset}, 7 inaccurate bits"
        )
        print(f"Dataset: {dataset}, Adder: {adder_name}, WCSS: {WCSS}, Converged: {converged}")
        
        #Refresh the plot
        plt.clf()

# adders = {
#     "accurate_adder": 4,
#     "LOA": 5,
#     "LOAWA": 5,
#     "APPROX5": 4,
#     "M_HEAA": 6,
#     "OLOCA": 5,
#     "HOERAA": 5,
#     "LDCA": 4,
#     "HPETA_II": 5,
#     "HOAANED": 5,
#     "HERLOA": 6,
#     "M_HERLOA": 6,
#     "COREA": 5,
#     "DBAA": 4,
#     "SAAR16": 4,  
#     "BPAA2_LSP1": 4
# }

# for adder_name, inaccurate_bits in adders.items():
#     if inaccurate_bits is not None:
#         WCSS, converged = test_clustering(
#             dataset_name=dataset_name,
#             clustering_algorithm="KMeans++_with_adder_mod",
#             approximate_adder_name=adder_name,
#             n_clusters=DATASETS[dataset_name]['clusters'],
#             bit_configuration=(16, inaccurate_bits),
#             maximum_iterations=10,
#             plot_clusters=True,
#             plot_save_path=f"./results/cluster_plots4x4/{adder_name}_{dataset_name}_{inaccurate_bits}.png",
#             plot_title=f"{adder_name} on {dataset_name}, {inaccurate_bits} inaccurate bits"
#         )
#         print(f"Dataset: {dataset_name}, Adder: {adder_name}, WCSS: {WCSS}, Converged: {converged}")
#     else:
#         print(f"Adder: {adder_name} is not applicable")