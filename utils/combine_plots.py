import matplotlib.pyplot as plt
import os

# List of adders and their corresponding inaccurate bits
adders = {
    "accurate_adder": 4,
    "LOA": 5,
    "LOAWA": 5,
    "APPROX5": 4,
    "M_HEAA": 6,
    "OLOCA": 5,
    "HOERAA": 5,
    "LDCA": 4,
    "HPETA_II": 5,
    "HOAANED": 5,
    "HERLOA": 6,
    "M_HERLOA": 6,
    "COREA": 5,
    "DBAA": 4,
    "SAAR16": 4,  
    "BPAA2_LSP1": 4
}
adders = [
    (name, inaccurate_bits) for name, inaccurate_bits in adders.items()
] 

# Create a 4x4 grid of plots
fig, axes = plt.subplots(4, 4, figsize=(20, 20))

for i, (adder_name, inaccurate_bits) in enumerate(adders):
    if inaccurate_bits is not None:
        row, col = divmod(i, 4)
        img_path = f"./results/cluster_plots4x4/{adder_name}_aggregation_{inaccurate_bits}.png"
        if os.path.exists(img_path):
            img = plt.imread(img_path)
            axes[row, col].imshow(img)
            axes[row, col].axis('off')
        else:
            axes[row, col].text(0.5, 0.5, 'Image not found', ha='center', va='center')
            axes[row, col].axis('off')
    else:
        row, col = divmod(i, 4)
        axes[row, col].text(0.5, 0.5, 'Not applicable', ha='center', va='center')
        axes[row, col].set_title(f"{adder_name}")
        axes[row, col].axis('off')
        
# Adjust the spacing between the subplots
plt.subplots_adjust(wspace=0.1, hspace=0.05)

plt.tight_layout()
plt.savefig("./results/combined_cluster_plots.png")
plt.show()