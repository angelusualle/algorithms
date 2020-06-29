# Problem is to find largest distance a family would need to travel in an optimally placed 
# number of K post offices with families located on a real number line set of positions
# optimality here is minimizing the furthest distance from one location to a post office.
# return smallest possible value of maximum distance
def find_max_dist_optimal_k_post_offices_n_families(locs, K, precision = -1):
    locs.sort()
    top = locs[-1]
    bottom = locs[0]
    if precision == -1:
        precision = abs((top - bottom) / 100000) # Arbritrary scaled precision.
    hit = False
    while abs(top - bottom) > precision:
        half = (top - bottom) / 2 + bottom
        if not hit:
            if is_feasible(locs, K, half):
                hit = True
                top = half
                continue
            else:
                top = half
        if hit:
            if is_feasible(locs, K, half):
                top = half
            else:
                bottom = half
    return bottom

def is_feasible(locs, K, dist):
    start = locs[0] 
    start += dist * 2 
    K -= 1
    for x in locs[1:]:
        if start < x:
            K -= 1
            if K < 0:
                return False
            start = x + dist * 2
            continue
        start += dist * 2
    if K == 0: # 1
        return True
    else:
        return False