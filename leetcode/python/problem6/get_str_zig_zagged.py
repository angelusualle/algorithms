# O(N) where n is len of string
def get_str_zig_zagged(s, numRows):
    if numRows == 1:
        return s
    ret = ''
    n = len(s)
    cycle_len = numRows*2 - 2
    for i in range(numRows):
        j = 0
        while j +i < n:
            ret += s[j+i]
            if (i != 0 and i != numRows -1 and j + cycle_len -i < n):
                ret += s[j + cycle_len - i]
            j += cycle_len
    return ret