from adders import error_report
# from adders.first_batch_adders import prepare_operands

adders = """
 LOA, LOAWA, APPROX5, HEAA, M_HEAA, OLOCA, HOERAA, CEETA, HOAANED, HERLOA, M_HERLOA, COREA, SAAR, BPAA1, DBAA, NAA, M_SAAR
"""

# error_report.plot_error_vs_inaccurate_bits(second_batch_adders.BPAA2_LSP1_approx, 16, 1025.123, 0)
# error_report.plot_error_vs_inaccurate_bits(second_batch_adders.CEETA_approx, 16, 102.123, 12452.123)


# for adder in adders.split(","):
#     try:
#         error_report.plot_error_vs_inaccurate_bits(second_batch_adders.__dict__[adder.strip()+"_approx"], 32, 102.123, 12452.123)
#     except KeyError:
#         pass
#     try:
#         error_report.plot_error_vs_inaccurate_bits(approximate_adders.__dict__[adder.strip()+"_approx"], 32, 102.123, 12452.123)
#     except KeyError:
#         pass
import constants
import numpy as np

npa = np.array


all_adders = [name['adder'] for name in constants.APPROXIMATE_ADDERS.values()]

# Generate 200 random numbers
np.random.seed(42)
n1 = np.random.randint(1, 100, 200)
n2 = np.random.randint(1, 100, 200)

for adder in all_adders:
    error_report.get_errors(
        [8,9],adder,16, 12423.2343,2434.2324 
    )
        
        
    
    

