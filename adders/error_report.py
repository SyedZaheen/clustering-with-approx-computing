from .approximate_adders import accurate_adder
import matplotlib.pyplot as plt
import numpy as np

def plot_error_vs_inaccurate_bits(approximate_adder, total_num_bits=32, n1=1, n2=1):
    inaccurate_bits = np.arange(3, total_num_bits)
    errors = []
    for inaccurate_bit in inaccurate_bits:
        approx_sum = approximate_adder(n1, n2, total_num_bits, inaccurate_bit)
        correct_sum = accurate_adder(n1, n2, total_num_bits, inaccurate_bit)
        errors.append(np.log((approx_sum - correct_sum)**2 + np.finfo(float).eps))  # add epsilon to avoid log(0)
    
    plt.plot(inaccurate_bits, errors)
    plt.xlabel('Number of inaccurate bits')
    plt.ylabel('Log Error')
    plt.title(f'Log Error vs Number of inaccurate bits for {approximate_adder.__name__}')
    plt.show()
