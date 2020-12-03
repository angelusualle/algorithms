def get_sum_pairs(nums, target):
    ans = []
    mem = {}
    for num in nums:
        if num in mem:
            ans.append((num, mem[num]))
        diff = target - num
        mem[diff] = num
    return ans