# O(N) time O(1) space
def remove_element(nums, val):
    pi = 0
    ni = 0
    while ni < len(nums):
        if nums[ni] != val:
            nums[pi] = nums[ni]
            pi+= 1
            ni += 1
        else:
            ni += 1
    return pi