from .approximate_adders import prepare_operands
import warnings

"""

LOA
LOAWA
APPROX5
HEAA - Done
M-HEAA
OLOCA
HOERAA - Done
CEETA
HOAANED - Done
HERLOA 
COREA
DBAA
SAAR
BPAA

Example adder:
# HEAA Approximate Adder Sum
def HEAA_approx(num1, num2, tot_num_bits, inaccurate_bits):

    Approximates the sum of two numbers using a Hybrid Error-Aware Approximate (HEAA) adder.
    
    Parameters:
    - num1: The first input number.
    - num2: The second input number.
    - tot_num_bits: The total number of bits used for representing the input numbers.
    - inaccurate_bits: The number of least significant bits considered inaccurate (approximate).
    
    Returns:
    - HEAA_estimate_sum: The approximated sum of num1 and num2 scaled appropriately.

    
    # Prepare operands by adjusting their size and scaling factor
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits)
    
    # Modulo operation to ensure numbers are within the defined bit range
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    
    # Check the inaccurate bits; if the (inaccurate_bits - 1) bit of both numbers is 0, perform the approximation
    if (((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)) == 0:
        # Case where no carry occurs within the inaccurate region
        # Approximate addition of accurate part shifted left and OR operation on inaccurate part
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits
        ) + ((num1 % (2 ** inaccurate_bits)) | (num2 % (2 ** inaccurate_bits)))
    else:
        # Case where carry does occur within the inaccurate region
        # Adds a carry of 1 to the accurate part and shifts left, merging with modified inaccurate bits
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + 1)
            << inaccurate_bits
        ) + (
            (num1 % (2 ** (inaccurate_bits - 1)))
            | (num2 % (2 ** (inaccurate_bits - 1)))
        )
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    HEAA_estimate_sum = HEAA_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return HEAA_estimate_sum / 10 ** scale_factor
"""

def LOA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
  
    accurate_region = (
        (
            # The accurate region sum
            (num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)
            
            # The carry bit - if the (inaccurate_bits - 1) bit of both numbers is 1, then carry occurs 
            + (
                ((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)
            )
        )
        # Shift it back
        << inaccurate_bits
    ) 
    # Merge the inaccurate region
    inaccurate_region = ((num1 % (2 ** inaccurate_bits)) | (num2 % (2 ** inaccurate_bits)))
    LOA_estimate_sum = accurate_region + inaccurate_region
    
    LOA_estimate_sum = LOA_estimate_sum % (2 ** (tot_num_bits + 1))
    return LOA_estimate_sum / 10 ** scale_factor
    

def LOAWA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    
    accurate_region = ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits
    inaccurate_region = ((num1 % (2 ** inaccurate_bits)) | (num2 % (2 ** inaccurate_bits)))
    
    LOAWA_estimate_sum = accurate_region + inaccurate_region
    
    LOAWA_estimate_sum = LOAWA_estimate_sum % (2 ** (tot_num_bits + 1))
    return LOAWA_estimate_sum / 10 ** scale_factor


def APPROX5_approx(num1, num2, tot_num_bits, inaccurate_bits):
    warnings.simplefilter('once', UserWarning)
    warnings.warn("The order of the arguments matters. The first number is considered the 'X' - its P-1th bit is considered the carry and the rest is thrown away.", UserWarning)    
    
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    carry = (num1 >> (inaccurate_bits - 1)) % 2
    accurate_region = (num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + carry
    # Shift the accurate region back
    accurate_region = accurate_region << inaccurate_bits
    # The inaccurate region is just the first inaccurate_bits of the second number
    inaccurate_region = num2 % (2 ** inaccurate_bits)
    APPROX5_estimate_sum = accurate_region + inaccurate_region
    APPROX5_estimate_sum = APPROX5_estimate_sum % (2 ** (tot_num_bits + 1))
    return APPROX5_estimate_sum / 10 ** scale_factor

def M_HEAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
     # Prepare operands by adjusting their size and scaling factor
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits, minimum_inaccurate_bits=2)
    
    # Modulo operation to ensure numbers are within the defined bit range
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    
    # Check the inaccurate bits; if the (inaccurate_bits - 1) bit of both numbers is 0, perform the approximation
    if (((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)) == 0:
        # Case where no carry occurs within the inaccurate region
        # Approximate addition of accurate part shifted left and OR operation on inaccurate part
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits
        ) + (
                (num1 % (2 ** inaccurate_bits)) 
             | (num2 % (2 ** inaccurate_bits)) 
             | (2 ** (inaccurate_bits - 2) - 1)
             )
    else:
        # Case where carry does occur within the inaccurate region
        # Adds a carry of 1 to the accurate part and shifts left, merging with modified inaccurate bits
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + 1)
            << inaccurate_bits
        ) + (
            (num1 % (2 ** (inaccurate_bits - 1)))
            | (num2 % (2 ** (inaccurate_bits - 1)))
            |(2 ** (inaccurate_bits - 2) - 1)
        )
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    HEAA_estimate_sum = HEAA_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return HEAA_estimate_sum / 10 ** scale_factor

def OLOCA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    # Prepare operands by adjusting their size and scaling factor
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits, minimum_inaccurate_bits=2)
    
    # Modulo operation to ensure numbers are within the defined bit range
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    
    # Check the inaccurate bits; if the (inaccurate_bits - 1) bit of both numbers is 0, perform the approximation
    if (((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)) == 0:
        # Case where no carry occurs within the inaccurate region
        # Approximate addition of accurate part shifted left and OR operation on inaccurate part
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits
        ) + (
             (num1 % (2 ** inaccurate_bits)) 
             | (num2 % (2 ** inaccurate_bits)) 
             | (2 ** (inaccurate_bits - 2) - 1)
             )
    else:
        # Case where carry does occur within the inaccurate region
        # Adds a carry of 1 to the accurate part and shifts left, merging with modified inaccurate bits
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + 1)
            << inaccurate_bits
        ) + (
            (num1 % (2 ** inaccurate_bits))
            | (num2 % (2 ** inaccurate_bits))
            | (2 ** (inaccurate_bits - 2) - 1)
        )
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    HEAA_estimate_sum = HEAA_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return HEAA_estimate_sum / 10 ** scale_factor

#TODO: Error report shows strange results
def HERLOA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
        
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    if inaccurate_bits >= 3:
        HERLOA_estimate_sum = (
            (
                (
                    (num1 >> inaccurate_bits)
                    + (num2 >> inaccurate_bits)
                    + (
                        ((num1 >> (inaccurate_bits - 1)) % 2)
                        & ((num2 >> (inaccurate_bits - 1)) % 2)
                    )
                )
                << inaccurate_bits
            )
            + (
                (
                    (
                        ((num1 >> (inaccurate_bits - 1)) % 2)
                        ^ ((num2 >> (inaccurate_bits - 1)) % 2)
                    )
                    | (
                        ((num1 >> (inaccurate_bits - 2)) % 2)
                        & ((num2 >> (inaccurate_bits - 2)) % 2)
                    )
                )
                << (inaccurate_bits - 1)
            )
            + (
                (
                    (
                        ((num1 >> (inaccurate_bits - 2)) % 2)
                        | ((num2 >> (inaccurate_bits - 2)) % 2)
                    )
                    & (
                        not (
                            (
                                ((num1 >> (inaccurate_bits - 2)) % 2)
                                & ((num2 >> (inaccurate_bits - 2)) % 2)
                            )
                            & (
                                not (
                                    ((num1 >> (inaccurate_bits - 1)) % 2)
                                    ^ ((num2 >> (inaccurate_bits - 1)) % 2)
                                )
                            )
                        )
                    )
                )
                << (inaccurate_bits - 2)
            )
            + (
                (num1 % (2 ** (inaccurate_bits - 2)))
                | (num2 % (2 ** (inaccurate_bits - 2)))
                | (
                    (
                        (2 ** (inaccurate_bits - 2) - 1)
                        * (
                            (
                                (
                                    ((num1 >> (inaccurate_bits - 1)) % 2)
                                    ^ ((num2 >> (inaccurate_bits - 1)) % 2)
                                )
                                & (
                                    (
                                        ((num1 >> (inaccurate_bits - 2)) % 2)
                                        & ((num2 >> (inaccurate_bits - 2)) % 2)
                                    )
                                )
                            )
                        )
                    )
                    # | (2 ** (inaccurate_bits - 4) - 1)
                )
            )
        )
    else:
        raise ValueError("Inaccurate bits should be greater than or equal to 3")

    HERLOA_estimate_sum = HERLOA_estimate_sum % (2 ** (tot_num_bits + 1))
    return HERLOA_estimate_sum / 10 ** scale_factor

def bit_not(num):
    return num ^ ((1 << num.bit_length()) - 1)

def CEETA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    carries = num1 << 1
    
    # TODO: Check if the formula is correct. Looks about right
    inaccurate_region = (bit_not(num1) & (num2 | carries) | (num2 & carries)) % (2 ** inaccurate_bits)
    accurate_region = (num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + ((num1 >> inaccurate_bits-1) % 2)
    accurate_region = accurate_region << inaccurate_bits
    
    CEETA_estimate_sum = accurate_region + inaccurate_region
    CEETA_estimate_sum = CEETA_estimate_sum % (2 ** (tot_num_bits + 1))
    return CEETA_estimate_sum / 10 ** scale_factor

def COREA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    pass

def DBAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    sum = 0
    def impreciseDBA(AQ, AQ_1, BQ, BQ_1, CQm1):
        SUMQ1 = (bit_not(BQ_1)) | () | () | ()
        pass
        
    raise NotImplementedError("DBAA is not implemented yet")
    pass

def SAAR_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    sum = 0
    cout = 0
    for times in range(4):
        sum += ((num1 % (2** 8)) + (num2 % (2** 8)) + cout) << (8 * times)
        A7 = (num1 >> 7) % 2
        B7 = (num2 >> 7) % 2
        A6 = (num1 >> 6) % 2
        B6 = (num2 >> 6) % 2
        cout = (A7 & B7) | (A6 & B6) 
        num1 = num1 >> 8
        num2 = num2 >> 8
    sum = sum + cout
    
    sum = sum % (2 ** (tot_num_bits + 1))
    return sum / 10 ** scale_factor

def BPAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    sum = 0
    cout = 0
    for times in range(2):
        sum += ((num1 % (2** 16)) + (num2 % (2** 16)) + cout) << (16 * times)
        A15 = (num1 >> 15) % 2
        B15 = (num2 >> 15) % 2
        A14 = (num1 >> 14) % 2
        B14 = (num2 >> 14) % 2
        cout = (A15 & B15) | (A14 & B14) 
        num1 = num1 >> 16
        num2 = num2 >> 16
    sum = sum + cout
    
    sum = sum % (2 ** (tot_num_bits + 1))
    return sum / 10 ** scale_factor
