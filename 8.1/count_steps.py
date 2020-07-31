# O(n) time with caching, O(n) space
def count_steps(n, cache = {}):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n in cache:
        return cache[n]
    cache[n] = count_steps(n - 1) + count_steps(n - 2) + count_steps(n - 3)
    return cache[n]

"""
# O(3^n) time, naive, no caching, O(n) space
def count_steps(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2 # 2 jump, or 1 jump 2 jump
    if n == 3:
        return 4
    count = 0
    count += count_steps(n -1) + count_steps(n - 3) + count_steps(n - 2)
    return count
"""