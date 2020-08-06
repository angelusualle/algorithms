# O(logn) binary search little duplices O(n) with duplicates
def search_through_rotated_array(arr, val, left = 0, right = -1):
    if right == -1:
        right = len(arr) - 1
    mid = (right + left) // 2
    if arr[mid] == val:
        return mid
    if arr[left] < arr[mid]:
        if val >= arr[left] and val < arr[mid]:
            return search_through_rotated_array(arr, val, left, mid - 1)
        else:
            return search_through_rotated_array(arr, val, mid + 1, right)
    elif arr[right] > arr[mid]:
        if val <= arr[right] and val > arr[mid]:
            return search_through_rotated_array(arr, val, mid + 1, right)
        else:
            return search_through_rotated_array(arr, val, left, mid - 1)
    elif arr[left] == arr[mid]:
        if arr[mid] != arr[right]:
            return search_through_rotated_array(arr, val, mid + 1, right)
        else:
            result = search_through_rotated_array(arr, val, mid - 1, x)
            if result is None:
                return search_through_rotated_array(arr, val, mid + 1, right)
            else:
                return None
    return None