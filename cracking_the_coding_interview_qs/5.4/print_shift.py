def print_shift(num):
    c = num
    c0 = 0
    c1 = 0
    while ((c & 1) == 0) and c!=0:
        c0 += 1
        c >>= 1
    while ((c & 1)):
        c1 += 1
        c >>= 1
    print(c0)
    print(c1)
    next_num = num + (1 << c0) + (1 << (c1 - 1)) - 1
    c0 = 0
    c1 = 0
    c = num
    while ((c &1) == 1):
        c1 += 1
        c >>= 1
    while ((c&1) == 0) and c!=0:
        c0 += 1
        c >>= 1
    previous_num = num - (1 << c1) - (1 << (c0 - 1)) + 1
    return next_num, previous_num