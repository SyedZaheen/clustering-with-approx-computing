from sklearn.datasets import make_blobs

# Generate synthetic dataset
def generate__clustering_data(n_samples=500, n_features=2, centers=3, cluster_std=3, random_state=212): # Random state 44 gets stuck in a local minimum
    X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=centers, cluster_std=cluster_std, random_state=random_state)
    # Scale up the data
    X = X * 10**6
    return X