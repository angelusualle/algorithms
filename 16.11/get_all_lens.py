def get_all_lens(short, large, k):
    ans = set()
    j = 0
    while j <= k:
        ans.add(short*j + large*(k - j))
        j += 1
    return list(ans)