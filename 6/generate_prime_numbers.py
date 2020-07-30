import math
# O(nlogn) time and O(n) space
def generate_prime_numbers(n):
    if n < 2:
        return None
    ans = []
    for i in range(2, n + 1):
        ans.append(i)
    flags = [1] * len(ans)
    i = 0
    while i < len(ans):
        val = ans[i]
        j = i+1
        while j < len(ans):
            if ans[j] % val == 0:
                flags[j] = 0
            j += 1
        i += 1
        while i < len(ans) and not flags[i]:
            i += 1
    return [x for i,x in enumerate(ans) if flags[i]]



# O(sqrt(n)) better
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""
# O(n) naive
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
"""