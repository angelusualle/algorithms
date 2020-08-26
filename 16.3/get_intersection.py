def get_intersection(p1s, p2s):
    slope1 = (p1s[1][1] - p1s[0][1]) / (p1s[1][0] - p1s[0][0])
    slope2 = (p2s[1][1] - p2s[0][1]) / (p2s[1][0] - p2s[0][0])
    intercept1 = p1s[0][1] - slope1*p1s[0][0]
    intercept2 = p2s[0][1] - slope2*p2s[0][0]
    x = (intercept2 - intercept1) / (slope1 - slope2)
    bigger = p1s[0][0]
    smaller = p1s[1][0]
    if smaller > bigger:
        bigger, smaller = smaller, bigger
    if x <= bigger and x >= smaller:
        bigger = p2s[0][0]
        smaller = p2s[1][0]
        if smaller > bigger:
            bigger, smaller = smaller, bigger
        if x <= bigger and x >= smaller:
            return (x, slope1*x+intercept1)
        else:
            return None
    else:
        return None
