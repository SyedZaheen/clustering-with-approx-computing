from adders import error_report, first_batch_adders, second_batch_adders, third_batch_adders
from adders.first_batch_adders import prepare_operands
import numpy as np

adders = """
 LOA, LOAWA, APPROX5, HEAA, M_HEAA, OLOCA, HOERAA, CEETA, HOAANED, HERLOA, M_HERLOA, COREA, SAAR, BPAA1, DBAA, NAA, M_SAAR
"""

error_report.plot_error_vs_inaccurate_bits(third_batch_adders.HPETA_II_approx, 16, 102.123, 12452.123)
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

