from .utils import prepare_operands, bit_not

def HPETA_II_approx(A, B, tot_num_bits, inaccurate_bits):
    A, B, scale_factor = prepare_operands(A, B, tot_num_bits, inaccurate_bits)
    carries = (A << 1) & (B << 1)
    
    # TODO: Check if the formula is correct. Looks about right
    inaccurate_region = ((A | B | carries) & bit_not(A&B) | (A&B&carries) ) % (2 ** inaccurate_bits)
    accurate_region = (A >> inaccurate_bits) + (B >> inaccurate_bits) + (((A & B) >> inaccurate_bits-1) % 2)
    accurate_region = accurate_region << inaccurate_bits
    
    HPETA_II_estimate_sum = accurate_region + inaccurate_region
    HPETA_II_estimate_sum = HPETA_II_estimate_sum % (2 ** (tot_num_bits + 1))
    return HPETA_II_estimate_sum / scale_factor

def LDCA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    # warnings.simplefilter('once', UserWarning)
    # warnings.warn("The order of the arguments matters. The first number is considered the 'X' - its P-1th bit is considered the carry and the rest is thrown away.", UserWarning)    

    # if inaccurate_bits is not an even number, make it even
    if inaccurate_bits % 2 != 0:
        # warnings.warn("The number of inaccurate bits must be an even number. Rounding up to the nearest even number.", UserWarning)
        inaccurate_bits -= 1
    
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    carry = (num1 >> (inaccurate_bits - 1)) % 2
    accurate_region = (num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + carry
    # Shift the accurate region back
    accurate_region = accurate_region << inaccurate_bits
    # First half of the inaccurate region is just the first number's bits
    inaccurate_region = num2 % (2 ** inaccurate_bits)
    # Second half of the inaccurate region is just 1s
    inaccurate_region = inaccurate_region | (2 ** (inaccurate_bits //2) - 1)
    
    LDCA_approx_sum = accurate_region + inaccurate_region
    LDCA_approx_sum = LDCA_approx_sum % (2 ** (tot_num_bits + 1))
    return LDCA_approx_sum / scale_factor