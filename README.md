# Clustering with Approximate Computing

This repository contains code for performing clustering algorithms using approximate adders. The project explores how approximate computing can be applied to clustering tasks, potentially offering energy efficiency benefits while maintaining acceptable clustering quality.

## Overview

This research project implements various clustering algorithms (such as K-means and K-means++) with different approximate adder configurations. The goal is to analyze the trade-offs between computation accuracy, energy efficiency, and clustering quality.

## Repository Structure

```
clustering-with-approx-computing/
├── utils/
│   ├── constants.py         # Contains dataset info, adder definitions, and algorithm configs
│   └── create_report.py     # Functions for generating reports and clustering results
├── adders/                  # Implementation of various approximate adders
├── clustering_algorithms/   # Implementation of clustering algorithms with approximate adders
├── data/                    # Dataset files
├── results/                 # Generated results and plots
└── main.py                  # Main execution script
```

## Features

- Implementation of various approximate adders (LOA, LOAWA, APPROX5, HOAANED, etc.)
- Support for multiple datasets (aggregation, engytime, DS-850, diamond9, etc.)
- Configurable clustering algorithms with approximate computing components
- Visualization of clustering results
- Performance evaluation using WCSS (Within-Cluster Sum of Squares)

## Usage

### Basic Usage

To run a clustering experiment with a specific approximate adder and dataset:

```python
python main.py
```

By default, this will run the configuration specified in main.py. You can modify the parameters in the file:

```python
dataset_name = "aggregation"
adder_name = "HOAANED"
bit_configuration = (16, 10)  # (total bits, inaccurate bits)
clustering_algorithm = "KMeans++_with_adder_mod"
```

### Customization

You can customize the clustering process by modifying the parameters passed to `perform_clustering_with_AA()`:

```python
WCSS, converged = perform_clustering_with_AA(
    approximate_adder_name=adder_name,
    dataset_name=dataset_name,
    clustering_algorithm=clustering_algorithm,
    n_clusters=DATASETS[dataset_name]['clusters'],
    bit_configuration=(16, 5),  # Total bits, inaccurate bits
    maximum_iterations=10,
    plot_clusters=True,
    plot_title=f"{adder_name} on {dataset_name}, {bit_configuration[1]} inaccurate bits",
)
```

## Results

All results are given in excel files in the /results folder, along with the analysis stated in the paper

## Dependencies

- NumPy
- Matplotlib
- scikit-learn (for certain clustering algorithms)
- Pandas (for data handling)

## Contributing

Contributions to this project are welcome. Please ensure that any pull requests or issues are well-documented.

## License

MIT License

## Acknowledgments

This project is part of research on approximate computing applications in machine learning and data mining tasks.

## Citation

If you use this code or our results in your research, please cite the following papers:

```bibtex
@article{balasubramanian2025machine,
  title={Machine Learning Using Approximate Computing},
  author={Balasubramanian, P. and Zaheen, S. M. M. A. H. and Maskell, D. L.},
  journal={Journal of Low Power Electronics and Applications},
  volume={15},
  number={2},
  pages={21},
  year={2025},
  publisher={MDPI},
  doi={10.3390/jlpea15020021}
}

@inproceedings{balasubramanian2025kmeans,
  title={K-means Clustering using Approximate Addition},
  author={Balasubramanian, P. and Zaheen, S. M. M. A. H. and Maskell, D. L.},
  booktitle={Proceedings of the 68th IEEE International Midwest Symposium on Circuits and Systems},
  year={2025},
  note={Under review}
}
```

### Plain Text Citations

Balasubramanian, P., Zaheen, S. M. M. A. H., & Maskell, D. L. (2025). Machine Learning Using Approximate Computing. Journal of Low Power Electronics and Applications, 15(2), 21. https://doi.org/10.3390/jlpea15020021

Balasubramanian, P., Zaheen, S. M. M. A. H., & Maskell, D. L. (2025). K-means Clustering using Approximate Addition. Under review. Extended work submitted to the 68th IEEE International Midwest Symposium on Circuits and Systems


This section provides both BibTeX format (commonly used in LaTeX) and plain text citations, making it easy for others to properly cite your work when using your code or referencing your research.This section provides both BibTeX format (commonly used in LaTeX) and plain text citations, making it easy for others to properly cite your work when using your code or referencing your research.