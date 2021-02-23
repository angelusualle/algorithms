# O(N^2) where n is number of nums
def three_sum_zero(nums):
    nums.sort()
    answer = []
    for i in range(0, len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sumz = nums[i] + nums[j] + nums[k]
            if sumz == 0:
                answer.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif sumz < 0:
                j += 1
            else:
                k -= 1
    return answer