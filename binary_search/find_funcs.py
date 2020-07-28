def find_val(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high +low) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return None

def find_last_in_series(arr, func):
    low = 0
    high = len(arr) - 1
    last_true = None
    while low <= high:
        mid = (high + low) // 2
        res = func(arr[mid])
        if res:
            low = mid + 1
            last_true = mid
        else:
            high = mid - 1
    return last_true

