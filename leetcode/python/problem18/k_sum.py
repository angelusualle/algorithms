def two_sum(nums ,target):
    res = []
    l, h = 0, len(nums) - 1
    while l < h:
        sumz = nums[l] + nums[h]
        if sumz < target or (l > 0 and nums[l] == nums[l-1]):
            l += 1
        elif sumz > target or (h < len(nums) - 1 and nums[h] == nums[h + 1]):
            h -= 1
        else:
            res.append([nums[l], nums[h]])
            l += 1
            h -= 1
    return res

# O(n^(k-1)) time, O(n) space
def k_sum(nums, target, k):
    nums.sort()
    res = []
    if len(nums) == 0 or nums[0] * k > target or target > nums[-1]*k:
        return res
    if k == 2:
        return two_sum(nums,target)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for _, set in enumerate(k_sum(nums[i+1:], target - nums[i], k-1)):
            res.append([nums[i]] + set)
    return res