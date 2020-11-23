# O(n) time and O(1) space
def get_max_cont(arr):
    max_sum = float('-inf')
    sumz = 0
    for num in arr:
        sumz += num
        if sumz > max_sum:
            max_sum = sumz
        elif sumz < 0:
            sumz = 0
    return max_sum