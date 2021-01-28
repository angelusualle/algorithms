# O(log(min(m+n))) time and space where m and n are size of arrs num1 and num2
def get_sorted_arrays_med(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    total = len(nums1) + len(nums2)
    half = total // 2
    l = 0
    r = len(nums1) - 1
    while True:
        i = (l + r) // 2
        print(l)
        print(r)
        print(i)
        j = half - i - 2

        nums1_l = nums1[i] if i >= 0  else float('-inf')
        nums1_r = nums1[i + 1] if (i+1) < len(nums1) else float('inf')

        nums2_l = nums2[j] if j >= 0 else float('-inf')
        nums2_r = nums2[j + 1] if (j+1) < len(nums2) else float('inf')

        
        if nums1_l <= nums2_r and nums2_l <= nums1_r:
            if total %2:
                return min(nums2_r, nums1_r)
            else:
                return ((min(nums2_r, nums1_r) + max(nums1_l, nums2_l)) / 2.0)
        elif nums1_l > nums2_r:
            r = i - 1
        else:
            l = i + 1



'''
# O(m+n) time and space where m and n are size of arrs num1 and num2
def get_sorted_arrays_med(nums1, nums2):
    concat = []
    i = 0
    j = 0
    while i < len(nums1) or j < len(nums2):
        if i < len(nums1):
            if j < len(nums2):
                if nums1[i] < nums2[j]:
                    concat.append(nums1[i])
                    i += 1
                else:
                    concat.append(nums2[j])
                    j += 1
            else:
                concat.append(nums1[i])
                i += 1
        else:
            concat.append(nums2[j])
            j += 1
    if len(concat) % 2 == 0:
        return (concat[len(concat) // 2 ] + concat[len(concat) //2 - 1]) / 2.0
    else:
        return concat[len(concat) // 2 ]
'''