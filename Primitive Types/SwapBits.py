def swap_bits(x, i, j):
    # Extract teh ith and jth bits, and see if they differ.
    if(x >> i) & 1 != (x >>j) & 1:
        # ith and jth bits differ. We will swap them by flipping their values.
        # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
        # when x = 0 we can perform the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x
