import math

def bit_not(num):
    return num ^ ((1 << num.bit_length()) - 1) if num else 1

def get_num_digits(num): 
    return 0 if num == 0 else int(math.log10(num))

# def prepare_operands(num1, num2, total_num_bits, inaccurate_bits, minimum_inaccurate_bits=0):
#     """
#     Converts two signed floating-point numbers into unsigned integer operands
#     that fully utilize the bit precision of a total_num_bits-bit approximate adder.

#     Args:
#         num1, num2 (float): Input floating-point numbers (signed).
#         total_num_bits (int): Total bit-width of the approximate adder.
#         inaccurate_bits (int): Number of least significant bits that are inaccurate.
#         minimum_inaccurate_bits (int, optional): Minimum number of inaccurate bits allowed.

#     Returns:
#         tuple: (operand1, operand2, scale_factor)
#             operand1, operand2 (int): Scaled unsigned integers.
#             scale_factor (float): Factor used for scaling.
#     """

#     # --- Validity Checks ---
#     if total_num_bits < 4:
#         raise ValueError("Total number of bits must be at least 4.")

#     if inaccurate_bits < minimum_inaccurate_bits:
#         raise ValueError(f"Inaccurate bits must be at least {minimum_inaccurate_bits}.")

#     # work with absolute values
#     num1, num2 = abs(num1), abs(num2)
    
#     # If both numbers are 0, return 0
#     if num1 == 0 and num2 == 0:
#         return 0, 0, 1
    
#     # Swap the numbers so that num1 is always the larger number
#     if num1 < num2:
#         num1, num2 = num2, num1

#     # --- Scale the Operands ---
    
#     # Get the max bit length between the two operands
#     max_bit_length = num1.bit_length()
    
#     # If the operands are too large, raise an error
#     if max_bit_length >= total_num_bits:
#         raise ValueError(f"Operands are too large to be represented by {total_num_bits} bits.")

#     # Get the number of bits to shift the operands by
#     diff_bits = total_num_bits - max_bit_length - 1
    
#     # Scale the operands by 2 ** diff_bits
#     scale_factor = 2 ** diff_bits
#     operand1 = num1 << diff_bits
#     operand2 = num2 << diff_bits
    
#     return operand1, operand2, scale_factor

# Create a function that changes the operands of the addition to use the full range of the bits
def prepare_operands(num1, num2, total_num_bits, inaccurate_bits, minimum_inaccurate_bits=0):
    if total_num_bits < 4:
        raise ValueError("The total number of bits should be at least 4")
    
    if inaccurate_bits < minimum_inaccurate_bits:
        raise ValueError(f"The number of inaccurate bits should be at least {minimum_inaccurate_bits}")
    
    # if inaccurate_bits >= total_num_bits:
    #     raise ValueError("The number of inaccurate bits should be less than the total number of bits")

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
    
