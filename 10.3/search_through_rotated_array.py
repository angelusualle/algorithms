# O(logn) binary search with virtual extension
def search_through_rotated_array(arr, val):
    low = 0
    high = len(arr) * 2 - 1
    while low <= high:
        mid = (low + high) // 2
        if mid > len(arr) - 1:
            if arr[mid - len(arr)] == val:
                return mid-len(arr)
            elif arr[mid - len(arr)] < val:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1