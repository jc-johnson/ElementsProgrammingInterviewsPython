
# Since we perform O(1)computation per bit, the run time is O(1). 
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits
