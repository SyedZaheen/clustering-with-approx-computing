from utils.constants import DATASETS, APPROXIMATE_ADDERS, CLUSTERING_ALGORITHMS
from utils.create_report import perform_clustering_with_AA
import matplotlib.pyplot as plt

dataset_name = "aggregation"
adder_name = "HOAANED"
bit_configuration = (16, 10)
clustering_algorithm = "KMeans++_with_adder_mod"

WCSS, converged = perform_clustering_with_AA(
    approximate_adder_name=adder_name,
    dataset_name=dataset_name,
    clustering_algorithm=clustering_algorithm,
    n_clusters=DATASETS[dataset_name]['clusters'],
    bit_configuration=bit_configuration,
    maximum_iterations=10,
    plot_clusters=True,
    plot_title=f"{adder_name} on {dataset_name}, {bit_configuration[1]} inaccurate bits",
)

print(f"WCSS: {WCSS}, Converged: {converged}")
plt.show()