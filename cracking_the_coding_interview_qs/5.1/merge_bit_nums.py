import bitarray

# O(n + m) where n and m are size in bits of nums
def merge_bit_nums(n, m, i, j):
    ans = bitarray.bitarray(len(n)+len(m))
    ans_i = 0
    n_i = 0
    m_i = 0
    while ans_i < len(ans):
        print(ans)
        if ans_i >= i and ans_i <= j:
            ans[ans_i] = m[m_i]
            m_i += 1
        else:
            ans[ans_i] = n[n_i]
            n_i += 1
        ans_i += 1
    return ans
