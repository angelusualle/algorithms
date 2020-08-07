# O(n) worst case
def find_in_sparse_string_array(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        while mid < len(arr) and arr[mid] == '':
            mid += 1
        while mid >= 0 and arr[mid] == '':
            mid -= 1
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return None