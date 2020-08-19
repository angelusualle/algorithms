def count_bits_diff(a,b):
    bits = 0
    bigger = a
    smaller = b
    if b > a:
        bigger = a
        smaller = b
    while bigger != 0:
        if smaller != 0:
            if bigger & 1 != smaller & 1:
                bits += 1
            smaller >>= 1
        else:
            bits += 1
        bigger >>= 1
    return  bits