import math

def bit_not(num):
    return num ^ ((1 << num.bit_length()) - 1) if num else 1

def get_num_digits(num):
    if not num: return 0
    return int(math.log10(num))

# Create a function that changes the operands of the addition to use the full range of the bits
def prepare_operands(num1, num2, total_num_bits, inaccurate_bits, minimum_inaccurate_bits=0):
    if total_num_bits < 4:
        raise ValueError("The total number of bits should be at least 4")
    
    if inaccurate_bits < minimum_inaccurate_bits:
        raise ValueError(f"The number of inaccurate bits should be at least {minimum_inaccurate_bits}")
    
    if inaccurate_bits >= total_num_bits:
        raise ValueError("The number of inaccurate bits should be less than the total number of bits")

    if num1 > 2 ** (total_num_bits-1):
        raise ValueError(f"The operand {num1} is too large to be represented by {total_num_bits} bits")

    if num2 > 2 ** (total_num_bits-1):
        raise ValueError(f"The operand {num2} is too large to be represented by {total_num_bits} bits")

    # First we need to get the maximum number that can be represented by the total number of bits
    max_num = 2 ** (total_num_bits) -1
    max_num_digits = get_num_digits(max_num) -1

    # Get the number of digits in the operands
    num1_digits = get_num_digits(num1)
    num2_digits = get_num_digits(num2)

    operand_max_digits = max(num1_digits, num2_digits)

    scale_factor = 10 ** (max_num_digits - operand_max_digits)

    num1 = int(num1 * scale_factor)
    num2 = int(num2 * scale_factor)
    
    # Get maximum bit length of the operands
    max_bit_length = max(num1.bit_length(), num2.bit_length())
    diff_bits = total_num_bits - max_bit_length - 1
    
    # Multiply the operands by 2 ** diff
    num1 = num1 << diff_bits
    num2 = num2 << diff_bits
    scale_factor *= 2 ** diff_bits

    return num1, num2, scale_factor
    
