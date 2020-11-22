def get_sort_indexes(arr):
    arr2 = merge_sorted(arr)
    n = len(arr) - 1
    m = 0
    n_done = False
    m_done = False
    while n != m and not (n_done and m_done):
        if arr[n] == arr2[n]:
            n -= 1
        else:
            n_done = True
        if arr[m] == arr2[m]:
            m += 1
        else:
            m_done = True
    return m, n

def merge_sorted(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    l = merge_sorted(arr[:mid])
    r = merge_sorted(arr[mid:])
    return merge(l,r)

def merge(l,r):
    ans = l[:]
    ans.extend(r[:])
    i1 = 0
    i2 = 0
    z = 0
    while i1 < len(l) and i2 < len(r):
        if l[i1] <= r[i2]:
            ans[z] = l[i1]
            i1 += 1
            z += 1
        else:
            ans[z] = r[i2]
            i2 += 1
            z += 1
    while i1 < len(l):
        ans[z] = l[i1]
        i1 += 1
        z += 1
    return ans