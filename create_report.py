# we will export the data to a excel file
# we will use the pandas library to create the excel file
# we will use the openpyxl library to format the excel file

from constants import *
import pandas as pd
from data.load_data import load_arff_file_from_file_path
from clustering_algorithms.kmeans import calculate_wcss
from main import plot_clusters as plot_clustering
from matplotlib import pyplot as plt
import  numpy as np

# We want to just test the clustering on a single dataset
# Choose the diamond9 dataset

def perform_clustering_with_AA(
    dataset_name,
    clustering_algorithm,
    approximate_adder_name,
    n_clusters,
    bit_configuration = (32, 8),
    initialisation_random_state = 42,
    maximum_iterations = 10,
    plot_clusters = False,
    plot_save_path = None,
    plot_title = ""
):
    """
    @param dataset_name: The name of the dataset to test the clustering algorithm on
    @param clustering_algorithm: The name of the clustering algorithm to use
    @param approximate_adder_name: The name of the approximate adder to use
    @param n_clusters: The number of clusters to use
    @param bit_configuration: The configuration of the bits to use
    @param initialisation_random_state: The random state to use for the initialisation
    @param maximum_iterations: The maximum number of iterations to use
    @param plot_clusters: Whether to plot the clusters or not
    
    @return: The WCSS and whether the algorithm converged
    """
    
    # We first load the dataset
    dataset = load_arff_file_from_file_path(DATASETS[dataset_name]['path'])
    
    # We then load the clustering algorithm
    clustering_function = CLUSTERING_ALGORITHMS[clustering_algorithm]['algorithm']
    # The clustering function has parameters (X, k, max_iters=100,  random_state=26, adder=accurate_adder, bits=(32, 4))
    # We then load the approximate adder
    adder = APPROXIMATE_ADDERS[approximate_adder_name]['adder']
    # The adder has parameters (num1, num2, total_bits, inaccurate_bits)
       
    # We then initialize the results dictionary
    
    clusters, centroids, converged = clustering_function(dataset, n_clusters, max_iters=maximum_iterations, adder=adder, random_state=initialisation_random_state, bits=bit_configuration)
    WCSS = calculate_wcss(dataset, clusters, centroids)
    
    COLORS = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'brown', 'orange']
    if plot_clusters:

        for idx, cluster in enumerate(clusters):
            points = dataset[cluster]
            plt.scatter(points[:, 0], points[:, 1], c=COLORS[idx % len(COLORS)], label=f'Cluster {idx+1}')
        centroids = np.array(centroids)
        WCSS = calculate_wcss(dataset, clusters, centroids)
   
        plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='black', marker='X', label='Centroids')
        # Print the WCSS in scientific notation
        plt.title(f"{dataset_name} on {approximate_adder_name}: WCSS: {WCSS}")
        
        if plot_save_path:
            plt.savefig(plot_save_path)
    
    return WCSS, converged

if __name__ == '__main__':
    
    all_adder_names = ["LDCA"]
    
    DATASET_NAMES = list(DATASETS.keys())
    
    for dataset_name in DATASET_NAMES:

        for total_bits in [16]:
            
            inaccurate_bit_range = range(4,14,2)
            
            # Initialise a dataframe to store rows for the adder functions and the inaccurate bits as the columns
            df = pd.DataFrame(columns=[a for a in all_adder_names], index=inaccurate_bit_range)
            
            # for every adder function
            for adder_name in all_adder_names:
                # for every inaccurate bit configuration
                for inaccurate_bits in inaccurate_bit_range:
                    # test the clustering
                    WCSS, converged = perform_clustering_with_AA(
                        dataset_name,
                        "KMeans++_with_adder_mod",
                        adder_name,
                        DATASETS[dataset_name]['clusters'],
                        (total_bits, inaccurate_bits),
                        initialisation_random_state=42,
                        maximum_iterations=11,
                        plot_clusters=False,
                        
                    )
                    
                    # Put it in the dataframe
                    df.loc[inaccurate_bits, adder_name] = (1 if converged else -1) * WCSS
                
                print("completed ", adder_name, dataset_name, total_bits)
            
            # put it in a csv file, naming it after the number of total bits and the dataset
            df.to_csv(f"results/LDCA results/{dataset_name}_{total_bits}.csv")
            
            print("\ncompleted ", dataset_name, total_bits)
    
                    
    