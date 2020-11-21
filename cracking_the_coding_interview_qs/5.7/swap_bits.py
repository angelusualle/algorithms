def swap_bits(num):
    return (num & 0xaaaaaaaaaa) >> 1 | (num & 0x5555555555) << 1