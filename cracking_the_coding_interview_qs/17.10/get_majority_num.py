# O(n) time and O(1) space
def get_majority_num(nums):
    count = 0
    for n in nums:
        if count == 0:
            majority = n
        if n == majority:
            count += 1
        else:
            count -= 1
    n_cnt  = 0
    for z in nums:
        if z == n:
            n_cnt += 1
    return n if n > len(nums) / 2 else -1