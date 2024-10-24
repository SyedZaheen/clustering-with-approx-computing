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