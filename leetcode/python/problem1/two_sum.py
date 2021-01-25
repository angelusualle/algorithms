def two_sum(nums, target):
    diffs = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in diffs:
            return i, diffs[diff]
        diffs[n] = i
    return None, None