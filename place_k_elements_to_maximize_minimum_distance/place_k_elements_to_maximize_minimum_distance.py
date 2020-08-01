# Place k elements such that minimum distance is maximized
def place_k_elements_to_maximize_minimum_distance(locs, K, steps):
    locs.sort()
    low = 0
    high = locs[-1] - locs[0]
    res = -1
    print(steps)
    for x in range(steps):
        mid = (high - low) / 2.0
        if is_feasible(locs, K, mid):
            res = max(res, mid)
            low = mid
        else:
            high = mid
    return res
        


def is_feasible(locs, K, dist):
    curr = locs[0]
    ks = 1
    for i in range(1,len(locs)):
        if locs[i] - curr >= dist:
            ks += 1
            curr = locs[i]
    return ks >= K