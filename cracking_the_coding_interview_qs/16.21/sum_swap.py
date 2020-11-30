# O(N + M) time and space
def sum_swap(a, b):
    a_sum = 0
    a_s = {}
    b_sum = 0
    b_s = {}
    for i, n in enumerate(a):
        a_sum += n
        a_s[n] = i
    for i, n in enumerate(b):
        b_sum += n
        b_s[n] = i
    diff = (a_sum - b_sum + 1) // 2
    for i, n in enumerate(a):
        if n - diff in b_s:
            return i, b_s[n - diff]
    return None