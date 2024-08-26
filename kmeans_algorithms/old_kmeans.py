import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from adders import HEAA_approx, HOERAA_approx, HOAANED_approx, accurate_adder

# Step 1: Create a 2D random dummy dataset
n_samples = 100
n_features = 2
X, _ = make_blobs(n_samples=n_samples, centers=4, n_features=n_features, random_state=42)

# Define custom adders (example provided for HEAA, you can add others similarly)
def HEAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1 = int(num1)
    num2 = int(num2)
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    if (((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)) == 0:
        HEAA_estimate_sum = (((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits) + ((num1 % (2 ** inaccurate_bits)) | (num2 % (2 ** inaccurate_bits)))
    else:
        HEAA_estimate_sum = (((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + 1) << inaccurate_bits) + ((num1 % (2 ** (inaccurate_bits - 1))) | (num2 % (2 ** (inaccurate_bits - 1))))
    HEAA_estimate_sum = HEAA_estimate_sum % (2 ** (tot_num_bits + 1))
    return HEAA_estimate_sum

# Define a helper function to convert floating-point numbers to scaled integers
def float_to_int(num, scale_factor):
    return int(num * scale_factor)

# K-means clustering algorithm from scratch using custom adder for the distance calculation
def kmeans_custom_adder(X, k, adder, tot_num_bits=32, inaccurate_bits=8, max_iters=100):
    n_samples, n_features = X.shape
    centroids = X[np.random.choice(n_samples, k, replace=False)]
    scale_factor = 10**5  # Scale factor to convert floats to ints

    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        for idx, point in enumerate(X):
            distances = []
            for centroid in centroids:
                distance = 0
                for i in range(n_features):
                    diff = float_to_int(point[i] - centroid[i], scale_factor)
                    # Use custom adder for difference squared
                    distance = adder(distance, diff * diff, tot_num_bits, inaccurate_bits)
                distances.append(distance)
            cluster_idx = np.argmin(distances)
            clusters[cluster_idx].append(idx)
        
        # Handle empty clusters by reinitializing them to random points
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroids.append(X[cluster].mean(axis=0))
            else:
                new_centroids.append(X[np.random.randint(0, n_samples)])
        new_centroids = np.array(new_centroids)
        
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids

# Calculate WCSS for a clustering result
def calculate_wcss(X, clusters, centroids):
    wcss = 0
    for i, cluster in enumerate(clusters):
        for idx in cluster:
            wcss += np.sum((X[idx] - centroids[i]) ** 2)
    return wcss

# Plotting results in a 3x3 grid and calculate WCSS
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

# List of custom adders
custom_adders = [HEAA_approx, HOERAA_approx, HOAANED_approx]  # Add other custom adders to this list

wcwss = []

for i, adder in enumerate(custom_adders + [accurate_adder]):
    clusters, centroids = kmeans_custom_adder(X, k=4, adder=adder)
    wcss = calculate_wcss(X, clusters, centroids)
    wcwss.append(wcss)
    
    ax = axes[i]
    for cluster in clusters:
        ax.scatter(X[cluster, 0], X[cluster, 1])
    ax.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='x')
    ax.set_title(f"{adder.__name__}, WCSS: {wcss:.2f}")

plt.tight_layout()
plt.show()

# Print WCSS values
for i, wcss in enumerate(wcwss):
    print(f"WCSS for Adder {i+1}: {wcss:.2f}")