# O(log(n)) time and O(1) space
def find_magic_index(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == arr[mid]:
            return mid
        elif mid > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
"""
# O(n) time and O(1) space
def find_magic_index(arr):
    for i, val in enumerate(arr):
        if i == val:
            return i
    return None
"""