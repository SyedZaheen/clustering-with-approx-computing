from .utils import prepare_operands, bit_not
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
BPAA1

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
    return HEAA_estimate_sum / scale_factor
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
    return LOA_estimate_sum / scale_factor
    

def LOAWA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    
    accurate_region = ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits
    inaccurate_region = ((num1 % (2 ** inaccurate_bits)) | (num2 % (2 ** inaccurate_bits)))
    
    LOAWA_estimate_sum = accurate_region + inaccurate_region
    
    LOAWA_estimate_sum = LOAWA_estimate_sum % (2 ** (tot_num_bits + 1))
    return LOAWA_estimate_sum / scale_factor


def APPROX5_approx(num1, num2, tot_num_bits, inaccurate_bits):
    # warnings.simplefilter('once', UserWarning)
    # warnings.warn("The order of the arguments matters. The first number is considered the 'X' - its P-1th bit is considered the carry and the rest is thrown away.", UserWarning)    
    
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    carry = (num1 >> (inaccurate_bits - 1)) % 2
    accurate_region = (num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + carry
    # Shift the accurate region back
    accurate_region = accurate_region << inaccurate_bits
    # The inaccurate region is just the first inaccurate_bits of the second number
    inaccurate_region = num2 % (2 ** inaccurate_bits)
    APPROX5_estimate_sum = accurate_region + inaccurate_region
    APPROX5_estimate_sum = APPROX5_estimate_sum % (2 ** (tot_num_bits + 1))
    return APPROX5_estimate_sum / scale_factor

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
    return HEAA_estimate_sum / scale_factor

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
    return HEAA_estimate_sum / scale_factor

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
    return HERLOA_estimate_sum / scale_factor



def CEETA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    carries = num1 << 1
    
    # TODO: Check if the formula is correct. Looks about right
    inaccurate_region = (bit_not(num1) & (num2 | carries) | (num2 & carries)) % (2 ** inaccurate_bits)
    accurate_region = (num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + ((num1 >> inaccurate_bits-1) % 2)
    accurate_region = accurate_region << inaccurate_bits
    
    CEETA_estimate_sum = accurate_region + inaccurate_region
    CEETA_estimate_sum = CEETA_estimate_sum % (2 ** (tot_num_bits + 1))
    return CEETA_estimate_sum / scale_factor

def COREA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    # Pepare operands
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    # We need the total inaccurate bits to be at least 3
    if inaccurate_bits < 3:
        raise ValueError("Inaccurate bits should be greater than or equal to 3")
    
    # Rename inaccurate bits to K in order to match the paper
    K = inaccurate_bits
    
    # Set L to be the floor of inaccurate_bits/2
    L = K // 2
    
    # First compute the accurate region
    accurate_region = (num1 >> K+1) + (num2 >> K+1)
    
    #Get the k-th bits
    AK = (num1 >> K) % 2
    BK = (num2 >> K) % 2
    
    # half-add the Kth bit
    half_add_kth_bits = AK ^ BK
    carry = AK & BK
    
    # Add the carry to the accurate region
    accurate_region += carry
    
    # Get the k-1th bits
    AK_1 = (num1 >> K-1) % 2
    BK_1 = (num2 >> K-1) % 2
    
    Cin = AK_1 & BK_1
    
    # The kth sum bit is the or of the half adder and the cin
    SUMK = half_add_kth_bits | Cin
    
    # The spread bit is OR-ed from k-1th bit to lth bit
    spread_bit = half_add_kth_bits & Cin
    
    # Now we focus on computing the inaccurate region
    # First we get the K-1th inaccurate bit
    SUMK_1 = (AK_1 ^ BK_1) | spread_bit
    
    # Now we get from the K-2th bit to the Lth bit for both the numbers
    A = (num1 >> L) % (2 ** (K - L - 1))
    B = (num2 >> L) % (2 ** (K - L - 1))
    
    # If the spread bit is 1, repeat it (K - L - 1) times
    spread = spread_bit * (2 ** (K - L - 1) - 1)
    
    SUMK_2toL = A | B | spread
    
    # Remaining L-1th bits to 0 is just 1
    SUML_1to0 = 2 ** L - 1
    
    # Finally, we bit shift each region to the correct position and add them together
    inaccurate_region = (SUMK << K) + (SUMK_1 << (K-1)) + (SUMK_2toL << L) + SUML_1to0
    
    # Shift the accurate region back
    accurate_region = accurate_region << (K + 1)
    
    # Combine the accurate and inaccurate regions
    COREA_estimate_sum = accurate_region + inaccurate_region
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    COREA_estimate_sum = COREA_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return COREA_estimate_sum / scale_factor
    

def DBAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    if inaccurate_bits % 2 != 0:
        inaccurate_bits -= 1
        # UserWarning(f"Inaccurate bits for DBAA should be an even number. Since it is not, it will be rounded down to {inaccurate_bits}")
    
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    def impreciseDBA(AQ, AQ_1, BQ, BQ_1, CQm1):
        nAQ = bit_not(AQ)
        nAQ_1 = bit_not(AQ_1)
        nBQ_1 = bit_not(BQ_1)

        CQ_1 = (AQ_1 & AQ) | (BQ_1 & AQ) | (AQ_1 & BQ_1)
        SUMQ_1 = (nBQ_1 & nAQ_1 & AQ) | (nBQ_1 & AQ_1 & nAQ) | (BQ_1 & nAQ_1 & nAQ) | (BQ_1 & AQ_1 & AQ)
        SUMQ = (BQ & nAQ) | (CQm1 & nAQ) | (BQ & CQm1)
        
        return SUMQ_1, SUMQ, CQ_1
    
    inaccurate_region = 0
    CQm1 = 0
    for i in range(0, inaccurate_bits, 2):
        AQ = (num1 >> i) % 2
        AQ_1 = (num1 >> (i + 1)) % 2
        BQ = (num2 >> i) % 2
        BQ_1 = (num2 >> (i + 1)) % 2
        
        SUMQ_1, SUMQ, CQm1 = impreciseDBA(AQ, AQ_1, BQ, BQ_1, CQm1)
        inaccurate_region += (SUMQ << i) + (SUMQ_1 << (i + 1))
    
    last_carry = CQm1
    
    # compute the accurate region
    accurate_region = (num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + last_carry
    accurate_region = accurate_region << inaccurate_bits
    
    # Combine the accurate and inaccurate regions
    DBAA_estimate_sum = accurate_region + inaccurate_region
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    DBAA_estimate_sum = DBAA_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return DBAA_estimate_sum / scale_factor
    

def SAAR_approx(num1, num2, tot_num_bits, inaccurate_bits):
    if not tot_num_bits % 8 or tot_num_bits < 8:
        # UserWarning("SAAR is only implemented for multiples of 8-bit numbers. Will use the closest 8-bit for this approx.")
        pass
    tot_num_bits = max((tot_num_bits // 8) * 8, 8)
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    sum = 0
    cout = 0
    for times in range(tot_num_bits // 8):
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
    return sum / scale_factor

def SAAR16_approx(num1, num2, tot_num_bits, inaccurate_bits):
    
    if tot_num_bits != 16:
        # UserWarning("SAAR16 is only implemented for 16-bit numbers. Will use 16-bit for this approx.")
        tot_num_bits = 16
    
    A, B, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    # SAAR16 is partition 6-6-4
    # So lets grab the first 4 bits of each number
    SUM0to3 = (A % (2 ** 4)) + (B % (2 ** 4))
    
    # Calculate the carry
    A3 = (A >> 3) % 2
    B3 = (B >> 3) % 2
    A2 = (A >> 2) % 2
    B2 = (B >> 2) % 2
    cout1 = (A3 & B3) | (A2 & B2)
    
    # We are done with the right side. Shift the numbers to the right
    A = A >> 4
    B = B >> 4
    
    # Now we do the same for the next 6 bits
    SUM4to9 = (A % (2 ** 6)) + (B % (2 ** 6)) + cout1
    
    # Calculate the carry
    A9 = (A >> 5) % 2
    A8 = (A >> 4) % 2
    B9 = (B >> 5) % 2
    B8 = (B >> 4) % 2
    cout2 = (A9 & B9) | (A8 & B8)
    
    # We are done with the middle. Shift the numbers to the right
    A = A >> 6
    B = B >> 6
    
    # Finally, we do the same for the last 6 bits
    SUM10to15 = (A % (2 ** 6)) + (B % (2 ** 6)) + cout2
    
    # Combine the results
    SAAR16_estimate_sum = (SUM0to3) + (SUM4to9 << 4) + (SUM10to15 << 10)
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    SAAR16_estimate_sum = SAAR16_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return SAAR16_estimate_sum / scale_factor


def M_SAAR_approx(num1, num2, tot_num_bits, inaccurate_bits):
    if not tot_num_bits % 8 or tot_num_bits < 8:
        pass
        # UserWarning("M-SAAR is only implemented for multiples of 8-bit numbers. Will use the closest 8-bit for this approx.")
    tot_num_bits = max((tot_num_bits // 8) * 8, 8)
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    sum = 0
    cout = 0
    for times in range(tot_num_bits // 8):
        sum += ((num1 % (2** 8)) + (num2 % (2** 8)) + cout) << (8 * times)
        A7 = (num1 >> 7) % 2
        B7 = (num2 >> 7) % 2
        A6 = (num1 >> 6) % 2
        B6 = (num2 >> 6) % 2
        cout = (A7 & B7)
        num1 = num1 >> 8
        num2 = num2 >> 8
    sum = sum + cout
    
    sum = sum % (2 ** (tot_num_bits + 1))
    return sum / scale_factor

def M_SAAR16_approx(num1, num2, tot_num_bits, inaccurate_bits):
    
    if tot_num_bits != 16:
        # UserWarning("SAAR16 is only implemented for 16-bit numbers. Will use 16-bit for this approx.")
        tot_num_bits = 16
    
    A, B, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    # SAAR16 is partition 6-6-4
    # So lets grab the first 4 bits of each number
    SUM0to3 = (A % (2 ** 4)) + (B % (2 ** 4))
    
    # Calculate the carry
    A3 = (A >> 3) % 2
    B3 = (B >> 3) % 2
    cout1 = (A3 & B3) 
    
    # We are done with the right side. Shift the numbers to the right
    A = A >> 4
    B = B >> 4
    
    # Now we do the same for the next 6 bits
    SUM4to9 = (A % (2 ** 6)) + (B % (2 ** 6)) + cout1
    
    # Calculate the carry
    A9 = (A >> 5) % 2
    B9 = (B >> 5) % 2
    cout2 = (A9 & B9) 
    
    # We are done with the middle. Shift the numbers to the right
    A = A >> 6
    B = B >> 6
    
    # Finally, we do the same for the last 6 bits
    SUM10to15 = (A % (2 ** 6)) + (B % (2 ** 6)) + cout2
    
    # Combine the results
    SAAR16_estimate_sum = (SUM0to3) + (SUM4to9 << 4) + (SUM10to15 << 10)
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    SAAR16_estimate_sum = SAAR16_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return SAAR16_estimate_sum / scale_factor

def BPAA1_approx(num1, num2, tot_num_bits, inaccurate_bits):
    
    # UserWarning("BPAA1 is only implemented for multiples of 8.)
    tot_num_bits = max((tot_num_bits // 8) * 8, 8)
    
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    sum = 0
    cout = 0
    middle = tot_num_bits // 2
    
    for times in range(2):
        sum += ((num1 % (2** middle)) + (num2 % (2** middle)) + cout) << (times * middle)
        A15 = (num1 >> (middle - 1)) % 2
        B15 = (num2 >> (middle - 1)) % 2
        A14 = (num1 >> (middle-1)) % 2
        B14 = (num2 >> (middle-1)) % 2
        cout = (A15 & B15) | (A14 & B14) 
        num1 = num1 >> middle
        num2 = num2 >> middle
    sum = sum + cout
    
    sum = sum % (2 ** (tot_num_bits + 1))
    return sum / scale_factor

def BPAA2_approx(num1, num2, tot_num_bits, inaccurate_bits):
    
    # UserWarning("BPAA1 is only implemented for multiples of 8.)
    tot_num_bits = max((tot_num_bits // 8) * 8, 8)
    
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    sum = 0
    cout = 0
    middle = tot_num_bits // 2
    
    for times in range(2):
        sum += ((num1 % (2** middle)) + (num2 % (2** middle)) + cout) << (times * middle)
        A15 = (num1 >> (middle - 1)) % 2
        B15 = (num2 >> (middle - 1)) % 2
        cout = (A15 & B15) 
        num1 = num1 >> middle
        num2 = num2 >> middle
    sum = sum + cout
    
    sum = sum % (2 ** (tot_num_bits + 1))
    return sum / scale_factor

def NAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    X, Y, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    # Rename inaccurate bits to P in order to match the paper
    P = inaccurate_bits
    
    # Grab the P-1, P-2 and P-3 bits of both numbers
    X_P_1 = (X >> (P-1)) % 2
    Y_P_1 = (Y >> (P-1)) % 2
    X_P_2 = (X >> (P-2)) % 2
    Y_P_2 = (Y >> (P-2)) % 2
    X_P_3 = (X >> (P-3)) % 2
    Y_P_3 = (Y >> (P-3)) % 2
    
    # Get the carry bit
    carry = X_P_1 & Y_P_1
    
    # Get the accurate region
    accurate_region = (X >> P) + (Y >> P) + carry
    
    # Shift the accurate region back
    accurate_region = accurate_region << P
    
    SP_1 = (X_P_1 ^ Y_P_1) | (X_P_2 & Y_P_2)
    SP_2 = X_P_2 | Y_P_2 
    SP_3 = X_P_3 | Y_P_3
    
    # Shift the SP bits to the correct position
    SP_1 = SP_1 << (P-1)
    SP_2 = SP_2 << (P-2)
    SP_3 = SP_3 << (P-3)
    
    # The remaining bits are just 1
    S0toSP_4 = (2 ** (P-3)) - 1
    
    # Inaccurate region is the sum of all the bits
    inaccurate_region = SP_1 + SP_2 + SP_3 + S0toSP_4
    
    # Combine the accurate and inaccurate regions
    NAA_estimate_sum = accurate_region + inaccurate_region
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    NAA_estimate_sum = NAA_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return NAA_estimate_sum / scale_factor

def BPAA1_LSP1_approx(num1, num2, tot_num_bits, inaccurate_bits):
    if tot_num_bits != 16:
        # UserWarning("BPAA1_LSP1 is only implemented for 16-bit numbers. Will use 16-bit for this approx.")
        tot_num_bits = 16
    
    # Note: this will throw an error if inaccurate_bits is greater than 16
    A, B, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    # Compute the carry using A6/A7 and B6/B7
    A7 = (A >> 7) % 2
    A6 = (A >> 6) % 2
    B7 = (B >> 7) % 2
    B6 = (B >> 6) % 2
    
    Cout = (A6 & B6) | (A7 & B7)
    
    # Compute the accurate region, which is the last 8 bits
    accurate_region = (A >> 8) + (B >> 8) + Cout
    
    # Shift the accurate region back
    accurate_region = accurate_region << 8
    
    # Compute the inaccurate region, which is the first 8 bits which are all equal to 1
    inaccurate_region = (2 ** 8) - 1
    
    # Combine the accurate and inaccurate regions
    BPAA1_LSP1_estimate_sum = accurate_region + inaccurate_region
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    BPAA1_LSP1_estimate_sum = BPAA1_LSP1_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return BPAA1_LSP1_estimate_sum / scale_factor


def BPAA2_LSP1_approx(num1, num2, tot_num_bits, inaccurate_bits):
    if tot_num_bits != 16:
        # UserWarning("BPAA2_LSP1 is only implemented for 16-bit numbers. Will use 16-bit for this approx.")
        tot_num_bits = 16
    
    # Note: this will throw an error if inaccurate_bits is greater than 16
    A, B, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
    # Compute the carry using A8/A7 and B8/B7
    A7 = (A >> 7) % 2
    B7 = (B >> 7) % 2

    
    Cout = (A7 & B7)
    
    # Compute the accurate region, which is the last 8 bits
    accurate_region = (A >> 8) + (B >> 8) + Cout
    
    # Shift the accurate region back
    accurate_region = accurate_region << 8
    
    # Compute the inaccurate region, which is the first 8 bits which are all equal to 1
    inaccurate_region = (2 ** 8) - 1
    
    # Combine the accurate and inaccurate regions
    BPAA1_LSP1_estimate_sum = accurate_region + inaccurate_region
    
    # Ensure result is within the bounds defined by tot_num_bits + 1
    BPAA1_LSP1_estimate_sum = BPAA1_LSP1_estimate_sum % (2 ** (tot_num_bits + 1))
    
    # Scale the result back based on the scale factor for fractional representation, if necessary
    return BPAA1_LSP1_estimate_sum / scale_factor