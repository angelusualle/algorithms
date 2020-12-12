import math

def count_2s(num):
    count = 0
    len_ = len(str(num))
    for i in range(len_):
        count += count_2s_in_range(num, i)
    return count

def count_2s_in_range(num, i):
    p_tens = int(10**i)
    np_tens = int(p_tens * 10)
    right = num % p_tens
    round_down = num - num % np_tens
    roundup = round_down + np_tens
    z = (num / p_tens) % 10
    if z < 2:
        return round_down / 10
    elif z == 2:
        return round_down / 10 + right + 1
    else:
        return roundup / 10