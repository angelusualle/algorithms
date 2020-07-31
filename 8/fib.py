
# O(n) time and O(1) with iterative bottom up approach
def fib(n):
    a = 0
    b = 1
    i = 2
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
    return a + b

# O(n) with caching, still O(n) space
def fib(n, cache = {}):
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    cache[n] = fib(n-1, cache)+ fib(n-2, cache)
    return cache[n]

# O(2^n) worst case no caching O(n) space
def fib(n):
    if n < 0:
        return None
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)