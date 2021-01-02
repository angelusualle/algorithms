# O(n) time O(n) space
def histo_volume(hist):
    left_max = hist[:]
    l_max = hist[0]
    for i in range(len(hist)):
        l_max = max(l_max, hist[i])
        left_max[i] = l_max
    ans = 0

    r_max = hist[-1]
    for i in range(len(hist)-1, -1, -1):
        r_max = max(r_max, hist[i])
        second_tallest = min(r_max, left_max[i])
        if second_tallest > hist[i]:
            ans += second_tallest - hist[i]
    return ans
