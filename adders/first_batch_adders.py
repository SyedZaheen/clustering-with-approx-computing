from .utils import prepare_operands
# Accurate Adder Sum
def accurate_adder(num1, num2, tot_num_bits, inaccurate_bits):

    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)

    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    total = num1 + num2
    total = total % (2 ** (tot_num_bits + 1))

    return total / scale_factor


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
    return HEAA_estimate_sum / scale_factor


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
    return HOERAA_estimate_sum / scale_factor

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
    return HOAANED_estimate_sum / scale_factor


# M-HERLOA Approx adder sum
def M_HERLOA_approx(num1, num2, tot_num_bits, inaccurate_bits):
    num1, num2, scale_factor = prepare_operands(num1, num2, tot_num_bits, inaccurate_bits)
        
    num1 = num1 % (2 ** tot_num_bits)
    num2 = num2 % (2 ** tot_num_bits)
    if inaccurate_bits > 5:
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
    elif 4 <= inaccurate_bits <= 5:
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
                (num1 % (2 ** (inaccurate_bits - 1)))
                | (num2 % (2 ** (inaccurate_bits - 1)))
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
                    | (2 ** (inaccurate_bits - 3) - 1)
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
    return M_HERLOA_estimate_sum / scale_factor


