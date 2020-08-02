# O(nlog(n))
def place_k_elements_to_maximize_minimum_distance(locs, K, steps):
    locs.sort()
    low = 0
    high = locs[-1] - locs[0]
    res = -1
    for x in range(steps):
        mid = (high - low) / 2.0
        if is_feasible_mami(locs, K, mid):
            res = max(res, mid)
            low = mid
        else:
            high = mid
    return res
        
def is_feasible_mami(locs, K, dist):
    curr = locs[0]
    ks = 1
    for i in range(1,len(locs)):
        if locs[i] - curr >= dist:
            ks += 1
            curr = locs[i]
    return ks >= K

def get_minimized_maximum_distance(arr, K, precision = 1e-6):
    arr.sort()
    low = 0
    high = arr[-1] -arr[0]
    ans = float('inf')
    while abs(high-low) > precision:
        mid = (high + low) / 2.0
        if is_feasible_mima(arr, K, mid):
            ans = min(mid, ans)
            high = mid
        else:
            low = mid
    return ans

def is_feasible_mima(locs, K, dist):
    curr = locs[0] + dist * 2
    ks = 1
    for i in range(1,len(locs)):
        if curr < locs[i]:
            ks += 1
            curr = locs[i] + 2*dist
            continue
    return ks <= K