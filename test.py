adders = """
 LOA, LOAWA, APPROX5, HEAA, M-HEAA, OLOCA, HOERAA, CEETA, HOAANED, HERLOA, M-HERLOA, COREA, DBAA, SAAR, BPAA
"""
# print the adders one by one
# for adder in adders.split(","):
#     print(adder.strip())

from adders import error_report, approximate_adders, second_batch_adders

error_report.plot_error_vs_inaccurate_bits(second_batch_adders.BPAA_approx, 32, 1567876, 123)


