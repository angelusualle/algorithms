def find_closest_sum(nums, target):
    answer = None
    nums.sort()
    for i in range(0, len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sumz = nums[i] + nums[j] + nums[k]
            if answer is None or abs(target-sumz) < abs(target-answer):
                answer = sumz
            if target < sumz:
                k -= 1
            else:
                j += 1
    return answer