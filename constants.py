from adders import first_batch_adders
from adders import second_batch_adders
from clustering_algorithms import kmeans

adders = """
accurate_adder, LOA, LOAWA, APPROX5, HEAA, M_HEAA, OLOCA, 
HOERAA, CEETA, HOAANED, HERLOA, M_HERLOA, COREA, SAAR, BPAA, DBAA, NAA, M_SAAR, BPAA_LSP1
"""

adders_name_list = [adder.strip() for adder in adders.split(", ")]
print(adders_name_list)
print()

APPROXIMATE_ADDERS = {
    "accurate_adder": {
        "name": "Accurate_adder",
        "adder": first_batch_adders.accurate_adder  
    },
    "LOA": {
        "name": "LOA",
        "adder": second_batch_adders.LOA_approx
    },
    "LOAWA": {
        "name": "LOAWA",
        "adder": second_batch_adders.LOAWA_approx
    },
    "APPROX5": {
        "name": "APPROX5",
        "adder": second_batch_adders.APPROX5_approx
    },
    "HEAA": {
        "name": "HEAA",
        "adder": first_batch_adders.HEAA_approx
    },
    "M_HEAA": {
        "name": "M_HEAA",
        "adder": second_batch_adders.M_HEAA_approx
    },
    "OLOCA": {
        "name": "OLOCA",
        "adder": second_batch_adders.OLOCA_approx
    },
    "HOERAA": {
        "name": "HOERAA",
        "adder": first_batch_adders.HOERAA_approx
    },
    "CEETA": {
        "name": "CEETA",
        "adder": second_batch_adders.CEETA_approx
    },
    "HOAANED": {
        "name": "HOAANED",
        "adder": first_batch_adders.HOAANED_approx
    },
    "HERLOA": {
        "name": "HERLOA",
        "adder": second_batch_adders.HERLOA_approx
    },
    "M_HERLOA": {
        "name": "M_HERLOA",
        "adder": first_batch_adders.M_HERLOA_approx
    },
    "COREA": {
        "name": "COREA",
        "adder": second_batch_adders.COREA_approx
    },
    "SAAR": {
        "name": "SAAR",
        "adder": second_batch_adders.SAAR_approx
    },
    "BPAA": {
        "name": "BPAA",
        "adder": second_batch_adders.BPAA_approx
    },
    "DBAA": {
        "name": "DBAA",
        "adder": second_batch_adders.DBAA_approx
    },
    "NAA": {
        "name": "NAA",
        "adder": second_batch_adders.NAA_approx
    },
    "M_SAAR": {
        "name": "M_SAAR",
        "adder": second_batch_adders.M_SAAR_approx
    },
    "BPAA_LSP1": {
        "name": "BPAA_LSP1",
        "adder": second_batch_adders.BPAA_LSP1_approx
    }
}

DATASET_PATHS = [
    r"C:\Users\All Saints\Desktop\Uni mods\fyp\FYP code\clustering-with-approx-computing\data\aggregation.arff",
    r"C:\Users\All Saints\Desktop\Uni mods\fyp\FYP code\clustering-with-approx-computing\data\diamond9.arff",
    r"C:\Users\All Saints\Desktop\Uni mods\fyp\FYP code\clustering-with-approx-computing\data\DS-850.arff",
    r"C:\Users\All Saints\Desktop\Uni mods\fyp\FYP code\clustering-with-approx-computing\data\engytime.arff",
]

DATASETS = {
    "aggregation": {
        "name": "aggregation",
        "path": DATASET_PATHS[0],
        "clusters": 7
    },
    "diamond9": {
        "name": "diamond9",
        "path": DATASET_PATHS[1],
        "clusters": 9
    },
    "DS-850": {
        "name": "DS-850",
        "path": DATASET_PATHS[2],
        "clusters": 5
    },
    "engytime": {
        "name": "engytime",
        "path": DATASET_PATHS[3],
        "clusters": 2
    },
}

CLUSTERING_ALGORITHMS = {
    "KMeans_with_adder": {
        "name": "KMeans_with_adder",
        "algorithm": kmeans.kmeans_with_adder
    },
    "KMeans_without_adder": {
        "name": "KMeans_without_adder",
        "algorithm": kmeans.kmeans
    },
    "KMeans++_with_adder": {
        "name": "KMeans++_with_adder",
        "algorithm": kmeans.kmeansplus_with_adder
    },
    "KMeans++_with_adder_mod": {
        "name": "KMeans++_with_adder_modified",
        "algorithm": kmeans.kmeansplus_with_adder_modified
        
    }
    
}