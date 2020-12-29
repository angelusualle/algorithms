import heapq

# O(L*log(S)) runtime
def get_shortest_subsequence(short, long):
    refs = {x:[] for x in short}
    i = len(long) - 1
    while i >= 0:
        if long[i] in refs:
            refs[long[i]].append(i)
        i -= 1
    next_ones = []
    maxi = float('-inf')
    for x in refs:
        n = refs[x].pop()
        maxi = max(maxi, n)
        next_ones.append((n, x))
    heapq.heapify(next_ones)
    ans = None
    ans_range = float('inf')
    while True:
        min_pos, min_x = heapq.heappop(next_ones)
        if abs(min_pos - maxi) < ans_range:
            ans_range = abs(min_pos - maxi)
            ans = (min_pos, maxi)
        if refs[min_x]:
            n = refs[min_x].pop()
            maxi = max(n, maxi)
            heapq.heappush(next_ones, (n, min_x))
        else:
            break
    return ans
