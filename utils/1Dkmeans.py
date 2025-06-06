import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plotting

# 1. Generate 1D dataset

n = 5
x1 = np.random.normal(loc=-2, scale=2, size=n)
x2 = np.random.normal(loc= 2, scale=2, size=n)
X = np.concatenate([x1, x2]).reshape(-1,1)  # shape (400,1)

# 2. Prepare 2D grid of centroid pairs
grid_vals = np.arange(-7, 7.01, 0.1)
C1, C2 = np.meshgrid(grid_vals, grid_vals)  # both shape (101,101)

# 3. Compute WCSS for every (c1, c2)
def wcss_for_pair(c1, c2, X):
    # assign each xi to the nearest of c1 or c2
    d1 = (X - c1)**2
    d2 = (X - c2)**2
    # for each point pick min squared distance
    return np.sum(np.minimum(d1, d2))

# Vectorize over the grid
WCSS = np.empty_like(C1)
for i in range(C1.shape[0]):
    for j in range(C1.shape[1]):
        WCSS[i,j] = wcss_for_pair(C1[i,j], C2[i,j], X)

# 4. 3D visualization
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
eps = 1e-8
shifted = WCSS - WCSS.min() + eps
Z = -np.log(shifted)         # valleys become tall peaks
# or
Z = 1.0 / (shifted**0.5)     # sqrt-reciprocal for a milder effect
ax.plot_surface(C1, C2, WCSS, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_xlabel('Centroid 1 position')
ax.set_ylabel('Centroid 2 position')
ax.set_zlabel('WCSS')
ax.set_title('WCSS surface for 1D k=2 clustering')
plt.show()
