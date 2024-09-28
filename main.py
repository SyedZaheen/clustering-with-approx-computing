import numpy as np
import matplotlib.pyplot as plt
from clustering_algorithms.kmeans import kmeans, calculate_wcss, kmeans_with_adder, kmeansplus_with_adder
from adders.approximate_adders import accurate_adder, HOAANED_approx, HOERAA_approx, M_HERLOA_approx, HEAA_approx
from data.load_data import load_arff_file

COLORS = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'brown', 'orange']



# Plot the data itself
def plot_data(X):
    plt.scatter(X[:, 0], X[:, 1])
    plt.title("Raw data w/o clusters")
    plt.show()

# Plot the clusters and centroids
def plot_clusters(X, clusters, centroids, title=""):
    for idx, cluster in enumerate(clusters):
        points = X[cluster]
        plt.scatter(points[:, 0], points[:, 1], c=COLORS[idx % len(COLORS)], label=f'Cluster {idx+1}')
    centroids = np.array(centroids)
    WCSS = calculate_wcss(X, clusters, centroids)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='black', marker='X', label='Centroids')
    # Print the WCSS in scientific notation
    plt.title(f"{title}: WCSS: {WCSS:.5e}")


# Plot the clusters and centroids
def plot_clusters_with_track(X, clusters, centroids, centroid_track):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    
    # Plot the final centroids
    centroids = np.array(centroids)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='black', marker='X', label='Final Centroids')
    
    # Plot the centroid tracks
    for idx in range(len(centroids)):
        centroid_path = centroid_track[:, idx, :]
        plt.plot(centroid_path[:, 0], centroid_path[:, 1], linestyle='--', marker='o', markersize=2, color=colors[idx % len(colors)], label=f'Centroid {idx+1} Path')
    plt.title("")
    plt.legend()
    plt.show()

def plot_wcss_vs_bits(adder, bits, X, k, start_bit=50, subaxis=None):
    
    plotter = plt if subaxis is None else subaxis

    accurate_bits, inaccurate_bits = bits

    # Create a range of inaccurate bits to test
    inacc_bits_range = range(start_bit, inaccurate_bits, 1)

    WCSS = []
    for bit in inacc_bits_range:
        clusters, centroids, _ = kmeansplus_with_adder(X, k, random_state=26, adder=adder, bits=(accurate_bits, bit))
        wcss = calculate_wcss(X, clusters, centroids)
        WCSS.append(wcss)
        print(f"WCSS for {adder.__name__} with {bit} inaccurate bits: {wcss}")
    plotter.plot(inacc_bits_range, WCSS, label=f'WCSS for {adder.__name__}', marker='o', color='r')
    plotter.xlabel("Inaccurate bits") if subaxis is None else plotter.set_xlabel("Inaccurate bits")
    plotter.ylabel("WCSS") if subaxis is None else plotter.set_ylabel("WCSS")

    # Plot the results from the accurate adder as a blue line
    accurate_clusters, accurate_centroids, _ = kmeans_with_adder(X, k, random_state=26, adder=accurate_adder, bits=(accurate_bits, 0))
    accurate_WCSS = calculate_wcss(X, accurate_clusters, accurate_centroids)
    plotter.axhline(y=accurate_WCSS, color='b', linestyle='--', label='WCSS with accurate adder')
    plotter.title(f"WCSS vs. Bits for {adder.__name__}") if subaxis is None else plotter.set_title(f"WCSS vs. Bits for {adder.__name__}")
    plotter.legend()
    


# Main function to test kmeans
def test_kmeans():

    X = load_arff_file()
    k = 9
    cur_adder = M_HERLOA_approx
  
    inaccurate_bit = 16
    clusters, centroids, _ = kmeansplus_with_adder(X, k, 100, 3134, cur_adder, bits=(32, inaccurate_bit))
    # plot_clusters(X, clusters, centroids, title=f"{cur_adder.__name__} {inaccurate_bit} bits")
    plot_wcss_vs_bits(cur_adder, (32, 30), X, k, 24)
    # fig, axes = plt.subplots(2, 2, figsize=(15, 15))
    # axes = axes.flatten()

    # for i in range(4):
    #     adders = [HEAA_approx, HOAANED_approx, HOERAA_approx, M_HERLOA_approx]
    #     plot_wcss_vs_bits(adders[i], (32, 31), X, k, 20, subaxis=axes[i])
    plt.tight_layout()
    plt.show()
    
def plot_seeds_vs_wcss():
    file_name = r'diamond9.arff'
    X = load_arff_file(file_name)
    k = 7
    cur_adder = HOERAA_approx

    seeds = np.arange(0, 30, 1)
    wcsses = []

    for seed in seeds:
        clusters, centroids, _ = kmeans_with_adder(X, k, 100, seed, cur_adder, bits=(64, 23))
        wcsses.append(
            calculate_wcss(X, clusters, centroids)
        )
        print(wcsses[-1], "for seed", seed)
    
    plt.plot(seeds, wcsses)
    plt.show()

# Call the test function
# plot_seeds_vs_wcss()
test_kmeans()

