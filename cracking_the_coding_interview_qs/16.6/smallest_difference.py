# O(nlog(n) + mlog(m)) time optimum, O(1) space
def smallest_difference(nums1, nums2):
    nums1.sort()
    nums2.sort()
    min_val = float('inf')
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        min_val = min(min_val, abs(nums1[i] - nums2[j]))
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return min_val
"""
# O(nm) time where n,m are sizes of lists, O(1) space, brute force
def smallest_difference(nums1, nums2):
    nums1.sort()
    nums2.sort()
    min_val = float("inf")
    for num1 in nums1:
        for num2 in nums2:
            min_val = min(min_val, abs(num1 - num2))
    return min_val
"""