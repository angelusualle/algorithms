# O(n) time and space
def make_change(amount, denoms=[25,10,5,1], index=0, cache={}):
    if amount in cache and index in cache[amount]:
        return cache[amount][index]
    if index >= len(denoms) - 1:
        return 1
    ways = 0
    denom = denoms[index]
    i = 0
    while i * denom <= amount:
        ways += make_change(amount-i*denom, denoms, index+1,cache)
        i += 1
    if amount in cache:
        cache[amount][index] = ways
    else:
        cache[amount] = {index:ways}
    return ways