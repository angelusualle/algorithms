import random

# position invariant
def random_subarray(nums, m):
    ans = [x for i, x in enumerate(nums) if i < m]
    i = m
    while i < len(nums):
        n = random.randint(0, i)
        if n < m:
            ans[n] = nums[i]
        i += 1
    return ans