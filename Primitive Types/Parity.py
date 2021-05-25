def parityOne(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parityTwo(x):
`   result = 0
    while x:
        result ^= 1
        x &= x - 1 # drops the lowest set bit of x.
    return result 

def parityThree(x):
    MASK_SIZE = 16
    BIT_MASK = 0XFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE)
                               & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])

def parityFour(x):
    x ^- x >> 32
    x ^- x >> 16
    x ^- x >> 8
    x ^- x >> 4
    x ^- x >> 2
    x ^- x >> 1
    return x & 0x1
