from .first_batch_adders import accurate_adder
import matplotlib.pyplot as plt
import numpy as np

def get_errors(inaccurate_bits, approximate_adder, total_num_bits=32, n1=1, n2=1):
    errors = []
    for inaccurate_bit in inaccurate_bits:
        approx_sum = approximate_adder(n1, n2, total_num_bits, inaccurate_bit)
        correct_sum = accurate_adder(n1, n2, total_num_bits, inaccurate_bit)
        percent_error = 100*abs(approx_sum - correct_sum) / correct_sum
        log_percent_error = np.log(percent_error + np.finfo(float).eps)
        print(
            f" inaccurate_bit {inaccurate_bit} approx_sum: {approx_sum}, correct_sum: {correct_sum}, logpercenterror {log_percent_error} AA {approximate_adder.__name__}"
        )
        errors.append(log_percent_error)
    
    return errors

def plot_error_vs_inaccurate_bits(approximate_adder, total_num_bits=32, n1=1, n2=1):
    inaccurate_bits = np.arange(3, total_num_bits)
    errors = get_errors(inaccurate_bits, approximate_adder, total_num_bits, n1, n2)
    
    plt.plot(inaccurate_bits, errors)
    # plot the x axis 
    plt.axhline(y=0, color='r', linestyle='--')
    
    # a 1% error will produce a log error of 0
    # so we plot the 1% error line
    if errors[-1] > 0:
        plt.axhline(y=np.log(1), color='g', linestyle='--')
    
    plt.xlabel('Number of inaccurate bits')
    plt.ylabel('Log Error')
    plt.title(f'Log Error vs Number of inaccurate bits for {approximate_adder.__name__}')
    plt.show()
