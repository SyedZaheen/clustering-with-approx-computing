import math

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

    scale_factor = max_num_digits - operand_max_digits

    num1 = int(num1 * 10 ** scale_factor)
    num2 = int(num2 * 10 ** scale_factor)

    return num1, num2, scale_factor
    

# Accurate Adder Sum
def accurate_adder(num1, num2, tot_num_bits, inaccurate_bits):

    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)

    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    total = num1 + num2
    total = total % (2 ** (tot_num_bits + 1))

    return total / 10 ** scale_factor


# HEAA Approx adder sum
def HEAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
    
        
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    if (
        ((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)
    ) == 0:
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits
        ) + ((num1 % (2 ** inaccurate_bits)) | (num2 % (2 ** inaccurate_bits)))
    else:
        HEAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + 1)
            << inaccurate_bits
        ) + (
            (num1 % (2 ** (inaccurate_bits - 1)))
            | (num2 % (2 ** (inaccurate_bits - 1)))
        )
    HEAA_estimate_sum = HEAA_estimate_sum % (2 ** (tot_num_bits + 1))
    return HEAA_estimate_sum / 10 ** scale_factor


# HOERAA Approx adder sum
def HOERAA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits, minimum_inaccurate_bits=2)

    
        
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    if (
        ((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)
    ) == 0:
        HOERAA_estimate_sum = (
            ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits
        ) + (
            (num1 % (2 ** inaccurate_bits))
            | (num2 % (2 ** inaccurate_bits))
            | (2 ** (inaccurate_bits - 2) - 1)
        )
    else:
        HOERAA_estimate_sum = (
            (
                ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + 1)
                << inaccurate_bits
            )
            + (
                (
                    ((num1 >> (inaccurate_bits - 2)) % 2)
                    & ((num2 >> (inaccurate_bits - 2)) % 2)
                )
                << (inaccurate_bits - 1)
            )
            + (
                (num1 % (2 ** (inaccurate_bits - 1)))
                | (num2 % (2 ** (inaccurate_bits - 1)))
                | (2 ** (inaccurate_bits - 2) - 1)
            )
        )
    HOERAA_estimate_sum = HOERAA_estimate_sum % (2 ** (tot_num_bits + 1))
    return HOERAA_estimate_sum / 10 ** scale_factor

# TODO: Unexpected behavior when inaccurate_bits < 3
# HOAANED Approx adder sum
def HOAANED_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits, minimum_inaccurate_bits=3)

        
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    if (
        ((num1 >> (inaccurate_bits - 1)) % 2) & ((num2 >> (inaccurate_bits - 1)) % 2)
    ) == 0:
        HOAANED_estimate_sum = (
            (((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits)) << inaccurate_bits)
            + ((
                (
                    (
                        ((num1 >> (inaccurate_bits - 2)) % 2)
                        & ((num2 >> (inaccurate_bits - 2)) % 2)
                    )
                    | (
                        ((num1 >> (inaccurate_bits - 1)) % 2)
                        | ((num2 >> (inaccurate_bits - 1)) % 2)
                    )
                )
                << (inaccurate_bits - 1)
            )
            + (
                (num1 % (2 ** (inaccurate_bits - 1)))
                | (num2 % (2 ** (inaccurate_bits - 1)))
                | (2 ** (inaccurate_bits - 2) - 1)
            )) if inaccurate_bits > 2 else 2 ** (inaccurate_bits + 1) - 1
        )
    else:
        HOAANED_estimate_sum = (
            (
                ((num1 >> inaccurate_bits) + (num2 >> inaccurate_bits) + 1)
                << inaccurate_bits
            )
            + ( 
            (
                (
                    ((num1 >> (inaccurate_bits - 2)) % 2)
                    & ((num2 >> (inaccurate_bits - 2)) % 2)
                )
                << (inaccurate_bits - 1)
            )
            + (
                (num1 % (2 ** (inaccurate_bits - 1)))
                | (num2 % (2 ** (inaccurate_bits - 1)))
                | (2 ** (inaccurate_bits - 2) - 1)
            ) 
            ) if inaccurate_bits > 2 else 2 ** (inaccurate_bits + 1) - 1
        )
    HOAANED_estimate_sum = HOAANED_estimate_sum % (2 ** (tot_num_bits + 1))
    return HOAANED_estimate_sum / 10 ** scale_factor


# M-HERLOA Approx adder sum
def M_HERLOA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
        
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    if inaccurate_bits >= 4:
        M_HERLOA_estimate_sum = (
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
                    | (2 ** (inaccurate_bits - 4) - 1)
                )
            )
        )
    elif inaccurate_bits == 3:
        M_HERLOA_estimate_sum = (
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
            )
        )

    M_HERLOA_estimate_sum = M_HERLOA_estimate_sum % (2 ** (tot_num_bits + 1))
    return M_HERLOA_estimate_sum / 10 ** scale_factor


